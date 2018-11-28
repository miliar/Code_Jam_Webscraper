#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
#include <iostream>
using namespace std;

int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n, l, h;

	cin >> t;
	for(int tc = 1; tc <= t; tc++)
	{
		cin >> n >> l >> h;

		vector<int> s(n);
		for (int i = 0; i < n; i++)
		{
			cin >> s[i];
		}

		bool gotcha = false;
		int f;
		for (f = l; f <= h && !gotcha; f++)
		{
			int cnt = 0;
			for (int j = 0; j < n; j++)
			{
				if (s[j] % f == 0 || f % s[j] == 0)
				{
					cnt++;
				}
			}
			if (cnt == n)
			{
				gotcha = true;
			}
		}

		if (gotcha)
		{
			cout << "Case #" << tc << ": " << f - 1 << endl;
		}
		else
		{
			cout << "Case #" << tc << ": NO" << endl;
		}
	}

	return 0;
}