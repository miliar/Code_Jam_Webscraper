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

bool inter(int x1, int y1, int x2, int y2)
{
    if(x1 > x2 && y1 < y2) return(true);
    if(x1 < x2 && y1 > y2) return(true);
    return(false);
}
    
int main()
{
freopen("A-large.in","r",stdin);
freopen("E:/out.txt","w",stdout);
   int t,test = 0;
   scanf("%d",&t);
   while(t--)
   {
      int a[1010],b[1010],n;
      scanf("%d",&n);
      for(int i = 1;i <= n;i++) scanf("%d %d",&a[i],&b[i]);
      int ans = 0;
      for(int i = 1; i < n; i++)
      {
         for(int j = i+1; j <= n; j++)
         {
             if(inter(a[i],b[i],a[j],b[j])) ans++;
         }
      }
      printf("Case #%d: %d\n",++test, ans);
   }
   return(0);
}
