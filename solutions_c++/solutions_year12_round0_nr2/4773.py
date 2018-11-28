#include <iostream>
using namespace std;
int t, n, s, p, a[3], ans, k;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		ans = 0;
		cin >> n >> s >> p;
		for (int j = 0; j < n; j++)
		{
			cin >> k;
			if (k % 3 == 2)
			{
				a[0] = a[1] = k / 3 + 1;
				a[2] = k / 3;
			}
			if (k % 3 == 1)
			{
				a[0] = k / 3 + 1;
				a[1] = a[2] = k / 3;
			}
			if (k % 3 == 0)
			{
				a[0] = a[1] = a[2] = k / 3;
			}
			if (a[0] >= p) ans++;
			else
			{
				if (k > 1 && s && a[0] == p - 1 && k % 3 != 1)
				{
					ans++;
					s--;
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
}