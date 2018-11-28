#include <cstdio>
#include <cstdlib>
int main()
{
   int T;
   scanf("%d",&T);
   while (T--)
   {
      int n;
      scanf("%d",&n);
      int ans=0;
      for (int i=1;i<=n;i++)
      {
         int x;
         scanf("%d",&x);
         ans+=x!=i;
      }
      static int id=0;
      printf("Case #%d: %d.000000\n",++id,ans);
   }
   return(0);
}
