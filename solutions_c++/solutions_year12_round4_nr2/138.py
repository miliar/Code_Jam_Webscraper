#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <cstdio>

using namespace std;

const int MAXN = 1000;

int N;
pair<double, int> z[MAXN];
double r[MAXN], x[MAXN], y[MAXN];
double rx[MAXN], ry[MAXN], L, W;

void solve()
{
  for (int i = 0; i < N; ++i)
    z[i] = make_pair(r[i], i);

  sort(&z[0], &z[N]);
  x[N-1] = 0.0; y[N-1] = 0.0;

  for (int i = N-2; i >= 0; --i) {
    bool bad = true;

    while (bad) {
      x[i] = rand() / (1.0 * RAND_MAX) * W;
      y[i] = rand() / (1.0 * RAND_MAX) * L;

      bad = false;

      for (int j = i+1; j < N; ++j)
        if ((x[j]-x[i])*(x[j]-x[i]) + (y[j]-y[i])*(y[j]-y[i]) < (z[i].first + z[j].first + 1e-2)*(z[i].first + z[j].first + 1e-2)) {
          bad = true; break;
        }
    }
  }

  for (int i = 0; i < N; ++i) {
    rx[z[i].second] = x[i];
    ry[z[i].second] = y[i];
  }

  for (int i = 0; i < N; ++i)
    printf(" %.5lf %.5lf", rx[i], ry[i]);

  printf("\n");
}

int main()
{
  int T; scanf("%d", &T);

  for (int t = 0; t < T; ++t) {
    scanf("%d%lf%lf", &N, &W, &L);

    for (int i = 0; i < N; ++i) scanf("%lf", &r[i]);

    printf("Case #%d:", t+1);
    solve();
  }

  return 0;
}
