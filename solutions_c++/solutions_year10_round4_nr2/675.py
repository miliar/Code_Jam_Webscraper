#include <stdio.h>
#include <algorithm>

const int inf = 1000000000 - 100000/2;

void solve()
{
	static int C[11][512], T[11][1024][11];
	int p;
	scanf("%d", &p);
	memset(C, sizeof(C), 0);
	memset(T, sizeof(T), 0);
	for (int i = 0; i < (1<<p); i++)
	{
		int m;
		scanf("%d", &m);
		m = p - m;
		for (int c = 0; c < m; c++)
			T[0][i][c] = inf;
		for (int c = m; c <= p; c++)
			T[0][i][c] = 0;
	}
	for (int h = 1; h <= p; h++)
	{
		int mi = 1 << (p - h);
		for (int i = 0; i < mi; i++)
		{
			scanf("%d", &C[h][i]);
			for (int c = 0; c <= p - h; c++)
				T[h][i][c] = std::min(
					std::min(inf, T[h - 1][2 * i][c] + T[h - 1][2 * i + 1][c]),
					std::min(inf, C[h][i] + T[h - 1][2 * i][c + 1] + T[h - 1][2 * i + 1][c + 1])
					);
		}
	}
	printf("%d\n", T[p][0][0]);
}

int main()
{
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}