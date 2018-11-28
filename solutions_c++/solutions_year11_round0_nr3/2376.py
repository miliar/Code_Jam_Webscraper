#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int a[10000];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, I = 0;
	cin >> t;
	while (t--)
	{
		I++;
		cout << "Case #" << I << ": ";
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		sort(a, a + n);
		int d = 0;
		int sum = 0;
		for (int i = 0; i < n; i++)
		{
			d ^= a[i];
			sum += a[i];
		}
		if (d != 0)
			cout << "NO" << endl;
		else
			cout << sum - a[0] << endl;
	}
	return 0;
}