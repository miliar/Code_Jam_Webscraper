#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;

const int	MAXN	=	100 + 10;
const int	dx[]	=	{-1, 0, 0, 1};
const int	dy[]	=	{0, -1, 1, 0};

int		h[MAXN][MAXN], father[MAXN * MAXN], lab[MAXN * MAXN];
int		T, N, M;

void Init ()
{
	scanf ("%d%d", &N, &M);
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j)
			scanf ("%d", h[i] + j);
}

int root (int x)
{
	if (father[x] == -1) return x; else
		return father[x] = root (father[x]);
}

void merge (int x0, int y0, int x1, int y1)
{
	int A = x0 * M + y0;
	int B = x1 * M + y1;

	father[A] = B;
}

int chk (int x, int y)
{
	return (x >= 0 && x < N && y >= 0 && y < M);
}

void Solve ()
{
	int nbasin = 0;

	memset (father, -1, sizeof (father));

	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j)
		{
			int ah = 1000000, ad;

			for (int d = 0; d < 4; ++d)
				if (chk (i + dx[d], j + dy[d]))
					if (h[i + dx[d]][j + dy[d]] < ah)
					{
						ah = h[i + dx[d]][j + dy[d]];
						ad = d;
					}
			
			if (ah < h[i][j])
				merge (i, j, i + dx[ad], j + dy[ad]);
		}
	
	//printf ("%d\n", nbasin);
	memset (lab, -1, sizeof (lab));

	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j)
			if (lab[root (i * M + j)] == -1)
				lab[root (i * M + j)] = nbasin ++;

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M - 1; ++j)
			printf ("%c ", 'a' + lab[root (i * M + j)]);

		printf ("%c\n", 'a' + lab[root (i * M + M - 1)]);
	}
}

int main()
{
	freopen ("in.txt", "r", stdin);
	freopen ("ou.txt", "w", stdout);

	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d:\n", i);
		Init ();
		Solve ();
	}

	return 0;
}
