#include <stdio.h>
#include <math.h>
int it,t,i,n;
int x[1000],y[1000],r[1000];
double rd;
double rad(int x0,int y0,int r0,int x1,int y1,int r1)
{
return (sqrt((x1-x0)*(x1-x0)+(y1-y0)*(y1-y0)+0.)+r0+r1)/2.;
}
int main()
{
freopen("D-small.in","r",stdin);
freopen("D-small.out","w",stdout);
scanf("%d",&t);
for(it=1;it<=t;it++)
   {
   printf("Case #%d: ",it);
   scanf("%d",&n);
   for(i=0;i<n;i++)
      scanf("%d %d %d",&x[i],&y[i],&r[i]);
   if(n==1)
      printf("%.9f\n",r[0]+0.);
   else
      if(n==2)
         printf("%.9f\n",(r[0]>?r[1])+0.);
      else
         {
         rd=rad(x[0],y[0],r[0],x[1],y[1],r[1])>?r[2];
         rd<?=rad(x[0],y[0],r[0],x[2],y[2],r[2])>?r[1];
         rd<?=rad(x[1],y[1],r[1],x[2],y[2],r[2])>?r[0];
         printf("%.9f\n",rd);
         }
   }
return 0;
}
