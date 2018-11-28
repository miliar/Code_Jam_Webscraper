#include<iostream>
using namespace std;

bool rec[110][110];
int dp[110][110];
int num;
int h, w, r;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	int id = 1;
	while (id <= n)
	{
		memset(rec, 0, sizeof(rec));
		memset(dp, 0, sizeof(dp));
		printf("Case #%d: ", id++);
		num = 0;
		scanf("%d %d %d", &h, &w, &r);
		while (r--)
		{
			int a, b;
			scanf("%d %d", &a, &b);
			rec[a][b] = 1;
		}
		int i, j;
		dp[1][1] = 1;
		for (i = 2; i <= h; i++)
			for (j = 2; j <= w; j++)
			{
				if (rec[i][j] == 1) continue;
				if (i - 1 >= 1 && j - 2 >= 1) dp[i][j] += dp[i - 1][j - 2];
				if (i - 2 >= 1 && j - 1 >= 1) dp[i][j] += dp[i - 2][j - 1];
				dp[i][j] %= 10007;
			}
		/*for (i = 1; i <= h; i++)
		{
			for (j = 1; j <= w; j++)
				printf("%d ", dp[i][j]);
			printf("\n");
		}*/
		printf("%d\n", dp[h][w]);
	}
	return 0;
}