#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test)
	{
		int n;
		cin >> n;
		int xo = 0;
		int sum = 0, mn = 1005000;
		for (int i = 0; i < n; ++i)
		{
			int a;
			cin >> a;
			mn = min(mn, a);
			sum += a;
			xo ^= a;
		}

		cout << "Case #" << test << ": ";
		if (xo)
			cout << "NO\n";
		else
			cout << sum - mn << endl;
	}

	return 0;
}
