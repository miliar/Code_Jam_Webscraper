#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

const int	MAXN	=	100 + 10;
const int	MAXK	=	25 + 5;

int		p[MAXN][MAXK];
int		G[MAXN][MAXN], match[MAXN], vst[MAXN];
int		T, N, K;

void Init ()
{
	scanf ("%d%d", &N, &K);
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < K; ++j)
			scanf ("%d", p[i] + j);
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
		{
			G[i][j] = 1;
			for (int k = 0; k < K; ++k)
				if (p[i][k] >= p[j][k]) G[i][j] = 0;
		}
}

int aug (int v)
{
	for (int u = 0; u < N; ++u)
		if (!vst[u] && G[v][u])
		{
			vst[u] = 1;
			if (match[u] == -1 || aug (match[u]))
			{
				match[u] = v;
				return 1;
			}
		}
	
	return 0;
}

void Solve ()
{
	int answer = N;

	memset (match, -1, sizeof (match));
	for (int i = 0; i < N; ++i)
	{
		memset (vst, 0, sizeof (vst));
		if (aug (i)) answer --;
	}

	printf ("%d\n", answer);
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
		Solve ();
	}

	return 0;
}
