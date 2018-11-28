#include <iostream>
using namespace std;

int main()
{
	int t, i, ans, n, a[1000], b[1000], j, k;
	cin >> t;
	for ( i = 0; i < t; i ++)
	{
		ans = 0;
		cin >>n;
		for (j = 0; j < n; j++)
		{
			cin >> a[j] >> b[j];
		}
		for (j = 0; j < n; j++)
		{
			for (k = 0; k <n; k++)
			{
				if (j != k)
				{
					if ((a[j] - a[k]) * (b[j] - b[k]) < 0) ans++;
				}
			}
		}
		ans /= 2;
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}