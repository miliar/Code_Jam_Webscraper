#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
	int T,cnt=0;
	int N,S,p,t[105],dp[105][105];
	scanf("%d",&T);
	while(T--) {
		scanf("%d %d %d",&N,&S,&p);
		for(int i=1;i<=N;i++) scanf("%d",&t[i]);
		memset(dp,0,sizeof(dp));
		for(int i=1;i<=N;i++)
			for(int j=0;j<=S;j++)
				if (j>i) break;
				else 
				if (j==0 || t[i]<2 || t[i]>28) {
					if(t[i]%3==0) dp[i][j]=dp[i-1][j]+((t[i]/3>=p)?1:0);
					else dp[i][j]=dp[i-1][j]+((t[i]/3+1>=p)?1:0);
				}
				else {
					if(t[i]%3==0) {
						dp[i][j]=max(dp[i-1][j-1]+((t[i]/3+1>=p)?1:0), dp[i-1][j]+((t[i]/3>=p)?1:0));
					} else 
					if(t[i]%3==1) {
						dp[i][j]=max(dp[i-1][j-1]+((t[i]/3+1>=p)?1:0), dp[i-1][j]+((t[i]/3+1>=p)?1:0));
					} else
					if(t[i]%3==2) {
						dp[i][j]=max(dp[i-1][j-1]+((t[i]/3+2>=p)?1:0), dp[i-1][j]+((t[i]/3+1>=p)?1:0));
					}
				}
		printf("Case #%d: %d\n",++cnt, dp[N][S]);
	}
	return 0;
}
