#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <cstdio>

using namespace std;

const int MAXN = 10000;

int N, D;
int d[MAXN+1], l[MAXN+1], res[MAXN+1];

void solve()
{
  memset(res, -1, sizeof(res));

  res[1] = 0;

  for (int i = 1; i <= N; ++i) {
    if (res[i] == -1) continue;

    for (int j = i+1; j <= N; ++j)
      if (d[i] + min(d[i] - d[res[i]], l[i]) >= d[j] && (res[j] == -1 || res[j] > i)) res[j] = i;
  }

  for (int i = 1; i <= N; ++i) {
    if (res[i] != -1) {
      if (d[i] + min(d[i] - d[res[i]], l[i]) >= D) { printf(" YES\n"); return; }
    }
  }

  printf(" NO\n");
}

int main()
{
  int T; scanf("%d", &T);

  for (int t = 0; t < T; ++t) {
    scanf("%d", &N);

    for (int i = 0; i < N; ++i) scanf("%d%d", &d[i+1], &l[i+1]);

    scanf("%d", &D);

    printf("Case #%d:", t+1);
    solve();
  }

  return 0;
}
