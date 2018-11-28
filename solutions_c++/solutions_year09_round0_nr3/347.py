#include <cstdio>
#include <cstring>
#include <memory.h>

using namespace std;

const char key[20] = "welcome to code jam";
int dp[501][20];
char word[501];

int main()
{
	int t, ti;
	char buf[501];
	gets(buf);
	sscanf(buf, "%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		memset(dp, 0, sizeof(dp));
		gets(word);
		int i, j;
		int L = strlen(word);
		dp[0][0] = 1;
		for (i = 0;i < L;i++)
		{
			for (j = 0;j <= 19;j++)
			{
				if (key[j] && key[j] == word[i])
				{
					dp[i + 1][j + 1] += dp[i][j];
					dp[i + 1][j + 1] %= 10000;
				}
				dp[i + 1][j] += dp[i][j];
				dp[i + 1][j] %= 10000;
			}
		}
		printf("Case #%d: %04d\n", ti, dp[L][19]);
	}
	return 0;
}
