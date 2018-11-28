#include<iostream>
#include<cstring>
#define F(i,n) for( i = 1; i <= (int)n;i++)
#define FE(i,v) for( typeof((v).begin()) i = (v).begin(); i!= (v).end();i++)

using namespace std;

int m, n;
char w[]="welcome to code jam";
int dp[1000][25];
char a[1000];
int main()
{
	int i, j, k, t;
	int tt;
	scanf("%d\n",&tt);
	F(t,tt)
	{
		memset(dp,0,sizeof(dp));
		dp[0][0]=1;
		gets(a);
		for(i=0;a[i];i++) dp[i+1][0]=1;
		for(j=0;w[j];j++)
		{
			for(i=0;a[i];i++)
			{
				if(w[j]==a[i])
				{
					dp[i+1][j+1] = (dp[i][j] + dp[i][j+1])%10000;
				}
				else
				{
					dp[i+1][j+1] = dp[i][j+1];
				}
			}
		}
		printf("Case #%d: %04d\n",t,dp[i][j]);
	}
	return 0;
}
