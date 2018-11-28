#include <iostream>
using namespace std;

int t, n, ans;

int main()
{
	int i, j, x;

//	freopen("D-large.in", "r", stdin);
//	freopen("D-large.out", "w", stdout);
	for (cin >> t, i = 1; i <= t; ++i)
	{
		ans = 0;
		for (cin >> n, j = 1; j <= n; ++j)
		{
			cin >> x;
			if (x != j) ++ans;
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}