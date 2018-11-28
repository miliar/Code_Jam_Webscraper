#include <stdio.h>
#include <algorithm>
const double eps = 1e-9;
struct ori {
int a, b;
bool operator<(const ori &A) const {return (a<A.a) || (a == A.a && b < A.b);}
};
ori mas[1000];
int ii,t,c,d,i,j;
double st,fin,k,mini,mn,mxx;
int main()
{
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
scanf("%d",&t);
for(ii=1;ii<=t;ii++)
   {
   printf("Case #%d: ",ii);
   scanf("%d %d",&c,&d);
   for(i=0;i<c;i++)
      scanf("%d %d",&mas[i].a, &mas[i].b);
   std::sort(mas, mas+c);
   st = 0.;
   fin = 1000000000000.;
   for(i=0;i<2000;i++)
      {
      k = (st+fin)/2;
      mini = mas[0].a - k - d;
      bool ind = 0;
      for(j=0;j<c;j++)
         {
         mn = mas[j].a - k;
         mxx = mas[j].a + k;
         mini += d;
         if(mini < mn) mini = mn;
         mini += (mas[j].b - 1.) * d;
         if(mini > mxx + eps)
            {
            ind = 1;
            break;
            }
         }
      if(!ind)
         fin = k;
      else
         st = k;
      }
   printf("%.9lf\n",fin);
   }
return 0;
}
