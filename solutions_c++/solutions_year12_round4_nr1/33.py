#include <cstdio>
#include <algorithm>
#define MAXN 10050

using namespace std;

const short infshort=MAXN+1;
const int infint=1000000050;

int n,dist;
int px[MAXN],len[MAXN];
short dp[MAXN];

inline bool solve() {
   px[0]=0;
   px[n+1]=dist;
   //len[n+1]=infint;
   for(short i=1;i<=n+1;i++)
      dp[i]=infshort;
   dp[1]=0;
   for(short i=1;i<=n;i++) {
      if(dp[i]==infshort) continue;
      int fx=min(2*px[i]-px[dp[i]],px[i]+len[i]);
      for(short j=i+1;j<=n+1&&px[j]<=fx;j++)
         /*if(px[j]-len[j]<=px[i]) */dp[j]=min(dp[j],i);
   }
   return dp[n+1]<infshort;
}

int main(void)
{
   int t,cas=1;
   scanf("%d",&t);
   while(t--) {
      scanf("%d",&n);
      for(int i=1;i<=n;i++)
         scanf("%d %d",px+i,len+i);
      scanf("%d",&dist);
      printf("Case #%d: %s\n",cas++,solve()?"YES":"NO");
   }
   return 0;
}
