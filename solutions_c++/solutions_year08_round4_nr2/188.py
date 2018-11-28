#include <iostream>

using	namespace	std;

const	int	maxp = 10000;

int	cases;
bool	p[maxp + 1];

void	show(int x1, int y1, int x2, int y2, int x3, int y3)
{
	printf("Case #%d: %d %d %d %d %d %d\n", ++cases, x1, y1, x2, y2, x3, y3);
}

void	solve()
{
	int	n, m, a;
	scanf("%d%d%d", &n, &m, &a);
	if (a <= n)
	{
		show(0, 0, a, 0, 0, 1);
		return;
	}
	else if (a <= m)
	{
		show(0, 0, 1, 0, 0, a);
		return;
	}
	for (int i = 2; i < a; ++i)
	{
	//	if (!p[i])	continue;
		if (a % i)	continue;
		if (i <= n && a / i <= m)
		{
			show(0, 0, i, 0, 0, a / i);
			return;
		}
		if (i <= m && a / i <= n)
		{
			show(0, 0, a / i, 0, 0, i);
			return;
		}
	}
	for (int x1 = 0; x1 <= n; ++x1)
		for (int y1 = 0; y1 <= m; ++y1)
			for (int x2 = x1; x2 <= n; ++x2)
				for (int y2 = 0; y2 <= m; ++y2)
					for (int x3 = x2; x3 <= n; ++x3)
						for (int y3 = 0; y3 <= m; ++y3)
						{
							if (abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) == a)
							{
							show(x1, y1, x2, y2, x3, y3);
							return;
							}
						}
	printf("Case #%d: IMPOSSIBLE\n", ++cases);
}

void	init()
{
	for (int i = 3; i < maxp; i += 2)	p[i] = true;
	p[2] = true;
	for (int i = 3; i < maxp; i += 2)
	{
		if (p[i])
		{
			for (int j = i * i; j < maxp; j += i)
				p[j] = false;
		}
	}
}

int	main()
{
	init();
	int	t;
	scanf("%d", &t);
	while (t--)	solve();
	return	0;
}

