#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int dp[1100][110];

int main()
{
	int T;
	int Ti=0;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		Ti++;
		int S,Q;
		map<string,int> mS;
		map<string,int> mQ;
		int q[1100];
		int cS=0,cQ=0;
		scanf("%d\n",&S);
		for(int i=0;i<S;i++)
		{
			char tstr[1000];
			gets(tstr);
			mS[tstr]=cS++;
		}
		scanf("%d\n",&Q);
		for(int i=0;i<Q;i++)
		{
			char tstr[1000];
			gets(tstr);
			//mQ[tstr]=cQ++;
			q[i]=mS[tstr];
		}

		memset(dp,0,sizeof(dp));
		for(int j=0;j<S;j++)
			if(q[0]==j)
				dp[0][j]=1<<30;
			else
				dp[0][j]=0;
		for(int i=1;i<Q;i++)
		{
			for(int j=0;j<S;j++)
				if(q[i]!=j)	
				{
					dp[i][j]=dp[i-1][j];
					for(int k=0;k<S;k++) if(j-k)
					{
						if(q[i]!=j)
							dp[i][j]=min(dp[i][j],dp[i-1][k]+1);
					}
				}
				else
					dp[i][j]=1<<30;
			
		}

		int minn=1<<30;
		for(int i=0;i<S;i++)
			if(dp[Q-1][i]>=0)
				minn=min(dp[Q-1][i],minn);
		
		printf("Case #%d: %d\n",Ti,minn);
	}

}