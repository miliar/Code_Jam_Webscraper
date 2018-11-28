# include <iostream>
# include <algorithm>
# define MAXN 805
using namespace std;

typedef long long llong;

llong a[MAXN], b[MAXN];

int main()
{
	int cases, i , j, n, t = 0;
	llong ans;
	freopen("D:\\A1.in", "r", stdin);
	freopen("D:\\A1.out", "w", stdout);
	cin >> cases;
	while (cases--)
	{
		cin >> n;
		for (i = 0; i < n; i++) cin >> a[i];
		for (i = 0; i < n; i++) cin >> b[i];
		sort(a, a + n);
		sort(b, b + n);
		ans = 0;
		for (i = 0, j = n - 1; i < n; i++, j--)
			ans += a[i] * b[j];
		cout << "Case #" << ++t <<": "<< ans << endl;
	}
	return 0;
}