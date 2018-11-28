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

int tn, nt;

double F(double x)
{
   if (x<0.0) x=0.0;
   if (x>1.0) x=1.0;
   return sqrt(1-x*x);
}

double f(double x)
{
   if (x<0.0) x=0.0;
   if (x>1.0) x=1.0;
   return 0.5*(asin(x)+x*sqrt(1-x*x));
}

double integr(double l, double r)
{
   return f(r)-f(l);
}

double integr2(double l, double r, double y1, double y2, double g, double L)
{
   if (r<=y1) return (r-l)*g;
   if (l>=y2) return 0.0;
   double res=0.0;
   if (l<=y1) res=(y1-l)*g, l=y1;
   if (r>=y2) r=y2;
   return res+integr(l, r)-L*(r-l);
}

double get2(double g, double r)
{
   double l=0.0, res=0.0, nl, y1, y2, L, NL;
   int i, j;
   if (g<=0.0) return 1.0;
   for (i=0; l<1.0; i++, l=nl)
   {
      if (i%2==0)
      {
         if (i==0) nl=l+r;
         else nl=l+r+r;
         if (nl>1.0) nl=1.0;
         res+=integr(l, nl);
      }
      else
      {
         nl=l+g;
         if (nl>1.0) nl=1.0;
         y2=F(l);
         y1=F(nl);
         L=0.0;
         for (j=0; L<y2; j++, L=NL)
         {
            if (j%2==0)
            {
               if (j==0) NL=L+r;
               else NL=L+r+r;
               res+=integr2(L, NL, y1, y2, nl-l, l);
            }
            else NL=L+g;
         }
      }
   }
   return res*4/3.1415926535897932384626433832795;
}

double get(double g, double r, double t)
{
   if (t>=1.0) return 1.0;
   double p=(1-t)*(1-t);
   return p*get2(g/(1-t), r/(1-t))+1-p;
}

int main(void)
{
   double f, R, t, r, g;
   //freopen("C-small-attempt0.in", "r", stdin);
   //freopen("C-small-attempt0.out", "w", stdout);
   freopen("C-large.in", "r", stdin);
   freopen("C-large.out", "w", stdout);
   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {      
      scanf("%lf%lf%lf%lf%lf\n", &f, &R, &t, &r, &g);

      g-=2*f;
      r+=f;
      t+=f;
      g/=R;
      r/=R;
      t/=R;
      
      printf("Case #%d: ", tn+1);
      printf("%.6lf\n", get(g, r, t));
   }
   return 0;
}
