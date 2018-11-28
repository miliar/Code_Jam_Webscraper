#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

typedef long long int64;
typedef double real;

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif

const int MaxN = 1003, MaxC = 0x3F3F3F3F, NA = -1;

real ya [MaxN], yb [MaxN], s [MaxN];
int m, n;

int main (void)
{
 int test, tests;
 real cx, cy, ox, oy, u, v, lo, me, hi;
 int g, i, j, w, p;
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d %d %d %d", &w, &m, &n, &g);
  cx = cy = 0;
  for (j = 0; j < m; j++)
  {
   ox = cx;
   oy = cy;
   scanf (" %lf %lf", &cx, &cy);
   for (i = ox; i <= cx; i++)
   {
    ya[i] = oy + (cy - oy) / (cx - ox) * (i - ox);
   }
  }
  cx = cy = 0;
  for (j = 0; j < n; j++)
  {
   ox = cx;
   oy = cy;
   scanf (" %lf %lf", &cx, &cy);
   for (i = ox; i <= cx; i++)
   {
    yb[i] = oy + (cy - oy) / (cx - ox) * (i - ox);
   }
  }

  s[0] = 0.0;
  for (i = 0; i < w; i++)
   s[i + 1] = s[i] + 0.5 * ((yb[i] - ya[i]) + (yb[i + 1] - ya[i + 1]));

/*
  for (i = 0; i <= w; i++)
   printf ("%d: %.6lf %.6lf %.6lf\n", i, ya[i], yb[i], s[i]);
*/

  printf ("Case #%d:\n", test);
  for (j = 1; j < g; j++)
  {
   v = s[w] / g * j;
   for (i = 0; i < w; i++)
    if (v < s[i])
     break;
   assert (i > 0);
//   printf ("%.6lf %d\n", v, i);
   oy = yb[i - 1] - ya[i - 1];
   cy = yb[i] - ya[i];
   lo = 0.0;
   hi = 1.0;
   for (p = 0; p < 100; p++)
   {
    me = (lo + hi) * 0.5;
    u = oy + (cy - oy) * me;
    u = 0.5 * me * (oy + u);
//    printf ("%.6lf: %.6lf %.6lf %.6lf\n", me, v, s[i - 1], u);
    if (v > s[i - 1] + u)
     lo = me;
    else
     hi = me;
   }
   printf ("%.6lf\n", i - 1 + lo);
  }
 }
 return 0;
}
