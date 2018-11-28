#include <cstdio>
#include <cstring>
#include <cmath>

int nt;
int n;

int x[102];
int L;


int d[102][102];

int rec(int from, int to)
{
	if (d[from][to] != -1) return d[from][to];

	if (from == to)
	{
		return x[to + 1] - x[from - 1] - 2;
	}

	if (from > to)
	{
		return 0;
	}

	int res = -1;

	for(int k = from; k <= to; k++)
	{
		int cur = x[to + 1] - x[from - 1] - 2 + rec(from, k - 1) + rec(k + 1, to);
		if (res == -1 || res > cur) res = cur;		
	}

	d[from][to] = res;

	return res;
}


int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d %d", &L, &n);

		for(int i = 1; i <= n; i++) scanf("%d", &x[i]);

		x[0] = 0;
		x[n + 1] = L + 1;

		memset(d, -1, sizeof d);
		
		printf("%d\n", rec(1, n));
	}

	return 0;	
}