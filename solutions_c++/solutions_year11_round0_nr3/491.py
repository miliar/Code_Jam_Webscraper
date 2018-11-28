#include <iostream>
using namespace std;

int t, n, i, j, x, temp, sum, ans;

int main()
{
//	freopen("C-large.in", "r", stdin);
//	freopen("C-large.out", "w", stdout);
	for (i = 1, cin >> t; i <= t; ++i)
	{
		temp = sum = 0;
		ans = INT_MAX;
		for (j = 1, cin >> n; j <= n; ++j)
		{
			cin >> x;
			temp ^= x;
			sum += x;
			ans = min(ans, x);
		}
		if (temp == 0) cout << "Case #" << i << ": " << sum - ans << endl;
		else cout <<  "Case #" << i << ": " << "NO" << endl;
	}
	return 0;
}