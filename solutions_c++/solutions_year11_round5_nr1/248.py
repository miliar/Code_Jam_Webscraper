#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const double eps = 1e-9;

int main (void)
{
  int test, tests, i, j;
  int w, l, u, g;
  double le, ri, me, meyu, meyl;
  double res, s, ts;
  double lx[123], ly[123];
  double ux[123], uy[123];
  freopen ("a-large.in", "rt", stdin);
  freopen ("a-large.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    res = 0;
    scanf ("%d %d %d %d", &w, &l, &u, &g);
    for (i = 0; i < l; i++)
      scanf ("%lf %lf", &lx[i], &ly[i]);
    for (i = 0; i < u; i++)
      scanf ("%lf %lf", &ux[i], &uy[i]);

    for (i = 1; i < l; i++)
      res -=  (lx[i] - lx[i-1]) * (ly[i] + ly[i-1]) / 2;

    for (i = 1; i < u; i++)
      res +=  (ux[i] - ux[i-1]) * (uy[i] + uy[i-1]) / 2;

    printf ("Case #%d:\n", test + 1);
    for (j = 1; j < g; j++)
    {
      s = res / g * j;
      le = me = 0;
      ri = w;
      while (ri - le > eps)
      {
        me = (le + ri) / 2;
        ts = 0;
        for (i = 1; lx[i] < me; i++)
          ts -= (lx[i] - lx[i-1]) * (ly[i] + ly[i-1]) / 2;

        meyl = (ly[i] + ly[i-1] * (lx[i] - me) / (me - lx[i-1])) /
               (1 + (lx[i] - me) / (me - lx[i-1]));

        ts -= (me - lx[i-1]) * (meyl + ly[i-1]) / 2;

        for (i = 1; ux[i] < me; i++)
          ts +=  (ux[i] - ux[i-1]) * (uy[i] + uy[i-1]) / 2;
        
        // (lx[i] - me)/(me - lx[i-1]) = (ly[i] - meyl) /(meyl - ly[i-1])
        // ly[i] - meyl = (meyl - ly[i - 1]) (lx[i] - me)/(me - lx[i-1]);
        // meyl (-1 - (lx - me) / (me - lx)) = -ly[i] - ly[i-1] ()/ ()
        // meyl (1 + (lx - me) / (me - lx)) = ly[i] + ly[i-1] () /()
        
        meyu = (uy[i] + uy[i-1] * (ux[i] - me) / (me - ux[i-1])) /
               (1 + (ux[i] - me) / (me - ux[i-1]));
        ts += (me - ux[i-1]) * (meyu + uy[i-1]) / 2;

        if (ts < s)
          le = me;
        else
          ri = me;
            
      }
      printf ("%lf\n", me);
    }
  }
  return 0;
}
