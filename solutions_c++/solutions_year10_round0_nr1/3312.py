#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	cin >> t;

	for (int i = 1; i <= t; ++i)
	{
		int n, k, isOn = 0;
		cin >> n >> k;

		if (k != 0)
		{
			int x = 1 << n;
			isOn = !((k + 1) % x);
		}

		printf("Case #%d: %s\n", i, isOn ? "ON" : "OFF");
	}

	return 0;
}
