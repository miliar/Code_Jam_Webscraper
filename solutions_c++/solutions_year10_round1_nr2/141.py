#include<stdio.h>
#define min(x,y) ((x)<(y)?(x):(y))
#define max(x,y) ((x)>(y)?(x):(y))
#define abs(x) ((x)<0?(-(x)):(x))
int t;

int dp[105][250];
int a[101];
int D,I,M,n;

int main()
{
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		scanf("%d%d%d%d",&D,&I,&M,&n);
		for(int i=1;i<=n;i++)
			scanf("%d",&a[i]);
		for(int i=0;i<256;i++)
			dp[0][i]=0;
		for(int i=1;i<=n;i++){
			for(int j=0;j<256;j++){
				for(int k=0;k<256;k++)
					dp[i][j]=dp[i-1][j]+D;
				for(int k=0;k<256;k++){
					int dist=abs(k-j);
					int ineed;
					ineed=100000;
					if(M!=0)ineed=(dist-1)/M;
					else{
						if(dist!=0)continue;
						else ineed=0;
					}
					if(ineed<0)ineed=0;
					int cost=dp[i-1][k]+I*ineed+abs(a[i]-j);
					dp[i][j]=min(dp[i][j],cost);
				}
			}
		}
		int ans=100000;
		for(int i=0;i<=n;i++)
			for(int j=0;j<256;j++)
				ans=min(ans,dp[i][j]+(n-i)*D);
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
