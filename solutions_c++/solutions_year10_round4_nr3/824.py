#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>

using namespace std;

const int Max = 101;
int n;
int a[Max][Max];
int b[Max][Max];

bool dead()
{
     for(int i = 1; i <= 100; i++)
     {
        for(int j = 1; j <= 100; j++)
        {
           if(a[i][j]) return(0);
        }
     }
     return(1);
}
     
int main()
{
freopen("C-small-attempt0.in","r",stdin);
freopen("E:/out.txt","w",stdout);
   int t,test = 0;
   scanf("%d",&t);
   while(t--)
   {
       scanf("%d",&n);
       memset(a,0,sizeof(a));
       memset(b,0,sizeof(b));
       for(int i = 1; i <= n; i++)
       {
           int x1,y1,x2,y2;
           scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
           for(int j = x1; j <= x2; j++)
           {
                for(int k = y1; k <= y2; k++)
                {
                     a[j][k] = 1;
                }
           }
       }
       for(int i =1; i<=100;i++)
          for(int j = 1;j <=100; j++)
             b[i][j] = a[i][j];
       int ans = 0;
       while(1)
       {
           if(dead()) break;
           ans ++;    
           for(int i = 1; i <= 100; i++)
           {
               for(int j = 1; j <= 100; j++)
               {
                    if(b[i][j])
                    {
                         if(!b[i][j-1] && !b[i-1][j]) a[i][j] = 0;
                    }
                    else if(b[i][j-1] && b[i-1][j]) a[i][j] = 1;
               }
           }
          for(int i =1; i<=100;i++)
          for(int j = 1;j <=100; j++)
             b[i][j] = a[i][j];
       }
       printf("Case #%d: %d\n",++test,ans);
   }
   return(0);
}
