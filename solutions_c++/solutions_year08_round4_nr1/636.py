#include <stdio.h>

#define maxn 10010
#define inf 20000
#define maxl 2
#define min(a,b) (a < b ? a : b)

int n, rez;
int c[maxn][maxl];
int x[maxn], y[maxn];

int calc(int nod, int type, int rez)
{
	if (rez ^ type) return min(c[nod*2][rez], c[nod*2+1][rez]);
	else return c[nod*2][rez] + c[nod*2+1][rez];
}

void DFS(int nod)
{
	if (nod <= (n-1)/2) 
	{
		DFS(nod*2);
		DFS(nod*2+1);

		int i;

		for (i=0; i<maxl; i++) c[nod][i] = calc(nod, x[nod], i);

		if (y[nod])
			for (i=0; i<maxl; i++) c[nod][i] = min(c[nod][i], calc(nod, x[nod]^1, i) + 1);
	}
}

int main()
{
	freopen("tree.in", "r", stdin);
	freopen("tree.out", "w", stdout);

	int i, t, T, aux;

	scanf("%d ", &T);

	for (t=1; t<=T; t++)
	{
		scanf("%d %d ", &n, &rez);

		for (i=1; i<=n; i++) c[i][0] = c[i][1] = inf;

		for (i=1; i<=(n-1)/2; i++) scanf("%d %d ", &x[i], &y[i]);

		for (i=(n-1)/2+1; i<=n; i++) 
		{
			scanf("%d ", &aux);
			c[i][aux] = 0;
		}

		DFS(1);

		printf("Case #%d: ", t);
		if (c[1][rez] >= inf) printf("IMPOSSIBLE\n");
		else printf("%d\n", c[1][rez]);
	}

	return 0;
}
