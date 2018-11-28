#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

#define mset(a,x) memset(a,x,sizeof(a))
typedef long long i64;
const int INF=100000000;
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define ABS(a) ((a) >= 0 ? (a) : -(a))
template <class T>void dbgarr(const T* a,int n){for(int i=0;i<n;i++)cerr<<a[i]<<" ";cerr<<endl;}
#define dbg(x) cerr<<#x<<" : "x<<endl

int dp[10005][2];
int G[10005];
int C[10005];
int M,V;

void init(){
	mset(dp,-1);
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    int T,kcase(0);
	scanf("%d",&T);
	while(T--){
		init();
		scanf("%d%d",&M,&V);
		for(int i=1;i<=(M-1)/2;i++){
			scanf("%d%d",&G[i],&C[i]);
		}
		for(int i=(M-1)/2+1;i<=M;i++){
			int t;
			scanf("%d",&t);
			dp[i][t]=0;
			dp[i][1-t]=INF;
		}
		for(int i=(M-1)/2;i>=1;i--){
			dp[i][0]=dp[i][1]=INF;
			if(G[i]==1){
				dp[i][0]<?=dp[i*2][0]+dp[i*2+1][0];
				dp[i][0]<?=dp[i*2][0]+dp[i*2+1][1];
				dp[i][0]<?=dp[i*2][1]+dp[i*2+1][0];
				dp[i][1]<?=dp[i*2][1]+dp[i*2+1][1];
			}
			else {
				dp[i][0]<?=dp[i*2][0]+dp[i*2+1][0];
				dp[i][1]<?=dp[i*2][1]+dp[i*2+1][1];
				dp[i][1]<?=dp[i*2][0]+dp[i*2+1][1];
				dp[i][1]<?=dp[i*2][1]+dp[i*2+1][0];
			}
			if(C[i]){
				if(G[i]==0){
					dp[i][0]<?=dp[i*2][0]+dp[i*2+1][0]+1;
					dp[i][0]<?=dp[i*2][0]+dp[i*2+1][1]+1;
					dp[i][0]<?=dp[i*2][1]+dp[i*2+1][0]+1;
					dp[i][1]<?=dp[i*2][1]+dp[i*2+1][1]+1;
				}
				else {
					dp[i][0]<?=dp[i*2][0]+dp[i*2+1][0]+1;
					dp[i][1]<?=dp[i*2][1]+dp[i*2+1][1]+1;
					dp[i][1]<?=dp[i*2][0]+dp[i*2+1][1]+1;
					dp[i][1]<?=dp[i*2][1]+dp[i*2+1][0]+1;
				}
			}
		}
		if(dp[1][V]<INF)printf("Case #%d: %d\n",++kcase,dp[1][V]);
		else printf("Case #%d: IMPOSSIBLE\n",++kcase);
	}
}
