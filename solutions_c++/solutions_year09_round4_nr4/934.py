#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <set>
#include <string>
#include <vector>

using namespace std;

typedef double real;
typedef long long int64;

const int MaxN = 40;
const real eps = 1E-9, MaxC = 1E25;
const real INV = 1.0 / real (RAND_MAX);

int x [MaxN], y [MaxN], r [MaxN];
real a [MaxN] [MaxN] [MaxN];
int64 b [MaxN] [MaxN] [MaxN];
int n;
int64 m;

#define sqr(o) ((o)*(o))

inline int vp (int x0, int y0, int x1, int y1, int x2, int y2)
{
 return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0);
}

inline int rho2 (int x1, int y1, int x2, int y2)
{
 return sqr (x2 - x1) + sqr (y2 - y1);
}

inline real rho (int x1, int y1, int x2, int y2)
{
 return sqrt (rho2 (x1, y1, x2, y2));
}

inline bool inside (real cr, real cx, real cy, int u)
{
 return (hypot (cx - x[u], cy - y[u]) + r[u] <= cr + 1E-7);
}

void calc (int u, int v, int w)
{
 real cr, cx, cy;
 int i;

 if (vp (x[u], y[u], x[v], y[v], x[w], y[w]))
 {
  const int STEPS = 12;
  real a, d, tx, ty, tr;

  cx = (x[u] + x[v] + x[w]) / 3.0;
  cy = (y[u] + y[v] + y[w]) / 3.0;
  cr = MaxC;
  for (d = 600.0; d > 1E-10; d *= 0.5)
  {
   cr = max (max (hypot (cx - x[u], cy - y[u]) + r[u],
                  hypot (cx - x[v], cy - y[v]) + r[v]),
                  hypot (cx - x[w], cy - y[w]) + r[w]);
   while (1)
   {
    real mr, mx, my;
    mr = cr; mx = cx; my = cy;
    for (i = 0; i < STEPS; i++)
    {
     a = (rand () * INV) * 2.0 * M_PI;
//     a = (2.0 * M_PI * i) / STEPS;
     tx = cx + d * cos (a);
     ty = cy + d * sin (a);
//     printf ("%.10lf %.10lf\n", tx, ty);
     tr = max (max (hypot (tx - x[u], ty - y[u]) + r[u],
                    hypot (tx - x[v], ty - y[v]) + r[v]),
                    hypot (tx - x[w], ty - y[w]) + r[w]);
     if (mr > tr)
     {
      mx = tx;
      my = ty;
      mr = tr;
     }
    }
    if (mr == cr)
     break;
    cr = mr;
    cx = mx;
    cy = my;
   }
/*
   printf ("%18.10lf: %18.10lf %18.10lf %18.10lf\n", d, cr, cx, cy);
   fflush (stdout);
*/
  }
 }
 else
 {
  int a, b, c;

  a = rho2 (x[u], y[u], x[v], y[v]);
  b = rho2 (x[v], y[v], x[w], y[w]);
  c = rho2 (x[w], y[w], x[u], y[u]);
  if (a || b || c)
  {
   if (b >= c && b >= a)
    swap (u, w);
   else if (c >= a && c >= b)
    swap (v, w);

   real dx, dy, dd;
   dx = x[v] - x[u];
   dy = y[v] - y[u];
   dd = hypot (dx, dy);
   assert (dd != 0.0);
   dd = 1.0 / dd;
   dx *= dd;
   dy *= dd;

   vector <pair <real, real> > e;
   e.push_back (make_pair (x[u] - dx * r[u], y[u] - dy * r[u]));
   e.push_back (make_pair (x[u] + dx * r[u], y[u] + dy * r[u]));
   e.push_back (make_pair (x[v] - dx * r[v], y[v] - dy * r[v]));
   e.push_back (make_pair (x[v] + dx * r[v], y[v] + dy * r[v]));
   e.push_back (make_pair (x[w] - dx * r[w], y[w] - dy * r[w]));
   e.push_back (make_pair (x[w] + dx * r[w], y[w] + dy * r[w]));
   sort (e.begin (), e.end ());
   cx = (e[0].first  + e[5].first ) * 0.5;
   cy = (e[0].second + e[5].second) * 0.5;
   cr = hypot (cx - e[0].first, cy - e[0].second);

   if (b >= c && b >= a)
    swap (u, w);
   else if (c >= a && c >= b)
    swap (v, w);
  }
  else
  {
   cr = max (max (r[u], r[v]), r[w]);
   cx = x[u];
   cy = y[u];
  }
 }

 ::a[u][v][w] = cr;
 b[u][v][w] = 0;
 for (i = 0; i < n; i++)
  if (inside (cr, cx, cy, i))
   b[u][v][w] |= 1ll << (int64) i;
 assert (b[u][v][w] | (1ll << (int64) u));
 assert (b[u][v][w] | (1ll << (int64) v));
 assert (b[u][v][w] | (1ll << (int64) w));
/*
 printf ("%3d %3d %3d: %14.6lf %14.6lf %14.6lf %I64d\n",
  u, v, w, cr, cx, cy, b[u][v][w]);
 fflush (stdout);
*/
}

int main (void)
{
 int test, tests;
 int i, u1, v1, w1, u2, v2, w2;
 srand (123);
 scanf (" %d", &tests);
 for (test = 1; test <= tests; test++)
 {
  scanf (" %d", &n);
  for (i = 0; i < n; i++)
   scanf (" %d %d %d", &x[i], &y[i], &r[i]);
  m = 1ll << (int64) n;

  for (u1 = 0; u1 < n; u1++)
   for (v1 = u1; v1 < n; v1++)
    for (w1 = v1; w1 < n; w1++)
     calc (u1, v1, w1);

  real cur, res;
  res = MaxC;
  for (u1 = 0; u1 < n; u1++)
   for (v1 = u1; v1 < n; v1++)
    for (w1 = v1; w1 < n; w1++)
     for (u2 = u1 + 1; u2 < n; u2++)
      for (v2 = u2; v2 < n; v2++)
       for (w2 = v2; w2 < n; w2++)
        if ((b[u1][v1][w1] | b[u2][v2][w2]) == m - 1)
         if (res > (cur = max (a[u1][v1][w1], a[u2][v2][w2])))
          res = cur;
  printf ("Case #%d: %.10lf\n", test, (double) res);
  fflush (stdout);
 }
 return 0;
}
