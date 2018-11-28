#include <cstdio>
#include <algorithm>
#define INF (1<<29)
using namespace std;

int c,n,m,q[2805],p[2805],dp[2805][15];

void dfs(int x){
	int t;

	for (int i=0;i<=n;i++) dp[x][i]=INF;

	if (x*2>=m){
		t=max(p[x*2],p[x*2+1]);
		dp[x][t]=0;
		if (t>0) dp[x][t-1]=q[x];
	}
	else{
		dfs(x*2);
		dfs(x*2+1);
		for (int i=0;i<=n;i++)
		    for (int j=0;j<=n;j++){
				t=max(i,j);
				dp[x][t]=min(dp[x][t],dp[x*2][i]+dp[x*2+1][j]);
				if (t>0) dp[x][t-1]=min(dp[x][t-1],dp[x*2][i]+dp[x*2+1][j]+q[x]);
			}
	}
}

int main(){
	scanf("%d",&c);
	for (int tc=1;tc<=c;tc++){
		scanf("%d",&n);
		m=(1<<(n));
		
		for (int i=m+m-1;i>=m;i--) scanf("%d",&p[i]),p[i]=n-p[i];
		
		for (int i=m-1;i>=1;i--) scanf("%d",&q[i]);
		
		dfs(1);
		printf("Case #%d: %d\n",tc,dp[1][0]);
		
	}
	return 0;
}
