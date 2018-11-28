#include <stdio.h>
#include <iostream>
using namespace std;
struct ori{
          double sic;
          double zoma;
          bool operator<(const ori &a) const { return sic < a.sic; }
};
ori a[2000000];
int T,x,s,r,t,n,i,sul;
int b[2000000],e[2000000],w[2000000];
double dro,tt;
int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
scanf("%d",&T);
for(int it=1;it<=T;it++)
   {
   printf("Case #%d: ",it);
   scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
   for(i=0;i<n;i++)
      scanf("%d %d %d",&b[i],&e[i],&w[i]);
   sul = x;
   for(i=0;i<n;i++)
      sul -= e[i] - b[i];
   for(i=0;i<n;i++)
      a[i].zoma = e[i] - b[i],
      a[i].sic = w[i] + s;
   a[n].zoma = sul;
   a[n].sic = s;
   n++;
   sort(a, a+n);
   tt = t;
   dro = 0.;
   for(i=0;i<n;i++)
      {
      if( (a[i].sic + r - s) * tt > a[i].zoma)
         {
         dro += a[i].zoma / (a[i].sic + r - s);
         tt  -= a[i].zoma / (a[i].sic + r - s);
         }
      else
         {
         dro += tt;
         a[i].zoma -= (a[i].sic + r - s) * tt;
         tt = 0.;
         dro += 1. * a[i].zoma / a[i].sic;
         }
      }
   printf("%.9lf\n",dro);
   }
return 0;
}
