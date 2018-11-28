# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <ctype.h>
# include <math.h>
# include <algorithm>
# define mx(a,b)(a>b?a:b)
# define mn(a,b)(a<b?a:b)

using namespace std;



int a[10200],b[10200];

int main()
{
   int i,j,k,l,m,n,r,s,t,u,v,test;
   freopen("A1.in","r",stdin);
   freopen("A1.out","w",stdout);


   scanf("%d",&test);

   for(k=1;k<=test;k++)
   {
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            scanf("%d%d",&a[i],&b[i]);
        }

        t = 0;
        for(i = 1;i <= n;i++)
         for(j = 1;j <= n;j++)
         {
             if(i == j)continue;
             if(a[i] < a[j] && b[i] > b[j] )
             ++t;
         }

         printf("Case #%d: %d\n",k,t);

   }
   return 0;
}
