#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long double dbl;

#define forn(i,n) for (int i = 0; i < (int)(n); i++)

#define eps 1e-12

#define maxn 1010

int n;
int x[maxn], y[maxn], z[maxn], p[maxn];

bool test( dbl power )
{
//   fprintf(stderr, "test(power=%.5Lf)\n", power);
  dbl minx = -1e9, maxx = 1e9;
  dbl miny = -1e9, maxy = 1e9;
  dbl minz = -1e9, maxz = 1e9;
  forn (i, n)
  {
    dbl dist = power * p[i];
    dbl tx = x[i] + y[i] + z[i];
    dbl ty = x[i] + y[i] - z[i];
    dbl tz = x[i] - y[i] + z[i];
//     fprintf(stderr, "(%.3Lf,%.3Lf,%.3Lf)\n", tx, ty, tz);
    minx = max(minx, tx - dist);
    maxx = min(maxx, tx + dist);
    miny = max(miny, ty - dist);
    maxy = min(maxy, ty + dist);
    minz = max(minz, tz - dist);
    maxz = min(maxz, tz + dist);
  }
//   fprintf(stderr, "%d\n", minx <= maxx + eps && miny <= maxy + eps && minz <= maxz + eps);
  if (minx <= maxx + eps && miny <= maxy + eps && minz <= maxz + eps)
    return true;
  else
    return false;
}

int main()
{
  int nn;
  scanf("%d", &nn);
  forn (tst, nn)
  {
    scanf("%d", &n);
    forn (i, n)
      scanf("%d%d%d%d", &x[i], &y[i], &z[i], &p[i]);
    dbl mn = 0.0, mx = 1e20;
//     return test(0.0);
    forn (ttt, 150)
    {
      dbl power = (mn + mx) / 2;
      if (test(power))
        mx = power;
      else
        mn = power;
    }
    printf("Case #%d: %.6Lf\n", tst + 1, mn);
  }
  return 0;
}

