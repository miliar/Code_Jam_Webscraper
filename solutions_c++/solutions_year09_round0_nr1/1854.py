#include <iostream>
#include <string>
#include <string.h>
#include <cstring>

using namespace std;

char c[]="welcome to code jam";
char tek[501];
int dp[505][20];
int n;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d\n",&n);

	int t,i,j,k;

	for (t=1; t<=n; t++)
	{
		gets(tek);
		int m=strlen(tek);

		memset(dp,0,sizeof(dp));

		if (tek[0]==c[0]) dp[0][0]=1;

		for (i=1; i<m; i++)
		{
			for (j=0; j<19; j++)
				dp[i][j]=dp[i-1][j];

			if (tek[i]==c[0]) dp[i][0]++;

			for (j=1; j<19; j++)
				if (tek[i]==c[j])
				{
					dp[i][j]+=dp[i-1][j-1];
					dp[i][j]%=10000;
				}
		}

		printf("Case #%d: %d%d%d%d\n",t,dp[m-1][18]/1000,(dp[m-1][18]/100)%10,(dp[m-1][18]/10)%10,dp[m-1][18]%10);
	}

	return 0;
}