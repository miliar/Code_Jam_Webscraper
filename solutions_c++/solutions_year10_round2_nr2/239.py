#include <stdio.h>
#include <algorithm>
using namespace std;
const double eps=0.0000001;
struct ori{
       int x,v;
       };
ori a[1000];
int it,T,i,q,n,k,b,t,r,rd;
int main()
{
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
scanf("%d",&T);
for(it=1;it<=T;it++)
   {
   printf("Case #%d: ",it);
   scanf("%d %d %d %d",&n,&k,&b,&t);
   for(i=0;i<n;i++)
      scanf("%d",&a[i].x);
   for(i=0;i<n;i++)
      scanf("%d",&a[i].v);
   for(r=rd=q=0,i=n-1;i>=0;i--)
      {
      if( (b-a[i].x) <=t * a[i].v)
         r+=q,rd++;
      else
         q++;
      if(rd>=k) break;
      }
   if(rd<k)
      printf("IMPOSSIBLE\n");
   else
      printf("%d\n",r);
   }
return 0;
}
