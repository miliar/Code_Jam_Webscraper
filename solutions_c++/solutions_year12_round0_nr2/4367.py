#include <iostream>
#include<ctype.h>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<string>
#include<string.h>
#include<cstring>
#include<stack>
#include<queue>
#include<cassert>
#include<iterator>
#include<cmath>
using namespace std ;
int main()
{
   int test;
   scanf("%d",&test);
   int i;
   for(i=1;i<=test;i++)
   {
      int n,s,p;

      scanf("%d",&n);
      scanf("%d",&s);
      scanf("%d",&p);

      int j;
      int a;
      int ans=0;
      for(j=0;j<n;j++)
      {
         int x,y,z;
         scanf("%d",&a);
         x = a/3;
         y = (a-x)/2;
         z = a - x - y;
         int f1=0,f2=0;

         if( x>=p || y>=p || z>=p )
         {
            f1=1;
         }
         if( abs(x-y)>2 || abs(y-z)>2 || abs(z-x)>2 )
         {
            f2=1;
         }
         else
         {
            if( abs(x-y)==2 || abs(y-z)==2 || abs(z-x)==2 )
            {
               f2=2;
            }
         }

         if(f2==0)//less
         {
            if(f1==1)
                ans++;
            else
            {
               int X,Y,Z;
               X = p;
               Y = (a-p)/2;
               Z = a- X - Y;
               if(X>=0 && Y>=0 && Z>=0)
               {
                  if( abs(X-Y)<=2 && abs(Y-Z)<=2 && abs(Z-X)<=2 )
                  {
                     if(s>0)
                     {
                        s--;
                        ans++;
                     }
                  }
               }
            }
         }
         else if(f2==2)
         {
            if(f1==1)
            {
               if(s>0)
               {
                  s--;
                  ans++;
               }
            }
         }
         
      }
      printf("Case #%d: ",i);
      printf("%d\n",ans);

   }

	return 0;
}
