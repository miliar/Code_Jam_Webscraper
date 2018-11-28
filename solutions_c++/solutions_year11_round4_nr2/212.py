#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
using namespace std;
const double eps=1e-8;
struct point
{
   double x,y;
   point(double x=0,double y=0):x(x),y(y){}
};
point operator +(point a,point b)
{
   return(point(a.x+b.x,a.y+b.y));
}
point operator -(point a,point b)
{
   return(point(a.x-b.x,a.y-b.y));
}
point operator *(double a,point b)
{
   return(point(a*b.x,a*b.y));
}
int a[20][20];
int main()
{
   int T;
   scanf("%d",&T);
   while (T--)
   {
      int n,m;
      scanf("%d%d%*d",&n,&m);
      for (int i=1;i<=n;i++)
         for (int j=1;j<=m;j++)
         {
            char ch;
            cin>>ch;
            a[i][j]=ch-'0';
         }
      int ans=-1;
      for (int i=n;i>=3;i--)
         for (int j=1;j<=n-i+1;j++)
            for (int k=1;k<=n-i+1;k++)
            {
               point center(j+i/2.0-0.5,k+i/2.0-0.5),sum(0,0);
               for (int p=0;p<i;p++)
                  for (int q=0;q<i;q++)
                  {
                     if (!p && !q || !p && q==i-1 || p==i-1 && !q || p==i-1 && q==i-1)
                        continue;
                     int x=j+p,y=k+q;
                     sum=sum+a[x][y]*(point(x,y)-center);
                  }
               if (fabs(sum.x)<eps && fabs(sum.y)<eps)
               {
                  ans=i;
                  goto last;
               }
            }
last:
      static int id=0;
      printf("Case #%d: ",++id);
      if (ans==-1)
         printf("IMPOSSIBLE\n");
      else
         printf("%d\n",ans);
   }
   return(0);
}
