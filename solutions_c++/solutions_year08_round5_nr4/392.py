#include <stdio.h>
#include <string.h>

int main(){
	int tt; scanf("%d",&tt);
	for (int ti=1;ti<=tt;ti++){
		int n,m,r;
		scanf("%d%d%d",&n,&m,&r);
		bool a[n][m]; memset(a,0,sizeof(a));
		long long dp[n][m]; memset(dp,0,sizeof(dp));
		for (int i=0;i<r;i++){
			int x,y;
			scanf("%d%d",&x,&y);
			x--; y--;
			a[x][y]=true;
		}

		dp[0][0]=1;

		for (int i=0;i<n;i++){
			for (int j=0;j<m;j++){
				if (a[i][j])continue;
				dp[i][j] %= 10007;
				int x,y;

				x = i+1; y = j+2;
				if (x<n && y<m){
					dp[x][y] = (dp[x][y] + dp[i][j])%10007;
				}
				x = i+2; y = j+1;
				if (x<n && y<m){
					dp[x][y] = (dp[x][y] + dp[i][j])%10007;
				}


			}
		}
/*
		for (int i=0;i<n;i++){
			for (int j=0;j<m;j++)printf("%6lld ",dp[i][j]); puts("");
		}
*/
		printf("Case #%d: %lld\n",ti,dp[n-1][m-1]);
	}
	
	return 0;
}
