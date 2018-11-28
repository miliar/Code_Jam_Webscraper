#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define ll long long

int tn, nt, n, m;

double x[10005], y[10005];

double get(double X, double Y)
{
  double r0=hypot(X-x[0], Y-y[0]);
  double r1=hypot(X-x[1], Y-y[1]);
  double d=hypot(x[0]-x[1], y[0]-y[1]);
  double c0=(r0*r0+d*d-r1*r1)/(2*r0*d);
  double c1=(r1*r1+d*d-r0*r0)/(2*r1*d);
  if (c0<=-1) c0=-1.0;
  if (c0>=1) c0=1.0;
  if (c1<=-1) c1=-1.0;
  if (c1>=1) c1=1.0;
  c0=2*acos(c0);
  c1=2*acos(c1);
  double s0=0.5*r0*r0*(c0-sin(c0));
  double s1=0.5*r1*r1*(c1-sin(c1));

  return s0+s1;
}

int main(void)
{
   freopen("D-small-attempt0.in", "r", stdin);
   freopen("D-small-attempt0.out", "w", stdout);
   //freopen("D-large.in", "r", stdin);
   //freopen("D-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      //fprintf(stderr, "Case #%d: \n", tn+1);

      scanf("%d%d", &n, &m);
      for (int i=0; i<n+m; i++)
        scanf("%lf%lf", &x[i], &y[i]);

      printf("Case #%d:", tn+1);

      for (int i=n; i<n+m; i++)
        printf(" %.10lf", get(x[i], y[i]));

      printf("\n");
   }
   return 0;
}
