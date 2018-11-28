#include <cstdio>
#include <cstring>

const int MAXN = 200;
int T, N, M;
int data[MAXN][MAXN], dp[MAXN][MAXN], color[MAXN][MAXN];
int pool;

int dx[] = {-1, 0, 0, 1}, dy[] = {0, -1, 1, 0};

int DP(int x, int y)
{
	if (dp[x][y] == -1)
	{
		int I = -1, best = 999999999;
		for (int i = 0; i < 4; i++)
		{
			int X = x+dx[i], Y = y+dy[i];
			if (data[X][Y] < data[x][y] && data[X][Y] < best)
			{
				best = data[X][Y];
				I = i;
			}
		}
		if (I == -1)
			dp[x][y] = ++pool;
		else
			dp[x][y] = DP(x+dx[I], y+dy[I]);
	}
	return dp[x][y];
}

int main()
{
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d%d", &N, &M);
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= M; j++)
				scanf("%d", &data[i][j]);
		for (int i = 0; i <= N; i++)
			data[i][0] = data[i][M+1] = 999999999;
		for (int i = 0; i <= M; i++)
			data[0][i] = data[N+1][i] = 999999999;

		memset(dp, -1, sizeof dp);
		memset(color, -1, sizeof color);
		pool = -1;
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= M; j++)
				DP(i, j);
		pool = -1;
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= M; j++)
				if (color[i][j] == -1)
				{
					++pool;
					for (int k = 1; k <= N; k++)
						for (int l = 1; l <= M; l++)
							if (dp[k][l] == dp[i][j])
								color[k][l] = pool;
				}
		printf("Case #%d:\n", t);
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= M; j++)
				printf("%c%c", 'a'+color[i][j], j == M ? '\n' : ' ');
	}
}
