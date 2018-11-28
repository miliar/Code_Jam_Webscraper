#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

typedef double real;

const int MaxN = 509;
const real eps = 1E-9;

real x [MaxN], y [MaxN], z [MaxN];
real dx [MaxN], dy [MaxN], dz [MaxN];

#define sqr(o) ((o)*(o))

int main (void)
{
 int test, tests;
 real tmin, dmin, xc, yc, zc, xb, yb, zb, xd, yd, zd, d;
 int i, n;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d", &n);
  xc = yc = zc = 0;
  xb = yb = zb = 0;
  for (i = 0; i < n; i++)
  {
   scanf (" %lf %lf %lf %lf %lf %lf",
    &x[i], &y[i], &z[i], &dx[i], &dy[i], &dz[i]);
   xc += x[i];
   yc += y[i];
   zc += z[i];
   xb += x[i] + dx[i];
   yb += y[i] + dy[i];
   zb += z[i] + dz[i];
  }
  xc /= n;
  yc /= n;
  zc /= n;
  xb /= n;
  yb /= n;
  zb /= n;
  xd = xb - xc;
  yd = yb - yc;
  zd = zb - zc;
  d = sqr (xd) + sqr (yd) + sqr (zd);
  if (d < eps)
  {
   tmin = 0.0;
   dmin = sqrt (sqr (xc) + sqr (yc) + sqr (zc));
  }
  else
  {
   tmin = -(xc * xd + yc * yd + zc * zd) / d;
   if (tmin < 0.0)
   tmin = 0.0;
   dmin = sqrt (sqr (xc + xd * tmin) +
                sqr (yc + yd * tmin) +
                sqr (zc + zd * tmin));
  }
  printf ("Case #%d: %.10lf %.10lf\n", test, dmin, tmin);
 }
 return 0;
}
