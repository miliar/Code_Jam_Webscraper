#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cmath>
#include <iterator>
#include <complex>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <list>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

int t, c, d;
vector <LD> x;

int main()
{
#ifdef DEBUG
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif

	cout << fixed << setprecision(10);
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		cin >> c >> d;
		x.clear();
		for (int i = 0; i < c; ++i)
		{
			int v; LD p;
			cin >> p >> v;
			for (; v; --v)
				x.push_back(p);
		}
		sort(x.begin(), x.end());

		LD ll = 0, rr = 1e18;
		for (int step = 0; step < 500; ++step)
		{
			LD m = (ll + rr) / 2;
			LD last = -1e18;
			bool good = true;
			for (int i = 0; i < x.size(); ++i)
			{
				last = max(last + d, x[i] - m);
				if (x[i] + m < last)
				{
					good = false;
					break;
				}
			}
			if (good) rr = m;
			else ll = m;
		}

		cout << "Case #" << tt << ": " << ll << '\n';

	}

	return 0;
}
