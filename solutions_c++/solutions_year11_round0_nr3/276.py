#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int main()
{
   int T;
   scanf("%d",&T);
   while (T--)
   {
      int n,m=0,value=1<<30,sum=0;
      scanf("%d",&n);
      for (int i=1;i<=n;i++)
      {
         int x;
         scanf("%d",&x);
         m^=x;
         sum+=x;
         value=min(value,x);
      }
      static int id=0;
      printf("Case #%d: ",++id);
      if (!m)
         printf("%d\n",sum-value);
      else
         printf("NO\n");
   }
   return(0);
}
