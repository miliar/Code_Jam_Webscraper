#pragma comment(linker,"/STACK:100000000")  

#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;
int x[1010], y[1010], z[1010], p[1010];

int check(double R)
{
   int i, X, Y, Z;
   double P, j;
   double l0=-10000000, r0=10000000, l1=-10000000, r1=10000000, l2=-10000000, r2=10000000, l3=-10000000, r3=10000000;

   for (i=0; i<n; i++)
   {
      X=x[i], Y=y[i], Z=z[i], P=R*p[i];
      j=(X+Y+Z+P);
      if (r0>j) r0=j;
      j=(X+Y+Z-P);
      if (l0<j) l0=j;
      j=(X+Y-Z+P);
      if (r1>j) r1=j;
      j=(X+Y-Z-P);
      if (l1<j) l1=j;
      j=(X-Y+Z+P);
      if (r2>j) r2=j;
      j=(X-Y+Z-P);
      if (l2<j) l2=j;
      j=(-X+Y+Z+P);
      if (r3>j) r3=j;
      j=(-X+Y+Z-P);
      if (l3<j) l3=j;
      if (l0>r0 || l1>r1 || l2>r2 || l3>r3) return 0;
   }
   if (l1+l2+l3>r0 || r1+r2+r3<l0) return 0;
   return 1;
}

int main(void)
{
   int i;
   freopen("C-small-attempt3.in", "r", stdin);
   freopen("C-small-attempt3.out", "w", stdout);
   //freopen("C-large.in", "r", stdin);
   //freopen("C-large.out", "w", stdout);

   scanf("%d\n", &nt);
   double l, r;
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d:\n", tn+1);
      scanf("%d\n", &n);
      for (i=0; i<n; i++)
         scanf("%d%d%d%d", &x[i], &y[i], &z[i], &p[i]);

      l=0.00000001, r=l;
      while (!check(r)) r*=2;
      while (r-l>1e-9)
      {
         if (check((l+r)*0.5))
            r=(l+r)*0.5;
         else 
            l=(l+r)*0.5;
      }

      printf("Case #%d: ", tn+1);
      printf("%.6lf\n", r);
   }
   return 0;
}
