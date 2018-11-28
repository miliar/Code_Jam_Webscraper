#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

char s[128];
int pos[128], dp[128];

int main()
{
	freopen("f:\\A-small-attempt0.in", "r", stdin);
	freopen("f:\\A-small-attempt0.out", "w", stdout);
	int T, N;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		scanf("%d", &N);
		for (int i = 1; i <= N; i++)
		{
			scanf("%s %d", s + i, &pos[i]);
		}

		int po = 1, pb = 1, to = 0, tb = 0;
		dp[0] = 0;
		for (int i = 1; i <= N; i++)
		{
			if (s[i] == 'O')
			{
				dp[i] = to + abs(po - pos[i]) + 1;
				po = pos[i];
			}
			else
			{
				dp[i] = tb + abs(pb - pos[i]) + 1;
				pb = pos[i];
			}
			if (dp[i - 1] + 1 > dp[i])
				dp[i] = dp[i - 1] + 1;
			if (s[i] == 'O') to = dp[i];
			else tb = dp[i];
		}
		printf("Case #%d: %d\n", t_case, dp[N]);
	}
	return 0;
}
