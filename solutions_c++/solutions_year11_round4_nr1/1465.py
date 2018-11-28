#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <vector>
#include <string>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>

#include <iostream>
#include <sstream>
#include <iomanip>

#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

struct W
{
	long long b, e, s;
};

bool operator< (const W& a, const W& b)
{
	return a.s < b.s;
}

int main()
{
	int tests = 0;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		long long X, S, R, t, N;
		cin >> X >> S >> R >> t >> N;

		vector<W> w(N);
		double d = X;
		for (int i = 0; i < N; ++i)
		{
			cin >> w[i].b >> w[i].e >> w[i].s;
			d -= (w[i].e - w[i].b);
		}
		sort(w.begin(), w.end());

		double ans = 0.0;

		double tLeft = t;

		if (t * R >= d)
		{
			tLeft -= d / R;
			ans += d / R;
			d = 0.0;
		}
		else
		{
			d -= t * R;
			tLeft = 0.0;
			ans += t;
			ans += d / S;
		}

		// cout << ans << " " << tLeft << " " << d << endl;

		for (int i = 0; i < N; ++i)
		{
			double dist = w[i].e - w[i].b;
			if (tLeft > 0.0)
			{
				double distFast = tLeft * (R + w[i].s);
				if (distFast >= dist)
				{
					tLeft -= dist / (R + w[i].s);
					ans += dist / (R + w[i].s);
				}
				else
				{
					ans += tLeft;
					ans += (dist - distFast) / (S + w[i].s);
					tLeft = 0.0;
				}
			}
			else
				ans += dist / (S + w[i].s);

			// cout << ans << endl;
		}

		cout << "Case #" << test << ": " << fixed << setprecision(9) << ans << endl;
	}

	return 0;
}
