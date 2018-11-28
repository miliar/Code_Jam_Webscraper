#include <vector>
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
#include <list>

using namespace std;

typedef struct node{
        int x;
        int v;
        int t;
        };

node a[60];
int n,K,B,T;

bool cmp1(node x, node y)
{
   if(x.t == y.t) return(x.x > y.x);
   else return(x.t < y.t);
}

bool cmp2(node x, node y)
{
   return(x.x < y.x);
}

int alltime(node y)
{
   int d1 = B - y.x;
   int t1;
   if(d1 % y.v == 0) 
     t1 = d1 / y.v;
   else t1 = d1 / y.v + 1;
   return(t1);
}

bool reach(node y)
{
   return(alltime(y) <= T);
}

int main()
{
freopen("B-large.in","r",stdin);
freopen("E:/out.txt","w",stdout);
   int t,test = 0;
   scanf("%d",&t);
   while(t--)
   {
      scanf("%d%d%d%d",&n,&K,&B,&T);
      printf("Case #%d: ",++test);
      for(int i = 1;i <= n; i++) scanf("%d",&a[i].x);
      for(int i = 1; i <= n; i++) scanf("%d",&a[i].v);
      for(int i = 1; i <= n; i++) a[i].t = alltime(a[i]);        
      sort(a+1,a+1+n,cmp1);
      if(K > 0) if(!reach(a[K]))
      {
         printf("IMPOSSIBLE\n");
         continue;
      }
      if(!K)
      {
         printf("0\n");
         continue;
      }
      sort(a+1,a+1+n,cmp2);
      int cur_num = 0;
      int ans = 0;
      for(int i = n; i > 0; i--)
      {
         if(reach(a[i]))
         {
            for(int j = i+1; j <= n; j++)
            {
               if(!reach(a[j])) ans ++;
            }
            cur_num ++;
            if(cur_num == K) break;
         }
      }
      printf("%d\n",ans);
   }
   return(0);
}
  
