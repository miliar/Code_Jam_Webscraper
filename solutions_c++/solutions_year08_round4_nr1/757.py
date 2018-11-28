#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
typedef unsigned long long LL;
const int maxn=10010;

int n1,n2,m,v;
int val[maxn],gat[maxn],cable[maxn];
int tval[maxn],tgat[maxn];
int dp[maxn][2];
bool vis[maxn][2];

int main()
{
	int t,cas;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++)
	{
		scanf("%d%d",&m,&v);
		n1=(m-1)/2;
		n2=(m+1)/2;
		memset(val,0,sizeof(val));
		memset(gat,0,sizeof(gat));
		memset(cable,0,sizeof(cable));
		for(int i=1;i<=n1;i++)
		{
			scanf("%d%d",&gat[i],&cable[i]);
		}
		for(int i=1;i<=n2;i++)
		{
			scanf("%d",&val[i+n1]);
		}
		memset(dp,0,sizeof(dp));
		memset(vis,0,sizeof(vis));
		for(int i=1;i<=n1;i++)dp[i][0]=dp[i][1]=1<<29;
	    for(int i=1;i<=n2;i++)
			vis[i+n1][ val[i+n1] ]=1;
		for(int i=n1;i;i--)
		{
			for(int j=0;j<2;j++)if(vis[i*2][j])
			{
				for(int k=0;k<2;k++)if(vis[i*2+1][k])
				{
					if(gat[i]==1){dp[i][j&k]=min(dp[i][j&k],dp[i*2][j]+dp[i*2+1][k]);vis[i][j&k]=1;}
					if(gat[i]==0){dp[i][j|k]=min(dp[i][j|k],dp[i*2][j]+dp[i*2+1][k]);vis[i][j|k]=1;}
					
					if(cable[i])
					{
						if(gat[i]==1)dp[i][j|k]=min(dp[i][j|k],dp[i*2][j]+dp[i*2+1][k]+1);vis[i][j|k]=1;
						if(gat[i]==0)dp[i][j&k]=min(dp[i][j&k],dp[i*2][j]+dp[i*2+1][k]+1);vis[i][j&k]=1;
					}
				}
			}
		}
		if(dp[1][v]!=1<<29)printf("Case #%d: %d\n",cas,dp[1][v]);
		else printf("Case #%d: IMPOSSIBLE\n",cas);
	}
	return 0;
}
