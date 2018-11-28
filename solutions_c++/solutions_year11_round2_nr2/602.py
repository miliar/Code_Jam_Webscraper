#include <iostream>
#include <vector>
#include <algorithm>

const int MAXC = 200;
const double EPS = 1e-7;

using namespace std;

int main()
{
	int t, tn = 1;

	cout.setf(ios::fixed);

	cin >> t;

	while (tn <= t)
	{
		double l = 0, r = 1e10, m, curr, d;
		vector<pair<int, int> > inp;
		int c;
		bool ok;

		cin >> c >> d;
		inp.resize(c);

		for (int i = 0; i < c; i++)
			cin >> inp[i].first >> inp[i].second;

		sort(inp.begin(), inp.end());

		while (r - l > EPS)
		{
			ok = true;
			m = (l + r) / 2;

			if ((inp[0].second - 1) * d / 2.0 > m)
			{
				l = m;
				continue;
			}

			curr = (double)inp[0].first - m + inp[0].second * d;
			for (int i = 1; i < c; i++)
			{
				curr = max(curr, inp[i].first - m) + (inp[i].second - 1) * d;
				if (curr > inp[i].first + m)
				{
					ok = false;
					break;
				}
				curr += d;
			}

			if (ok)
				r = m;
			else
				l = m;
		}

		cout << "Case #" << tn << ": " << l << endl;

		tn++;
	}

	return 0;
}
