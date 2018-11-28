#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int MAXN = 55;

int T = 1, C, N, K, right [MAXN];
char grid [MAXN][MAXN], ngrid [MAXN][MAXN];

inline bool valid (int i, int j, char colo)
{
	return i >= 0 && j >= 0 && i < N && j < N && grid [i][j] == colo;;
}

inline int maxrun (int i, int j, char colo)
{
	int best = 1, cur = 0;

	for (int k = 0; k < K; k++)
		if (valid (i, j + k, colo))
			cur++;
		else
			break;
	best = max (best, cur);
	cur = 0;

	for (int k = 0; k < K; k++)
		if (valid (i, j - k, colo))
			cur++;
		else
			break;
	best = max (best, cur);
	cur = 0;

	for (int k = 0; k < K; k++)
		if (valid (i + k, j, colo))
			cur++;
		else
			break;
	best = max (best, cur);
	cur = 0;
	
	for (int k = 0; k < K; k++)
		if (valid (i - k, j, colo))
			cur++;
		else
			break;
	best = max (best, cur);
	cur = 0;

	for (int k = 0; k < K; k++)
		if (valid (i + k, j + k, colo))
			cur++;
		else
			break;
	best = max (best, cur);
	cur = 0;

	for (int k = 0; k < K; k++)
		if (valid (i - k, j - k, colo))
			cur++;
		else
			break;
	best = max (best, cur);
	cur = 0;

	for (int k = 0; k < K; k++)
		if (valid (i - k, j + k, colo))
			cur++;
		else
			break;
	best = max (best, cur);
	cur = 0;

	for (int k = 0; k < K; k++)
		if (valid (i + k, j - k, colo))
			cur++;
		else
			break;
	best = max (best, cur);

	return best;
}

int main ()
{
	for (scanf ("%d", &C); T <= C; T++)
	{
		int maxR = 0, maxB = 0;
		memset (grid, 0, sizeof (grid));
		memset (ngrid, 0, sizeof (ngrid));
		scanf ("%d %d", &N, &K);

		for (int i = 0; i < N; i++)
			scanf ("%s", &ngrid [i]);

		for (int i = 0; i < N; i++)
		{
			int loc = N - 1;

			for (int j = N - 1; j >= 0; j--)
				if (ngrid [i][j] != '.')
					grid [i][loc--] = ngrid [i][j];

			for (int j = 0; j < N; j++)
				if (grid [i][j] == 'B' || grid [i][j] == 'R')
					break;
				else
					grid [i][j] = '.';
		}

		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
			{
				if (grid [i][j] == 'B')
					maxB = max (maxB, maxrun (i, j, 'B'));
				else if (grid [i][j] == 'R')
					maxR = max (maxR, maxrun (i, j, 'R'));
			}

		if (max (maxB, maxR) >= K)
			printf ("Case #%d: %s\n", T, ((maxB > maxR && maxR < K) ? "Blue" : ((min (maxB, maxR) >= K) ? "Both" : "Red")));
		else
			printf ("Case #%d: Neither\n", T);
	}
	return 0;
}
