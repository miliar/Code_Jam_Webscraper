#include <cstdio>
#include <cstdlib>
#include <utility>
#include <algorithm>
using namespace std;
pair <int,int> a[1010];
int main()
{
   int T;
   scanf("%d",&T);
   while (T--)
   {
      int len,s,r,n;
      double t;
      scanf("%d%d%d%lf%d",&len,&s,&r,&t,&n);
      for (int i=1;i<=n;i++)
      {
         int l,r,x;
         scanf("%d%d%d",&l,&r,&x);
         a[i]=make_pair(x,r-l);
         len-=r-l;
      }
      a[++n]=make_pair(0,len);
      sort(a+1,a+n+1);
      double ans=0;
      for (int i=1;i<=n;i++)
      {
         double now=double(a[i].second)/(r+a[i].first);
         now=min(now,t);
         ans+=now+(a[i].second-(r+a[i].first)*now)/(s+a[i].first);
         t-=now;
      }
      static int id=0;
      printf("Case #%d: %.10f\n",++id,ans);
   }
   return(0);
}
