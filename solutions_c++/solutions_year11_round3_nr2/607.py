#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int dp[1005][5];
int main()
{
	freopen("d:\\data\\B-small-attempt1.in","r",stdin);
	freopen("d:\\data\\B-small-attempt1.out","w",stdout);
	int T,C=0,i,j,k;
	int l,t,n,c,a[1005],s[1005];
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d%d",&l,&t,&n,&c);
		for(i=0;i<c;i++)
			scanf("%d",&a[i]);
		for(i=0;i<=l;i++)
			dp[0][i]=0;
		for(i=1;i<=n;i++)
		{
			s[i]=a[(i-1)%c];
			dp[i][0]=dp[i-1][0]+s[i]*2;
		}
		int x,y;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=l;j++)
			{
				dp[i][j]=dp[i-1][j]+s[i]*2;
				if(dp[i-1][j-1]+s[i]*2>=t)
				{
					x=0;
					if(t>=dp[i-1][j-1])
						x=t-dp[i-1][j-1];
					y=x+(s[i]-x/2);
					dp[i][j]=min(dp[i][j],dp[i-1][j-1]+y);
				}
				//dp[i][j]=dp[i-1][j]+s[i]*2;
				//if(dp[i-1][j-1]+s[i]>=t&&dp[i-1][j-1]<=t)
				//	dp[i][j]=min(dp[i][j],dp[i-1][j-1]+(x=t-dp[i-1][j-1])*2+(s[i]-x));
				//printf("%d %d %d %d %d %d\n",i,j,s[i],t,dp[i-1][j-1],dp[i][j]);
			}
		}
		printf("Case #%d: ",++C);
		int ans=-1u>>1;
		for(i=0;i<=l;i++)
			ans=min(ans,dp[n][i]);
		printf("%d\n",ans);
	}
}
