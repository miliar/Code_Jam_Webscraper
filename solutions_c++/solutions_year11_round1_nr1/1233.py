#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
const double eps=1e-8;
using namespace std;
int main()
{
   int T;
   scanf("%d",&T);
   while (T--)
   {
      int n,d,g;
      scanf("%d%d%d",&n,&d,&g);
      static int id=0;
      printf("Case #%d: ",++id);
      if (g==100 && d<100 || d>0 && g==0)
         printf("Broken\n");
      else
      {
         bool flag=false;
         n=min(n,100);
         for (int i=1;i<=n;i++)
         {
            double x=i*d/100.0;
            if (fabs(x-int(x))<eps)
            {
               flag=true;
               break;
            }
         }
         printf("%s\n",flag?"Possible":"Broken");
      }
   }
   return(0);
}
