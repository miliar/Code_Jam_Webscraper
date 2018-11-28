#include <iostream>
using namespace std;

const int N = 100;
int c[N], d[N], a[N], pre[N];
bool g[N][N];
int x[N][25];

int bipartite(bool g[N][N], int n, int m)
{
	int i, j, x, ret, head, tail;
	ret = 0;
	for (i = 0; i < n; i++) c[i] = -1;
	for (i = 0; i < m; i++) d[i] = -1;
	for (i = 0; i < n; i++) 
	{
		for (j = 0; j < m; j++) pre[j] = -2;
		head = tail = 0;
		for (j = 0; j < m; j++)
			if (g[i][j]) 
			{
				pre[j] = -1;
				a[tail++] = j;
			}
		while (head < tail) 
		{
			x = a[head];
			if (d[x] == -1) break;
			head++;
			for (j = 0; j < m; j++) 
				if (pre[j] == -2 && g[d[x]][j]) 
				{
					pre[j] = x;
					a[tail++] = j;
				}
		}
		if (head == tail) continue;
		while (pre[x] > -1) 
		{
			c[d[pre[x]]] = x;
			d[x] = d[pre[x]];
			x = pre[x];
		}
		d[x] = i;
		c[i] = x;
		ret++;
	}
	return ret;
}

int main()
{
	int cas, num = 0;
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &cas);
	while (cas--)
	{
		int n, m;
		int i, j, k;
		scanf("%d %d", &n, &m);
		for (i = 0; i < n; ++i)
			for (j = 0; j < m; ++j)
				scanf("%d", &x[i][j]);
		memset(g, 0, sizeof(g));
		for (i = 0; i < n; ++i)
			for (j = 0; j < n; ++j)
			{
				if (i == j) continue;
				for (k = 0; k < m; ++k)
					if (x[i][k] >= x[j][k]) break;
				if (k == m) g[i][j] = true;
			}
		printf("Case #%d: %d\n", ++num, n - bipartite(g, n, n));
	}
	return 0;
}
