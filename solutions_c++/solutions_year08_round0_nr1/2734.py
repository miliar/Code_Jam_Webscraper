#include <cstdio>
#include <cstring>
#include <algorithm>

const int infty = 10000;

int s, q;
char S[20][200], temp[200];
int dp[20][200], Q[200];

int eq(char *str1, char *str2)
{
	int res = 0;
	for (int i = 0; str1[i] && str2[i]; i++)
	{
		if (str1[i] == str2[i])
			res+=5;
		else
			res--;
	}
	return res;
}

void solve(int testId)
{
	scanf("%d\n", &s);
	for (int i = 0; i < s; i++)
		gets(S[i]);
	scanf("%d\n", &q);
	for (int i = 0; i < q; i++)
	{
		Q[i] = -1;
		gets(temp);
		for (int j = 0; j < s; j++)
			if (strcmp(temp, S[j]) == 0)
				Q[i] = j;
		if (Q[i] == -1) while (1);		
	}

	for (int i = 0; i < s; i++)
		dp[i][0] = i != Q[0] ? 0 : infty;

	for (int j = 1; j < q; j++)
	{
		for (int i = 0; i < s; i++)
		{
			dp[i][j] = infty;
			if (Q[j] != i)
			{
				for (int k = 0; k < s; k++)
					dp[i][j] = std::min(dp[k][j-1] + (i != k ? 1 : 0), dp[i][j]);

			}
		}
	}

	int ans = infty;

	for (int i = 0; i < s; i++)
		ans = std::min(ans, dp[i][q-1]);

	printf("Case #%d: %d\n", testId, ans);
}

int main()
{
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d\n", &n);
	for (int t = 0; t < n; t++)
	{
		solve(t+1);
	}

	return 0;
}