#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int T, i, j, n;
	int a[801], b[801];
	freopen("aa.in", "r", stdin);
	freopen("aa.out", "w", stdout);
	cin >> T;
	for (i = 1; i <= T; i ++)
	{
		cin >> n;
		for (j = 0; j < n; j ++)
			cin >> a[j];
		for (j = 0; j < n; j ++)
			cin >> b[j];
		
		sort(a, a+n);
		sort(b, b+n);

		int ans = 0;
		for (j = 0; j < n; j ++)
			ans += a[j]*b[n-1-j];
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
