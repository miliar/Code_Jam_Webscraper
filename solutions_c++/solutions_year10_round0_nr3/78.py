#include <iostream>

using	namespace	std;

static const int maxn = 1000;
int	g[maxn];

int	next(int now, int n)
{
	++now;
	if (now == n)	now = 0;
	return now;
}

void	solve()
{
	int	r, k, n;
	cin >> r >> k >> n;
	for (int i = 0; i < n; ++i)
		cin >> g[i];

	long long	count = 0, cost = 0;
	int	index = 0;
	while (true)
	{
		long long	amount = 0;
		int	from = index;
		while (amount + g[index] <= k)
		{
			amount += g[index];
			index = next(index, n);
			if (index == from)	break;
		}

		++count;
		cost += amount;

		if (count >= r)
		{
			cout << cost << endl;
			return;
		}

		if (index == 0)	break;
	}

	cost = cost * (r / count);
	r %= count;
	count = 0;

	if (count >= r)
	{
		cout << cost << endl;
		return;
	}

	while (true)
	{
		long long	amount = 0;
		int	from = index;
		while (amount + g[index] <= k)
		{
			amount += g[index];
			index = next(index, n);
			if (index == from)	break;
		}

		++count;
		cost += amount;

		if (count >= r)
		{
			cout << cost << endl;
			return;
		}
	}
}

int	main()
{
	int	t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return	0;
}

