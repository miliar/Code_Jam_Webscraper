#include <iostream>
#include <algorithm>

using namespace std;

int x[800], y[800];

int main()
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt)
	{
		int n;
		cin >> n;
		for(int i = 0; i < n; ++i) cin >> x[i];
		for(int i = 0; i < n; ++i) cin >> y[i];
		sort(x, x + n);
		sort(y, y + n, greater<int>());
		long long res = 0;
		for(int i = 0; i < n; ++i) res += x[i] * y[i];
		printf("Case #%d: %d\n", tt, res);
	}
	return 0;
}
