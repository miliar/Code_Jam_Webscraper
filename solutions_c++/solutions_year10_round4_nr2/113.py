#include <stdio.h>
#include <string.h>
#include <algorithm>

int N, size;
int M[2048], cost[2048];

int opt[2048][11];
bool cached[2048][11];

int solve(int x, int y)
{
	if (cached[x][y]) 
		return opt[x][y];
	cached[x][y] = true;

	if (x >= size)
		return opt[x][y] = (y >= M[x] ? 0 : 1000000000);
	
	opt[x][y] = std::min( opt[x][y], solve(x * 2, y) + solve(x * 2 + 1, y) );
	opt[x][y] = std::min( opt[x][y], solve(x * 2, y + 1) + solve(x * 2 + 1, y + 1) + cost[x] );

	return opt[x][y];
}

int main()
{
//	freopen("B.in", "r", stdin);

	int C;

	scanf("%d", &C);
	for (int cas = 0; cas < C; ++cas)
	{
		scanf("%d", &N); size = 1 << N;

		memset(M, 0, sizeof(M));
		memset(cost, 0, sizeof(cost));
		for (int i = 0; i < size; ++i) 
		{
			scanf("%d", &M[size + i]);
			M[size + i] = N - M[size + i];
		}
		for (int i = N - 1; i >= 0; --i)
			for (int j = 0; j < (1 << i); ++j)
				scanf("%d", &cost[(1 << i) + j]);

		for (int i = 0; i < size * 2; ++i)
			for (int j = 0; j <= N; ++j)
			{
				opt[i][j] = 1000000000;
				cached[i][j] = false;
			}
		printf("Case #%d: %d\n", cas + 1, solve(1, 0));
	}

	return 0;
}

