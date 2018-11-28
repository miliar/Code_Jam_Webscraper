#include <iostream>

using	namespace	std;

const	int	maxm = 10000;

int	m, v;
int	g[maxm + 1];
int	c[maxm + 1];
int	l[maxm + 1];
int	cases, ans;
int	f[maxm + 1][2];

int	calc(int a, int b)
{
	if (a == INT_MAX || b == INT_MAX)	return	INT_MAX;
	return	a + b;
}

void	calc(int id)
{
	if (id > (m - 1) / 2)
	{
		f[id][l[id]] = 0;
		f[id][1 - l[id]] = INT_MAX;
		return;
	}
	calc(id * 2);
	calc(id * 2 + 1);
	if (g[id] == 1)
	{
		f[id][1] = calc(f[id * 2][1], f[id * 2 + 1][1]);
		f[id][0] = min(min(calc(f[id * 2][1], f[id * 2 + 1][0]),
					calc(f[id * 2][0], f[id * 2 + 1][1])),
				calc(f[id * 2][0], f[id * 2 + 1][0]));
		if (c[id] == 1)
		{
			int	t = calc(f[id * 2][0], f[id * 2 + 1][0]);
			if (t != INT_MAX)
				f[id][0] = min(f[id][0], t + 1);
			t = min(min(calc(f[id * 2][1], f[id * 2 + 1][0]),
							calc(f[id * 2][0], f[id * 2 + 1][1])),
				calc(f[id * 2][1], f[id * 2 + 1][1]));
			if (t != INT_MAX)
				f[id][1] = min(f[id][1], t + 1);
		}
	}
	else
	{
		f[id][0] = calc(f[id * 2][0], f[id * 2 + 1][0]);
		f[id][1] = min(min(calc(f[id * 2][1], f[id * 2 + 1][0]),
					calc(f[id * 2][0], f[id * 2 + 1][1])),
				calc(f[id * 2][1], f[id * 2 + 1][1]));
		if (c[id] == 1)
		{
			int	t = calc(f[id * 2][1], f[id * 2 + 1][1]);
			if (t != INT_MAX)
				f[id][1] = min(f[id][1], t + 1);
			t = min(min(calc(f[id * 2][1], f[id * 2 + 1][0]),
							calc(f[id * 2][0], f[id * 2 + 1][1])),
				calc(f[id * 2][0], f[id * 2 + 1][0]));
			if (t != INT_MAX)
			f[id][0] = min(f[id][0], t + 1);
		}
	}
}

void	solve()
{
	scanf("%d%d", &m, &v);
	for (int i = 1; i <= (m - 1) / 2; ++i)
		scanf("%d%d", &g[i], &c[i]);
	for (int i = (m - 1) / 2 + 1; i <= m; ++i)
		scanf("%d", &l[i]);
	calc(1);
	if (f[1][v] != INT_MAX)
		printf("Case #%d: %d\n", ++cases, f[1][v]);
	else
		printf("Case #%d: IMPOSSIBLE\n", ++cases);
}

int	main()
{
	int	t;
	scanf("%d", &t);
	while (t--)	solve();
}

