//Welcome to Code Jam

#include<iostream>
using namespace std;

const int MAX = 550;
const char wel[] = " welcome to code jam";

char szIn[MAX];
int lcs[20][MAX];
int dp[20][MAX];



void Solve(int no)
{
	gets(szIn+1);
	int len = strlen(szIn+1);
	int i, j;
	memset(lcs, 0, sizeof(lcs));
	for(i=0; i<=len; ++i)dp[0][i] = 1;
	for(i=1; i<=19; ++i)
	{
		for(j=1; j<=len; ++j)
		{
			dp[i][j] = dp[i][j-1];
			if(szIn[j] == wel[i])
			{
				lcs[i][j] = max(lcs[i][j], lcs[i-1][j-1]+1);
				if(lcs[i][j] == i)
				{
					dp[i][j] += dp[i-1][j-1];
					dp[i][j] %= 10000;
				}
			}
			else lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1]);
		}
	}
	printf("Case #%d: %04d\n", no, dp[19][len]);
}

int main()
{
	int n, i;
	scanf("%d", &n);
	getchar();
	for(i=1; i<=n; ++i)
	{
//		getchar();
		Solve(i);
	}
	return 0;
}
