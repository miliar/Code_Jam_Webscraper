#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int smax[2][1<<20];

int main()
{
	freopen ("c.in", "r", stdin);
	freopen ("c.out", "w", stdout);

	int t;
	cin >> t;

	for (int i = 0; i < t; i++)
	{
		memset(smax, 0, sizeof(smax));
		smax[0][0] = 1;

		cout << "Case #" << i + 1 << ": ";

		int n;
		cin >> n;
		int st = 0;
		int xt = 0;
		int minx = 1<<21;

		for (int j = 0; j < n; j++)
		{
			int q;
			cin >> q;
			st += q;
			xt ^= q;
			if (q < minx)
				minx = q;
		}

		if (xt != 0)
		{
			cout << "NO\n";
			continue;
		}

		cout << st - minx << "\n";
	}

	return 0;
}

