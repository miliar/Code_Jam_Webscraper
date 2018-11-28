#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

#include <map>
#include <ctime>
#include <queue>
#include <algorithm>
#define MAXN 2049
#define INFINITE 0x3f3f3f3f
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int P, n;
int M[MAXN * 2 + 1];
int v[MAXN + 1];
void Init()
{
	scanf("%d", &P);
	n = 1 << P;
	for (int i = n + n - 1; i >= n; i --)
		scanf("%d", &M[i]);
	for (int i = n - 1; i >= 1; i --)
		scanf("%d", &v[i]);
}

int f[MAXN * 2 + 1][MAXN + 1];
int g[MAXN * 2 + 1];
void Solve(int id)
{
	memset(f, 0x3f, sizeof(f));
	for (int i = n; i <= n + n - 1; i ++)
		for (int j = 0; j <= M[i]; j ++)
			f[i][j] = 0, g[i] = M[i];
	for (int i = n - 1; i >= 1; i --)
	{
		int lc = i << 1, rc = lc + 1;
		g[i] = MIN(g[lc], g[rc]);
		for (int j = 0; j <= g[i]; j ++)
		{
			f[i][j] = f[lc][j] + f[rc][j] + v[i];
			if (j < g[i])
				f[i][j] = MIN(f[i][j], f[lc][j + 1] + f[rc][j + 1]);
		}
	}
	int ans = INFINITE;
	for (int i = 0; i <= g[1]; i ++)
		ans = MIN(ans, f[1][i]);
	printf("Case #%d: %d\n", id, ans);
}

int main()
{
	freopen("worldcup.in", "r", stdin);
	freopen("worldcup.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i ++)
	{
		Init();
		Solve(i);
	}
	return 0;
}
