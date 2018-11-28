#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int MAXN = 10;

int N;
int x[MAXN], y[MAXN];

int calc(int i, int d)
{
  int jmax = i+1;

  for (int j = i+2; j <= d; ++j)
  {
    if (y[j] * (jmax-i) > y[i]*(jmax-i) + (y[jmax]-y[i])*(j-i)) jmax = j;
  }

  return jmax;
}

bool go(int d)
{
  if (d == N) {
    return true;
  }

  for (y[d] = 0; ; ++y[d]) {
    bool good = true;

    for (int i = 0; i < d; ++i)
      if (x[i] < d) {
        int k = calc(i, d);

        if (k == d) return false;
      } else if (x[i] == d) {
        int k = calc(i, d);

        if (k < d) { good = false; break; }
      }

    if (good && go(d+1)) return true;
  }

  return false;
}

void solve()
{
  for (int i = 0; i < N-1; ++i)
    for (int j = i+1; j < x[i]; ++j)
      if (x[j] > x[i]) { printf(" Impossible\n"); return; }

  y[0] = 0;
  go(1);

  for (int i = 0; i < N; ++i) printf(" %d", y[i]);
  printf("\n");
}

int main()
{
  int T; scanf("%d", &T);

  for (int t = 0; t < T; ++t) {
    scanf("%d", &N);

    for (int i = 0; i < N-1; ++i) { scanf("%d", &x[i]); --x[i]; }

    printf("Case #%d:", t+1);
    solve();
  }

  return 0;
}
