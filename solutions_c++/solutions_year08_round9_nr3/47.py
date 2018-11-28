#include <iostream>

using namespace std;

const int dirx[9] = {-1, -1, -1, 0, 0, 0, 1, 1, 1};
const int diry[9] = {-1, 0, 1, -1, 0, 1, -1, 0, 1};

int	N, M;
int	value, answer;
int	a[10][10];

int task, now;

bool	DFS(int x, int y)
{
	if (y == M)
	{
		++x;
		y = 0;
	}
	if (x > N / 2 && value <= answer) return 0;
	if (x == N)
	{
		answer = max(answer, value);
		return 0;
	}

	bool canGo = 1;
	if (x && y && a[x - 1][y - 1]) canGo = 0;
	if (x && y == M - 1 && a[x - 1][y]) canGo = 0;

	if (x == N - 1 && y && a[x][y - 1]) canGo = 0;
	if (x == N - 1 && y == M - 1 && a[x][y]) canGo = 0;
	if (canGo) DFS(x, y + 1);

	canGo = 1;
	for (int i = 0; canGo && i < 9; ++i) 
	{
		int u = x + dirx[i];
		int v = y + diry[i];
		if (u < N && u >= 0 && v < M && v >= 0 && !a[u][v]) canGo = 0;
	}
	if (canGo)
	{
		for (int i = 0; i < 9; ++i) 
		{
			int u = x + dirx[i];
			int v = y + diry[i];
			if (u < N && u >= 0 && v < M && v >= 0) a[u][v] -= 1;
		}

		if (x == N / 2) ++value;
		DFS(x, y + 1);
		if (x == N / 2) --value;

		for (int i = 0; i < 9; ++i) 
		{
			int u = x + dirx[i];
			int v = y + diry[i];
			if (u < N && u >= 0 && v < M && v >= 0) a[u][v] += 1;
		}
	}
}

int	main()
{
	scanf("%d", &task);

	for (int now = 1; now <= task; ++now)
	{
		scanf("%d%d", &N, &M);
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
				scanf("%d", &a[i][j]);

		value = 0;
		answer = 0;
		DFS(0, 0);
		printf("Case #%d: %d\n", now, answer);
	}
	return 0;
}
