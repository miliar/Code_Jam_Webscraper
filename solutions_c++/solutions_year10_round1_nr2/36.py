#include <stdio.h>
#include <string.h>

int dp[500][256]={0};
int v[500];

int main(void)
{
	int T, cs, D, I, M, N, i, j, k;
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++){
		scanf("%d%d%d%d",&D,&I,&M,&N);
		memset(dp,-1,sizeof(dp));
		for(i=1;i<=N;i++)
			scanf("%d",&v[i]);
		for(j=0;j<256;j++)
			dp[0][j] = 0;
		for(i=1;i<=N;i++){
			for(j=0;j<256;j++)
				dp[i][j] = dp[i-1][j] + D;
			for(j=0;j<256;j++){
				for(k=0;k<256;k++){
					if(j-k > M || k-j > M) continue;
					if(dp[i][j] > dp[i-1][k] + ((j<v[i])? (v[i]-j):(j-v[i])))
						dp[i][j] = dp[i-1][k] + ((j<v[i])? (v[i]-j):(j-v[i]));
				}
			}
			for(j=0;j<256;j++){
				for(k=j;k>=j-M && k>=0;k--)
					if(dp[i][j] > dp[i][k] + I)
						dp[i][j] = dp[i][k] + I;
			}
			for(j=255;j>=0;j--)
				for(k=j;k<=j+M && k<=255;k++)
					if(dp[i][j] > dp[i][k] + I)
						dp[i][j] = dp[i][k] + I;
		}
		int mc=dp[N][0];
		for(j=0;j<256;j++)
			if(dp[N][j] < mc)
				mc = dp[N][j];
		printf("Case #%d: %d\n",cs, mc);
	}
	return 0;
}
