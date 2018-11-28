# include <iostream>
# include <stdio.h>
# include <algorithm>
# include <functional>

using namespace std;

int a[1001];
int p[1000001];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out_debug.out", "w", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		int l, n, c;
		long long t, sum = 0;
		cin >> l >> t >> n >> c;
		int a[1001];
		for (int i = 0; i < c; ++i)
			cin >> a[i];
		int q = 0;
		for (int i = 0; i < n; ++i)
		{
			p[i] = a[q++];
			sum += 2 * p[i];
			if (q == c)
				q -= c;
		}

		t /= 2;
		for (int i = 0; i < n && t > 0; ++i)
		{
			if (p[i] < t)
			{
				t -= p[i];
				p[i] = 0;
			}
			else
			{
				p[i] -= t;
				t = 0;
			}
		}

		sort(p, p + n, std::greater<int>());

		for (int i = 0; i < l; ++i)
			sum -= p[i];

		cout << "Case #" << test << ": " << sum << endl;
	}
	return 0;
}