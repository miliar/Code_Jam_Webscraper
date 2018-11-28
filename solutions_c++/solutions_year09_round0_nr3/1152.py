#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>

#include <set>
#include <map>
#include <vector>
#include <string>

#include <algorithm>

using namespace std;


char s[550];
char p[100]="welcome to code jam";
int dp[550][100];
int const base = 10000;

void run()
{
	memset(dp,0,sizeof(dp));
	gets(s);
	int n = strlen(s);
	int m = strlen(p);
	dp[0][0]=1;
	for(int i=1; i<=n; i++)
	{
		dp[i][0]=1;
		for(int j=1; j<=m; j++)
		{
			dp[i][j]=dp[i-1][j];
			if(s[i-1]==p[j-1])
			{
				dp[i][j]+=dp[i-1][j-1];
				dp[i][j]%=base;
			}							
		}
	}
	printf("%04d",dp[n][m]);

}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int testCount;
	scanf("%d\n",&testCount);
	for(int testNumber=1; testNumber<=testCount; testNumber++)
	{
		printf("Case #%d: ",testNumber);
		run();
		printf("\n");
	}
	return 0;
}