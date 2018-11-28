#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

const int	MAXN	=	12;
const int	MAXS	=	(1 << 6);
const int	BIGNUM	=	10000;

char	map[MAXN][MAXN];
int		F[MAXN][MAXN][MAXS][MAXS], s[MAXN];
int		T, R, C, Limit;

void Init ()
{
	scanf ("%d%d%d", &R, &C, &Limit);
	for (int i = 0; i < R; ++i)
	{
		scanf ("%s", map[i]);
		s[i] = 0;
		for (int j = 0; j < C; ++j)
			if (map[i][j] == '#') s[i] += (1 << j);
	}

	memset (F, -1, sizeof (F));
}

int bit (int S, int p)
{
	return ((S >> p) & 1);
}

int dfs (int x, int y, int S0, int S1)
{
	if (x == R - 1) return 0;

	if (F[x][y][S0][S1] != -1) return F[x][y][S0][S1];
	F[x][y][S0][S1] = BIGNUM;

	for (int i = y; i >= 0; --i)
	{
		if (i > 0 && bit (S0, i - 1) == 0 && bit (S1, i - 1) == 1) 
			F[x][y][S0][S1] <?= dfs (x, i, S0, S1 - (1 << (i - 1))) + 1;
		if (i < C - 1 && bit (S0, i + 1) == 0 && bit (S1, i + 1) == 1) 
			F[x][y][S0][S1] <?= dfs (x, i, S0, S1 - (1 << (i + 1))) + 1;

		if (i == 0 || bit (S0, i - 1) == 1 || bit (S1, i - 1) == 0)
			break;
	}
	for (int i = y; i < C; ++i)
	{
		if (i > 0 && bit (S0, i - 1) == 0 && bit (S1, i - 1) == 1) 
			F[x][y][S0][S1] <?= dfs (x, i, S0, S1 - (1 << (i - 1))) + 1;
		if (i < C - 1 && bit (S0, i + 1) == 0 && bit (S1, i + 1) == 1) 
			F[x][y][S0][S1] <?= dfs (x, i, S0, S1 - (1 << (i + 1))) + 1;

		if (i == C - 1 || bit (S0, i + 1) == 1 || bit (S1, i + 1) == 0)
			break;
	}

	for (int i = y - 1; i >= 0; --i)
	{
		if ((S0 >> i) & 1) break;
		if ((S1 >> i) & 1) continue;

		int cur = x + 1;
		while (cur + 1 < R && bit (s[cur + 1], i) == 0) cur ++;

		if (cur - x > Limit) break;

		if (cur == x + 1)
			F[x][y][S0][S1] <?= dfs (cur, i, S1, s[cur + 1]);
		else
			F[x][y][S0][S1] <?= dfs (cur, i, s[cur], s[cur + 1]);

		break;
	}

	for (int i = y + 1; i < C; ++i)
	{
		if ((S0 >> i) & 1) break;
		if ((S1 >> i) & 1) continue;

		int cur = x + 1;
		while (cur + 1 < R && bit (s[cur + 1], i) == 0) cur ++;

		if (cur - x > Limit) break;

		if (cur == x + 1)
			F[x][y][S0][S1] <?= dfs (cur, i, S1, s[cur + 1]);
		else
			F[x][y][S0][S1] <?= dfs (cur, i, s[cur], s[cur + 1]);

		break;
	}

	return F[x][y][S0][S1];
}

int main ()
{
	freopen ("in.txt", "r", stdin);
	freopen ("ou.txt", "w", stdout);
	
	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		Init ();
		printf ("Case #%d: ", i);

		int tmp = dfs (0, 0, s[0], s[1]);
		if (tmp == BIGNUM)
			printf ("No\n");
		else
			printf ("Yes %d\n", tmp);
	}

	return 0;
}
