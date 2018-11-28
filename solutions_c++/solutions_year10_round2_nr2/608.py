#include <iostream>
#include <vector>
#include <climits>

using	namespace	std;

static const int maxn = 50;

int	n, k, b, t;
int	x[maxn], v[maxn];
bool	pass[maxn];
int	f[maxn][maxn + 1];

void	solve()
{
	cin >> n >> k >> b >> t;
	for (int i = 0; i < n; ++i)
		cin >> x[i];
	for (int i = 0; i < n; ++i)
		cin >> v[i];

	if (k == 0)
	{
		cout << 0 << endl;
		return;
	}

	for (int i = 0; i < n; ++i)
		pass[i] = (b - x[i]) <= v[i] * t;

	int	ans = 0, passed = 0;
	for (int i = n - 1; i >= 0; --i)
	{
		if (pass[i])
		{
			++passed;
			for (int j = i + 1; j < n; ++j)
				if (!pass[j])	++ans;
		}
		if (passed >= k)
		{
			cout << ans << endl;
			return;
		}
	}

	cout << "IMPOSSIBLE" << endl;

/*
	for (int i = 0; i < n; ++i)
		for (int j = 0; j <= n; ++j)
			f[i][j] = INT_MAX;
	
	f[n - 1][0] = 0;
	if ((b - x[n - 1]) > v[n - 1] * t)
		f[n - 1][1] = INT_MAX;
	else
		f[n - 1][1] = 0;

	for (int i = n - 2; i >= 0; --i)
	{
		for (int j = 0; j < n - i; ++j)
			f[i][j] = f[i + 1][j];

		if ((b - x[i]) > v[i] * t)
			f[i][n - i] = INT_MAX;
		else
		{
			int	c = count(i);
			for (int j = 1; j <= n - i; ++j)
			{
				if (f[i + 1][j - 1] == INT_MAX)	continue;
				f[i][j] = min(f[i][j], f[i + 1][j - 1] + c);
			}
		}
		if ((n - i) >= k && f[i][k] != INT_MAX)
		{
			cout << f[i][k] << endl;
			return;
		}
	}

	int	ans = INT_MAX;
	for (int i = k; i <= n; ++i)
		ans = min(ans, f[0][i]);

	if (ans == INT_MAX)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << ans << endl;
*/
}

int	main()
{
	int	t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
}

