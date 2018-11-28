#include <iostream>
#include <string>
#include <map>
using namespace std;

map<string,int> engine;
string tmp;
char str[110];
int query[1005],dp[1005][105];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("11.out","w",stdout);
	int nca,S,Q,i,j,k,ans,ca;
	scanf("%d",&nca);
	for(ca=1;ca<=nca;ca++)
	{
		memset(dp,-1,sizeof(dp));
		engine.clear();
		scanf("%d",&S);
		getchar();
		for(i=1;i<=S;i++)
		{
			gets(str);
			tmp = str;
			engine[tmp] = i;
		}
		scanf("%d",&Q);
		getchar();
		for(i=0;i<Q;i++)
		{
			gets(str);
			tmp = str;
			query[i] = engine[tmp];
		}
		
		for(i=1;i<=S;i++)
		{
			dp[0][i]=0;
			if(query[0]==i)
				dp[0][i]=-1;
		}

		for(i=1;i<Q;i++)
		{
			for(j=1;j<=S;j++)
			{
				if(dp[i-1][j]==-1)	continue;

				if(query[i]==j)
				{
					for(k=1;k<=S;k++)
					{
						if(k==j)	dp[i][k]=-1;
						else
						{
							if(dp[i][k]==-1 || dp[i][k]>dp[i-1][j]+1)
								dp[i][k] = dp[i-1][j]+1;
						}
					}
				}
				else
				{
					if(dp[i][j]==-1 || dp[i-1][j]<dp[i][j])
						dp[i][j] = dp[i-1][j];
				}
			}
		}

		ans = -1;
		for(i=1;i<=S;i++)
		{
			if(dp[Q-1][i]==-1)	continue;
			if(ans==-1 || dp[Q-1][i]<ans)
				ans = dp[Q-1][i];
		}

		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}