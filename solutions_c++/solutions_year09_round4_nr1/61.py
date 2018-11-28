#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

const int	MAXN	=	40 + 5;
const int	BIGNUM	=	10000;

char	line[MAXN];
int		G[MAXN][MAXN], lx[MAXN], ly[MAXN], match[MAXN], vx[MAXN], vy[MAXN], last[MAXN];
int		T, N;

int abs (int x) { return x >= 0 ? x : -x; }

int aug (int v)
{
	vx[v] = 1;

	for (int u = 0; u < N; ++u)
		if (!vy[u] && G[v][u] == lx[v] + ly[u])
		{
			vy[u] = 1;
			if (match[u] == -1 || aug (match[u]))
			{
				match[u] = v;
				return 1;
			}
		}
	
	return 0;
}

void KM ()
{
	memset (lx, 0, sizeof (lx));
	memset (ly, 0, sizeof (ly));

	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
			lx[i] >?= G[i][j];

	memset (match, -1, sizeof (match));

	for (int k = 0; k < N; ++k)
		while (1)
		{
			memset (vx, 0, sizeof (vx));
			memset (vy, 0, sizeof (vy));
			if (aug (k)) break;

			int delta = BIGNUM;
			for (int i = 0; i < N; ++i) if (vx[i])
			for (int j = 0; j < N; ++j) if (!vy[j])
				delta <?= lx[i] + ly[j] - G[i][j];

			for (int i = 0; i < N; ++i) if (vx[i]) lx[i] -= delta;
			for (int i = 0; i < N; ++i) if (vy[i]) ly[i] += delta;
		}
	
	int ans = 0;
	for (int i = 0; i < N; ++i) ans += lx[i];
	for (int i = 0; i < N; ++i) ans += ly[i];
	printf ("%d\n", N * BIGNUM - ans);

	for (int i = 0; i < N; ++i)
		printf ("%d ", match[i]);
	printf ("\n");
}

void Init ()
{
	scanf ("%d", &N);
	for (int i = 0; i < N; ++i)
	{
		scanf ("%s", line);
		last[i] = 0;
		for (int j = 0; j < N; ++j)
			if (line[j] == '1') last[i] = j;

		for (int j = 0; j < last[i]; ++j)
			G[i][j] = 0;
		for (int j = last[i]; j < N; ++j)
			G[i][j] = BIGNUM - abs (i - j);

		//printf ("%d ", last[i]);
	}
	//printf ("\n");
}

void Greedy ()
{
	int used[MAXN], ans = 0;
	memset (used, 0, sizeof (used));
	for (int i = 0; i < N; ++i)
		for (int j = i; j < N; ++j)
			if (last[j] <= i)
			{
				ans += j - i;
				for (int k = j; k > i; --k)
					last[k] = last[k - 1];
				break;
			}
	
	printf ("%d\n", ans);
}

int main ()
{
	freopen ("in.txt", "r", stdin);
	freopen ("ou.txt", "w", stdout);

	scanf ("%d", &T);
	for (int test = 1; test <= T; ++test)
	{
		Init ();

		printf ("Case #%d: ", test);
		//KM ();
		Greedy ();
	}

	return 0;
}
