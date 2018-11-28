#include <cstdio>
#include <algorithm>

using namespace std;

#define AND 1
#define OR 0

const int inf = 99999999;

int n, v;
int d[10001][2];
int c[10001];
int g[10001];

void solve(int v)
{
	if(v > n / 2) return;
    solve(v * 2);
	solve(v * 2 + 1);
    int i, j;
	int and, or;
	for(i = 0; i <= 1; ++i)
		for(j = 0; j <= 1; ++j)
		{
            and = or = 0;
			if(i + j == 2) and = 1;
			if(i + j >= 1) or = 1;
			if(g[v] == AND) d[v][and] = min(d[v][and], d[v * 2][i] + d[v * 2 + 1][j]);
			else d[v][or] = min(d[v][or], d[v * 2][i] + d[v * 2 + 1][j]);
			if(c[v])
			{
				if(g[v] == AND) d[v][or] = min(d[v][or], d[v * 2][i] + d[v * 2 + 1][j] + 1);
				else d[v][and] = min(d[v][and], d[v * 2][i] + d[v * 2 + 1][j] + 1);
			}
		}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i;
	int r, cs = 0;
	scanf("%d", &r);
	while(r--)
	{
        scanf("%d %d", &n, &v);
        fill(d[0], d[n + 1], inf);
		fill(c, c + n + 1, 0);
		fill(g, g + n + 1, 0);
		for(i = 1; i <= n / 2; ++i)
		{
            scanf("%d %d", &g[i], &c[i]);
		}
		for(i = n / 2 + 1; i <= n; ++i)
		{
			int k;
			scanf("%d", &k);
			d[i][k] = 0;
		}
		solve(1);
		printf("Case #%d: ", ++cs);
		if(d[1][v] == inf) printf("IMPOSSIBLE\n");
		else printf("%d\n", d[1][v]);
	}
	return 0;
}