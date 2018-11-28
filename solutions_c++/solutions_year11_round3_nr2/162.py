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
	int T, l, n, c, a;
	long long t;

	cin >> T;
	for(int tc = 1; tc <= T; tc++)
	{
		cin >> l >> t >> n >> c;

		vector<int> d(n);
		for (int i = 0; i < c; i++)
		{
			cin >> a;

			for (int k = 0; k*c + i < n; k++)
			{
				d[k*c + i] = a;
			}
		}

		int pos;
		long long time = 0, res = 0;
		for (pos = 0; pos < n && time < t; pos++)
		{
			res += 2 * d[pos];
			time += 2*  d[pos];
		}
		
		vector<int> tmp(d.begin() + pos, d.end());
		if (time > t)
		{
			res = t;
			tmp.push_back((time - t) / 2);
		}
		sort(tmp.rbegin(), tmp.rend());

		int tl = 0;
		for (int i = 0; i < tmp.size(); i++)
		{
			if (tl < l)
			{
				res += tmp[i];
				tl++;
			}
			else
			{
				res += 2 * tmp[i];
			}
		}

		cout << "Case #" << tc << ": " << res << endl;
	}

	return 0;
}