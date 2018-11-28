#include<iostream>

using namespace std;

bool map[110][110];
int dp[110][110];
int num;
int h, w, r;

void DFS(int x, int y)
{
	if (map[x][y] == 1) return;
	if (x > h || y > w) return;
	if (x == h && y == w)
	{
		num++;
		if (num >= 10007) num -= 10007;
		return;
	}
	DFS(x + 1, y + 2);
	DFS(x + 2, y + 1);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	int id = 1;
	while (id <= n)
	{
		memset(map, 0, sizeof(map));
		memset(dp, 0, sizeof(dp));
		printf("Case #%d: ", id++);
		num = 0;
		scanf("%d %d %d", &h, &w, &r);
		while (r--)
		{
			int a, b;
			scanf("%d %d", &a, &b);
			map[a][b] = 1;
		}
		int i, j;
		dp[1][1] = 1;
		for (i = 2; i <= h; i++)
			for (j = 2; j <= w; j++)
			{
				if (map[i][j] == 1) continue;
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