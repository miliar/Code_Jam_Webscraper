#include <iostream>
#include <cstdio>

using namespace std;

int a[1000 + 100];

int solve ()
{
	int n;
	cin >> n;
	int res = n;

	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
		if (a[i] == i + 1)
			res--;
	}

	return res;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		double x = solve();
		cout << "Case #" << i << ": ";
		printf ("%.6f\n", x);
	}

	return 0;
}
