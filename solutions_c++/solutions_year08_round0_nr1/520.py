#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

map <string , int> mp;
char ch[128];
int dp[1002][102];
int main()
{
	int T, i, j, n, m, S, Q, id, t = 1, k;
	string name;
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	while (T --)
	{
		mp.clear();
		memset(dp, -1, sizeof(dp));

		scanf("%d", &S);
		getchar();
		for (i = 0; i < S; i ++)
		{
			gets(ch);
			name = ch;
			mp[name] = i+1;
		}
		scanf("%d", &Q);
		getchar();
		for (i = 0; i < Q; i ++)
		{
			gets(ch);
			name = ch;
			id = mp[name];
			if (i == 0)
			{
				for (j = 1; j <= S; j ++)
				{
					if (id == j)
						continue;
					dp[i][j] = 0;
				}
			}
			else
			{
				for (j = 1; j <= S; j ++)
				{
					if (id == j)
						continue;
					for (k = 1; k <= S; k ++)
					{
						if (dp[i-1][k] != -1)
						{
							if (j == k)
							{
								if (dp[i][j] == -1 || dp[i][j] > dp[i-1][k])
									dp[i][j] = dp[i-1][k];
							}
							else
							{
								if (dp[i][j] == -1 || dp[i][j] > dp[i-1][k] + 1)
									dp[i][j] = dp[i-1][k] + 1;
							}
						}
					}
				}
			}
		}
		int ans = -1;
		if (Q == 0)
			ans = 0;
		else
		{
			for (i = 1; i <= S; i ++)
			{
				if (dp[Q-1][i] != -1)
				{
					if (ans == -1 || ans > dp[Q-1][i])
						ans = dp[Q-1][i];
				}
			}
		}
		printf("Case #%d: %d\n", t ++, ans);
	}
	return 0;
}