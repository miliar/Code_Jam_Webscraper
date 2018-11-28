#include <iostream>

using	namespace	std;

static const int maxn = 30;
int	x[maxn + 1];

void	solve()
{
	int	n, k;
	cin >> n >> k;
	k %= x[n] + 1;
	if (k == x[n])
		cout << "ON" << endl;
	else
		cout << "OFF" << endl;
}

int	main()
{
	x[0] = 0;
	for (int i = 1; i <= maxn; ++i)
		x[i] = 2 * x[i - 1] + 1;
	int	t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
}

