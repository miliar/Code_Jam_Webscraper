#include <stdio.h>
#include <string.h>
#define maxn 10240

#define inf 0x3f3f3f3f

int min(int i,int j){return i<j?i:j;}

int s[maxn];
int c[maxn];
int dp[2][maxn];
int M,V;

void dfs(int i){
	int l,r;
	l=i+i; r=l+1;
	if (r<=M){
		dfs(l);
		dfs(r);
		// AND
		if (s[i]==1){
			dp[0][i]=min(dp[0][i],dp[0][l]+dp[0][r]);
			dp[0][i]=min(dp[0][i],dp[0][l]+dp[1][r]);
			dp[0][i]=min(dp[0][i],dp[1][l]+dp[0][r]);
			dp[1][i]=min(dp[1][i],dp[1][l]+dp[1][r]);
			if (c[i]==1){
				// OR
				dp[0][i]=min(dp[0][i],dp[0][l]+dp[0][r]+1);
				dp[1][i]=min(dp[1][i],dp[1][l]+dp[0][r]+1);
				dp[1][i]=min(dp[1][i],dp[0][l]+dp[1][r]+1);
				dp[1][i]=min(dp[1][i],dp[1][l]+dp[1][r]+1);
			}
		}else{
			// OR
			dp[0][i]=min(dp[0][i],dp[0][l]+dp[0][r]);
			dp[1][i]=min(dp[1][i],dp[0][l]+dp[1][r]);
			dp[1][i]=min(dp[1][i],dp[1][l]+dp[0][r]);
			dp[1][i]=min(dp[1][i],dp[1][l]+dp[1][r]);
			if (c[i]==1){
				// AND
				dp[0][i]=min(dp[0][i],dp[0][l]+dp[0][r]+1);
				dp[0][i]=min(dp[0][i],dp[1][l]+dp[0][r]+1);
				dp[0][i]=min(dp[0][i],dp[0][l]+dp[1][r]+1);
				dp[1][i]=min(dp[1][i],dp[1][l]+dp[1][r]+1);
			}		
		}
	}else dp[s[i]][i]=0;
//	printf("dp[0][%d]= %d dp[1][%d]=%d\n",i,dp[0][i],i,dp[1][i]);
}

void solve(int cas){
	int i,m;
	scanf("%d%d",&M,&V);
	memset(dp,0x3f,sizeof(dp));
	m=M/2;
	for (i=1;i<=m;i++) scanf("%d%d",s+i,c+i);
	for (i=m+1;i<=M;i++) scanf("%d",s+i);
	dfs(1);
	if (dp[V][1]>M) printf("Case #%d: IMPOSSIBLE\n",cas);
	else printf("Case #%d: %d\n",cas,dp[V][1]);
}

int main(){
	int t,cas;
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		solve(cas);
	return 0;
}

