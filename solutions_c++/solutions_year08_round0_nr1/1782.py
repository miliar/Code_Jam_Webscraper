#include <iostream>
#include <cstdio>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

map<string, int> engines;
int dp[1010][110];

int main()
{
	int N, S, Q, i, j, k, l;
	char tmp[110];
	string s;
	scanf("%d ", &N);
	//getchar();
	for (i = 1; i <= N; i++)
	{
		engines.clear();
		scanf("%d ", &S);
		//getchar();
		for (j = 1; j <= S; j++)
		{
			gets(tmp);
			s = tmp;
			engines[s] = j;
		}
		memset(dp, 0x7f, sizeof(dp));
		for (j = 1; j <= S; j++) dp[0][j] = 0;
		scanf("%d ", &Q);
		//getchar();
		for (j = 1; j <= Q; j++)
		{
			gets(tmp);
			s = tmp;
			int q = engines[s];
			for (k = 1; k <= S; k++)
			{
				for (l = 1; l <= S; l++)
				{
					if (l != q)
					{
						if (k == l)
							dp[j][k] = dp[j][k] > dp[j - 1][l] ? dp[j - 1][l] : dp[j][k];
						else
							dp[j][k] = dp[j][k] > dp[j - 1][l] + 1 ? dp[j - 1][l] + 1 : dp[j][k];
					}
				}
			}
		}
		int minValue = 999999999;
		for (j = 1; j <= S; j++)
			if (dp[Q][j] < minValue) minValue = dp[Q][j];
		printf("Case #%d: %d\n", i, minValue);
	}
	return 0;
}