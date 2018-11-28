#include <stdio.h>
#include <algorithm>
using namespace std;
#define M 1000000
#define INF (1LL<<60)
typedef long long ll;

ll dp[M];

main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		ll l;
		int n;
		ll b[100];
		scanf("%lld%d",&l,&n);
		for(int i=0;i<n;i++)scanf("%lld",&b[i]);
		sort(b,b+n);
		for(int i=0;i<M;i++)dp[i]=INF;
		dp[0]=0;
		for(int i=0;i<n;i++){
			for(int j=0;j<M;j++)if(j>=b[i])dp[j]=min(dp[j],dp[j-b[i]]+1);
			//for(int j=0;j<100;j++)printf("%lld ",dp[j]);puts("");
		}
		ll m=M-1;
		for(;;m--){
			if((l-m)%b[n-1]==0)break;
		}
		printf("Case #%d: ",t);
		if(dp[m]==INF)printf("IMPOSSIBLE\n");
		else printf("%lld\n",dp[m]+(l-m)/b[n-1]);
	}
}