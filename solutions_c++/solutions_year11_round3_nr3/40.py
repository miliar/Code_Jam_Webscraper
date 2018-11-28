#include <cstdio>
#include <cstdlib>
int a[110];
int main()
{
   int T;
   scanf("%d",&T);
   while (T--)
   {
      int n,l,r;
      scanf("%d%d%d",&n,&l,&r);
      for (int i=1;i<=n;i++)
         scanf("%d",&a[i]);
      int ans=-1;
      for (int i=l;i<=r;i++)
      {
         bool flag=true;
         for (int j=1;j<=n;j++)
         {
            int x=a[j];
            if (x%i==0 || i%x==0)
               continue;
            flag=false;
            break;
         }
         if (flag)
         {
            ans=i;
            break;
         }
      }
      static int id=0;
      printf("Case #%d: ",++id);
      if (ans==-1)
         printf("NO\n");
      else
         printf("%d\n",ans);
   }
   return(0);
}
