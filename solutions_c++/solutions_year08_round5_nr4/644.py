#include <cstdio>

int dp[110][110];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int q,k,i,j,R,r,c,W,H;
	scanf("%d",&q);
	for(k=1;k<=q;k++){
		for(i=0;i<110;i++)
			for(j=0;j<110;j++)
				dp[i][j]=0;
		dp[0][0]=1;
		scanf("%d%d%d",&H,&W,&R);
		for(i=0;i<R;i++){
			scanf("%d%d",&r,&c);
			dp[r-1][c-1]=-1;
		}
		for(i=1;i<H;i++)
			for(j=1;j<W;j++)
				if((dp[i][j]!=-1)){
					if(i!=1)if(dp[i-2][j-1]!=-1)dp[i][j]+=dp[i-2][j-1];
					if(j!=1)if(dp[i-1][j-2]!=-1)dp[i][j]+=dp[i-1][j-2];
					dp[i][j]=dp[i][j]%10007;
				}
		printf("Case #%d: %d",k,dp[H-1][W-1]);
		printf("\n");
	}
	return 0;
}


//compiled with Visual Studio 2005
