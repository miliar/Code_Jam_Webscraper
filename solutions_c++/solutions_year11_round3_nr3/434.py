#include <map>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


void main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cases;
	cin >> cases;
	for (int casen = 1; casen <= cases; casen++)
	{
		cout << "Case #" << casen << ": ";
		int n, l, h;
		cin >> n >> l >> h;
		vector<int> a(n);
		for (int i = 0; i < n; ++i)
		{
			cin >> a[i];
		}
		bool found = false;
		for (int i = l; i <= h; ++i)
		{
			bool good = true;
			for (int j = 0; j < n; ++j)
			{
				if (!(i % a[j] == 0 || a[j] % i == 0))
					good = false;
			}
			if (good)
			{
				cout << i << endl;
				found = true;
				break;
			}
		}
		if (!found)
			cout << "NO" << endl;
	}
}