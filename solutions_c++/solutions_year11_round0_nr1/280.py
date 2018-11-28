#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;
bool f[110];
int a[110],b[110],g[110];
int main()
{
   int T;
   scanf("%d",&T);
   while (T--)
   {
      int n;
      scanf("%d",&n);
      for (int i=1;i<=n;i++)
      {
         char op;
         cin>>op>>g[i];
         f[i]=op=='O';
      }
      int x,y,u,v;
      x=y=1,u=v=0;
      for (int i=1;i<=n;i++)
         if (f[i])
            a[++u]=g[i];
         else
            b[++v]=g[i];
      int p,q,ans=0;
      p=q=1;
      for (int i=1;i<=n;i++)
      {
         int step;
         if (f[i])
         {
            step=abs(a[p]-x)+1;
            x=a[p++];
            if (abs(b[q]-y)<=step)
               y=b[q];
            else if (y<b[q])
               y+=step;
            else
               y-=step;
         }
         else
         {
            step=abs(b[q]-y)+1;
            y=b[q++];
            if (abs(a[p]-x)<=step)
               x=a[p];
            else if (x<a[p])
               x+=step;
            else
               x-=step;
         }
         ans+=step;
      }
      static int id=0;
      printf("Case #%d: %d\n",++id,ans);
   }
   return(0);
}
