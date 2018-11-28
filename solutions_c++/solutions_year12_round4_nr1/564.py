#include <cstdio>
#include <algorithm>
#define INF 2000000002;
using namespace std;
int dis[10001];
int len[10001];
int DP[10001];
int n;
int main(){
  int t,D;
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    scanf("%d",&n);
    for(int i=0;i<n;i++){
      scanf("%d %d",&dis[i], &len[i]);
    }
    scanf("%d",&D);
    for(int i=n-1;i>=0;i--){
      DP[i]=INF;
      if(D-dis[i]<=len[i]){
        DP[i]=D-dis[i];
      }
      for(int j=i+1;j<=n;j++){
        //if(dis[j]-dis[i]>len[j]) continue;
        if(dis[j]-dis[i]>len[i]){
          break;
        }
        int prop=min(dis[j]-dis[i],len[j]);
        if(DP[j]<=prop){
          DP[i]=min(DP[i],dis[j]-dis[i]);
        }
      }
    }
    if(dis[0]>=DP[0]) printf("Case #%d: YES\n",tt);
    else printf("Case #%d: NO\n",tt);
   // for(int i=0;i<n;i++){ printf("\n dp[%d]=%d",i,DP[i]);}
  }
  return 0;
}



