#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int INF = (1 << 29) - 1;

int N, S, p, score[105];
int dp[105][105];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("lowesy_B.out", "w", stdout);
	int _, cases = 1;
	scanf("%d", &_);
	while (_--)
	{
		scanf("%d%d%d", &N, &S, &p);
		for (int i = 0; i < N; i++)
			scanf("%d", &score[i]);
		//sort(score, score + N);
		bool end = false;
		for (int i = 0; i <= N; i++)
			for (int j = 0; j <= S; j++)
				dp[i][j] = 0;
		dp[0][0] = 0;
		for (int i = 0; i < N; i++)
		{
			int v = score[i] / 3, r = score[i] % 3;
			for (int s = 0; s <= S; s++)
			{
				dp[i + 1][s] = max(dp[i + 1][s], dp[i][s]);
				if (score[i] < p) continue;
				//dp[i + 1][s] = max(dp[i + 1][s], 0);
				if (v >= p) dp[i + 1][s] = max(dp[i + 1][s], dp[i][s] + 1);
				else if (r == 0 && v + 1 >= p && s < S) dp[i + 1][s + 1] = max(dp[i + 1][s + 1], dp[i][s] + 1);
				else if (r == 1 && v + 1 >= p) dp[i + 1][s] = max(dp[i + 1][s], dp[i][s] + 1);
				else if (r == 2)
				{
					if (v + 1 >= p) dp[i + 1][s] = max(dp[i + 1][s], dp[i][s] + 1);
					if (v + 2 >= p && s < S) dp[i + 1][s + 1] = max(dp[i + 1][s + 1], dp[i][s] + 1);
				}
			}
		}
		printf("Case #%d: %d\n", cases++, dp[N][S]);
	}
	return 0;
}