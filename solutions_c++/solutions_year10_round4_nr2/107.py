#include <stdio.h>
#include <string.h>

int n, N;

int M[4096];

int c[4096];

int dp[4096][15], large=1000000000;

int dfs(int lev,int x, int r){

	if(lev == n){
		if(r <= M[x])
			return 0;
		else
			return large;
	}
	if(dp[x][r] != -1)
		return dp[x][r];
	int yescst = dfs(lev+1, x*2, r) + dfs(lev+1, x*2+1, r) + c[x];
	int nocst = dfs(lev+1, x*2, r+1) + dfs(lev+1, x*2+1, r+1);
	if(yescst < nocst)
		dp[x][r] = yescst;
	else
		dp[x][r] = nocst;
	
	if(dp[x][r] > large) dp[x][r] = large;
	if(dp[x][r] < 0) fprintf(stderr,"ALERM!\n");
	//fprintf(stderr,"%d %d %d => %d\n", lev, x,r, dp[x][r]);
	return dp[x][r];
}

int main(void)
{
	int cs, T, i, j;
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++){
		scanf("%d",&n);
		N = (1<<n);
		for(i=0;i<N;i++)
			scanf("%d",&M[N+i]);
		for(i=n-1;i>=0;i--)
			for(j=0;j<(1<<i);j++)
				scanf("%d",&c[ (1<<i) + j ]);
		memset(dp, -1, sizeof(dp));
		int ans = dfs(0, 1, 0);
		printf("Case #%d: %d\n", cs, ans);
		fprintf(stderr,"Case #%d: %d\n", cs, ans);
	}
	return 0;
}
