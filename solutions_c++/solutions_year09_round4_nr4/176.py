#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

const int maxn = 1000;

double x[maxn], y[maxn], r[maxn];
int n, nt;

double d( int i, int j )
{
  return sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]));
}

int main()
{
  scanf("%d", &nt);
  for (int tt = 1; tt <= nt; tt++)
  {
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
      scanf("%lf%lf%lf", &x[i], &y[i], &r[i]);
    double ans = 1e100;
    if (n == 1)
      ans = r[0];
    if (n == 2)
      ans = max(r[0], r[1]);
    if (n == 3)
    {
      double d0 = d(1, 2), d1 = d(0, 2), d2 = d(0, 1);
      double r0 = max(r[0], (d0 + r[1] + r[2]) * 0.5);
      double r1 = max(r[1], (d1 + r[0] + r[2]) * 0.5);
      double r2 = max(r[2], (d2 + r[1] + r[0]) * 0.5);
      ans = min(r0, min(r1, r2));
    }
    printf("Case #%d: %.6lf\n", tt, ans);
  }
  return 0;
}
