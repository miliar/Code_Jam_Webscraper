#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;
#define PI 3.14159265358979323846264338327950288
#define sqr(x) ((x) * (x))

const double eps = 1e-8;

struct cir
{
   double x, y, r;
}a[45];


double xs1, ys1, xs2, ys2;
int yes[10000][45];
vector < cir > P;
int N;

void init()
{
   scanf("%d", &N);
   for (int k = 0; k < N; ++ k)
     scanf("%lf%lf%lf", &a[k].x, &a[k].y, &a[k].r);
}

bool same(double x, double y)
{
    return fabs(x - y) < eps;
}

int solve(double x1, double y1, double r1, double x2, double y2, double r2)
{
   if (same(x1, x2) && same(y1, y2) && same(r1, r2)) return 0;
   double d=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
   if(d > r1 + r2|| d < fabs(r1 - r2)) return 0;
   if(eps > fabs(d - r1 - r2) || eps > fabs(d - fabs(r1 - r2))){
     double a=2.0*r1*(x1-x2);
     double b=2.0*r1*(y1-y2);
     double c=r2*r2-r1*r1-(x1-x2)*(x1-x2)-(y1-y2)*(y1-y2);
     double p=a*a+b*b;
     double q=-2.0*a*c;
     double c1=-q/p/2.0;
     double s1=sqrt(1-c1*c1);
     xs1=r1*c1+x1;
     ys1=r1*s1+y1;
     if(eps <fabs((xs1-x2)*(xs1-x2)+(ys1-y2)*(ys1-y2)-r2*r2)) ys1=-r1*s1+y1;
     return 1;
    }else{
     double a = 2.0*r1*(x1-x2);
     double b = 2.0*r1*(y1-y2);
     double c = r2*r2-r1*r1-(x1-x2)*(x1-x2)-(y1-y2)*(y1-y2);
     double p = a*a+b*b;
     double q = -2.0*a*c;
     double r=c*c-b*b;
     double tmp = q * q - 4.0 * p * r;
     if (fabs(tmp) < eps) tmp = 0.0;
     double c1=(sqrt(tmp)-q)/p/2.0;
     double c2=(-sqrt(tmp)-q)/p/2.0;
     double s1=sqrt(1-c1*c1);
     double s2=sqrt(1-c2*c2);
     xs1=r1*c1+x1;
     xs2=r1*c2+x1;
     ys1=r1*s1+y1;
     ys2=r1*s2+y1;
     if(eps<fabs((xs1-x2)*(xs1-x2)+(ys1-y2)*(ys1-y2)-r2*r2)){
      ys1=-r1*s1+y1;
     }if(eps<fabs((xs2-x2)*(xs2-x2)+(ys2-y2)*(ys2-y2)-r2*r2)){
      ys2=-r1*s2+y1;
     }if(eps>fabs(ys1-ys2)&&eps>fabs(xs1-xs2)){
      if(ys1>y1){
       ys2=2.0*y1-ys1;
      }else{
       ys1=2.0*y1-ys1;
      }
     }
     return 2;
    }
  return 0;
}

void work()
{
     if (N == 1)
     {
         printf("%lf\n", a[0].r);
         return;
     }
     if (N == 2)
     {
         printf("%lf\n", max(a[0].r, a[1].r));
         return;
     }
     double res = 100000000.0;
     for (int i = 0; i < N; ++ i)
       for (int j = i + 1; j < N; ++ j)
         {
             double l = max(a[i].r, a[j].r);
             double r = 100000.0;
             while (l + 1e-6 < r)
             {
                double mid = (l + r) / 2.0;
                if (solve(a[i].x, a[i].y, mid - a[i].r, a[j].x, a[j].y, mid - a[j].r)) r = mid; else l = mid;
             }
             l = (l + r) / 2.0;
             double t = max(l, a[3 - i - j].r);
             if (t < res) res = t;
         }
      printf("%lf\n", res);
}

int main()
{
    //freopen("D.in", "r", stdin);
       int caseNo;
       scanf("%d", &caseNo);
       for (int T = 1; T <= caseNo; ++ T)
       {
           printf("Case #%d: ", T);
           init();
           work();
       }
    return 0;
}

