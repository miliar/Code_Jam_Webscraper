#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
#include <iostream>
#include <iomanip>
#include <vector>
#include <deque>
#include <stack>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++)
	{
		int n;
		cin >> n;
		vector <int> x(n), y(n), z(n), p(n);
		for (int i = 0; i < n; i++) cin >> x[i] >> y[i] >> z[i] >> p[i];
		double mi = 0.0, ma = 1e9;
		int it = 0;
		while (fabs (ma - mi) > 1e-9 && it < 100)
		{
			double mid = (mi + ma) / 2;
			vector <double> mh;
			for (int i = 0; i < n; i++) mh.push_back (mid * p[i]);
			int f = 1;
			for (int i = 0; i < n && f; i++)
				for (int j = i+1; j < n && f; j++)
				{
					if (mh[i] + mh[j] < -1e-9 + fabs(x[i]-x[j]) +
						fabs(y[i]-y[j]) + fabs(z[i]-z[j])) f = 0;
				}
			if (f) ma = mid+1e-9;
			else mi = mid;
			it++;
		}
		printf ("Case #%ld: %.8lf\n", cc, mi);
		//cout << "Case #" << cc << ": " << mi << endl;
	}
	return 0;
}
