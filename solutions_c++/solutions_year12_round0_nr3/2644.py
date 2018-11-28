#include <algorithm>
#include <cstdio>

using namespace std;

const int MAXN = 2000000;

bool mark[10000000];
int seq[MAXN+1][11], ns = 0;

int main()
{
  int dig[100];

  for (int i = 1; i <= MAXN; ++i) {
    if (mark[i]) continue;

    int ti = i, l = 0;
    while (ti > 0) { dig[l++] = ti % 10; ti /= 10; }

    for (int s = l-1; s < 2*l-1; ++s) {
      dig[s+1] = dig[s-l+1];
      if (dig[s] == 0) continue;

      int cur = 0;
      for (int j = 0; j < l; ++j) cur = cur*10 + dig[s-j];

      if (mark[cur]) continue;
      mark[cur] = true;

      ++seq[ns][0]; seq[ns][seq[ns][0]] = cur;
    }

    sort(&seq[ns][1], &seq[ns][seq[ns][0] + 1]);
    ++ns;
  }

  int T; scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    int A, B, res = 0;
    scanf("%d%d", &A, &B);

    for (int i = 0; i < ns; ++i) {
      int l = 0;

      for (int j = 1; j <= seq[i][0]; ++j)
        if (seq[i][j] >= A && seq[i][j] <= B) ++l;

      res += (l*l-l) / 2;
    }

    printf("Case #%d: %d\n", t, res);
  }
}
