#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int n;
string s;

int d[31];
int dd[31];

int main()
{
	for (int i=0; i<=30; ++i)
		d[i] = dd[i] = -1;
	for (int i=0; i<=10; ++i)
		for (int j=0; j<=10; ++j)
			for (int k=0; k<=10; ++k)
			{
				int dmin = min(min(i, j), k);
				int dmax = max(max(i, j), k);
				int dsum = i + j + k;
				if (dmax - dmin > 2) continue;
				dd[dsum] = max(dd[dsum], dmax);
				if (dmax - dmin > 1) continue;
				d[dsum] = max(d[dsum], dmax);
			}
	int t;
	cin >> t;
	for (int i=1; i<=t; ++i)
	{
		cout << "Case #" << i << ": ";
		int n, s, p, r = 0;
		cin >> n >> s >> p;
		for (int j=0; j<n; ++j)
		{
			int q;
			cin >> q;
			if (d[q] >= p) ++r;
			else if (dd[q] >= p && s > 0)
			{
				--s;
				++r;
			}
		}
		cout << r << endl;
	}
	return 0;
}
