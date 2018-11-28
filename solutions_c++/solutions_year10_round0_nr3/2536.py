#include <iostream>
#include <algorithm>
using namespace std;

int T, r, k, n, g[1000], f[1000][1000];

int main()
{
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cin >> r >> k >> n;
		for (int i = 0; i != n; ++i)
			cin >> g[i];
		for (int i = 0; i != n; ++i)
		{
			f[i][i] = g[i];
			for (int j = i + 1; j != n; ++j)
				f[i][j] = f[i][j - 1] + g[j];
			if (!i) continue;
			f[i][0] = f[i][n - 1] + g[0];
			for (int j = 1; j != i; ++j)
				f[i][j] = f[i][j - 1] + g[j];
		}
		int p = 0, ans = 0;
		while (r--)
		{
			int* a = upper_bound(f[p], f[p] + p, k);
			if (a == f[p])
				a = upper_bound(f[p] + p, f[p] + n, k);
			ans += *(a - 1);
			p = (a - f[p]) % n;
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}