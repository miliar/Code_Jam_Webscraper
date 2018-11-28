#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

const int Mod = 10000;
string W = "welcome to code jam";

char s[1024];
int dp[1024][20];

int main()
{
	freopen("f:\\C-small-attempt0.in", "r", stdin);
	freopen("f:\\C-small.out", "w", stdout);
	int T, t_case = 1;
	scanf("%d", &T);
	gets(s);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		gets(s + 1);
		int L = strlen(s + 1);
		memset(dp, 0, sizeof(dp));

		int res = 0;
		for (int i = 1; i <= L; i++)
		{
			for (int j = 0; j <= 18; j++)
			{
				if (j == 0)
				{
					if (W[j] == s[i])
						dp[i][j] = (dp[i][j] + 1) % Mod;
				}
				else
				{
					if (W[j] == s[i])
					{
						for (int k = 0; k < i; k++)
							dp[i][j] = (dp[i][j] + dp[k][j - 1]) % Mod;
					}
				}
			}
		}

		for (int i = 1; i <= L; i++)
			res = (res + dp[i][18]) % Mod;
		if (res < 0) res += Mod;

		printf("Case #%d: %04d\n", t_case, res);
	}
	return 0;
}
