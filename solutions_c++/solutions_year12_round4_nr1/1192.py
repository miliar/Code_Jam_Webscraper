#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int d[10010], l[10010];
int n,D;
int dp[10010];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		scanf("%d",&n);
		for(int i=0;i<n;++i){
			scanf("%d%d",&d[i],&l[i]);
		}
		scanf("%d",&D);
		memset(dp,0,sizeof dp);
		dp[0] = d[0];
		for(int i=0;i<n-1;++i){
			int r = dp[i];
			for(int j=i+1;j<n && d[j] - d[i] <= r;++j){
				int rr = min(d[j] - d[i], l[j]);
				dp[j] = max(dp[j],rr);
			}
		}
		bool reachable = false;
		for(int i=0;i<n;++i)
			if(d[i] + dp[i] >= D){
				reachable = true;
				break;
			}
		if(reachable) printf("Case #%d: YES\n",t);
		else printf("Case #%d: NO\n",t);
	}
}
