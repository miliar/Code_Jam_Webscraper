#include"iostream"

using namespace std;

char well[20]="welcome to code jam";
char ch[510];
int dp[510][20];
int n;


int main()
{
//	freopen("small","r",stdin);
//	freopen("small","w",stdout);
	scanf("%d",&n);
	int k;
	getchar();
	for(k=1;k<=n;k++)
	{
		gets(ch);
		memset(dp,0,sizeof(dp));
		int len=strlen(ch);
		int i,j;
		for(i=len-1;i>=0;i--)
		{
			for(j=18;j>=0;j--)
			{
				if(ch[i]==well[j])
				{
					if(j==18)
						++dp[i][j];
					dp[i][j]=(dp[i][j]+dp[i+1][j]+dp[i+1][j+1])%10000;
				}
				else
				{
					dp[i][j]=dp[i+1][j];
				}
			}
		}
		printf("Case #%d: %04d\n",k,dp[0][0]);
	}
	return 0;
}