#include <cstdio>
#include <queue>
using namespace std;

queue <int> a;
int x,R,N,K,k,t,i;
long long sum,ans,rag;
int main()
{
   freopen("file.in","r",stdin);
   freopen("file.out","w",stdout);
   scanf("%d",&t);
   for(i=0;i<t;i++)
   {
   while (!a.empty()) a.pop();
   scanf("%d%d%d",&R,&K,&N);
   rag=0;
   for(k=0;k<N;k++)
   {
      scanf("%d",&x);
      a.push(x);
      rag+=(long long)x;
   }
   if (rag<K) printf("Case #%d: %lld\n",i+1,rag*R); else
   {
   ans=0;
   for(k=0;k<R;k++)
   {
      sum=0;
      while (sum<=K)
      if (sum+a.front()<=K)
      {
         sum+=(long long)a.front();
         x=a.front();
         a.pop();
         a.push(x);
      } else break;
      ans+=(long long)sum;
   }
   printf("Case #%d: %lld\n",i+1,ans);
  }
  }
}
