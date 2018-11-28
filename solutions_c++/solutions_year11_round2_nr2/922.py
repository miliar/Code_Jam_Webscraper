# include <iostream>
# include <stdio.h>
# include <algorithm>
# include <math.h>

using namespace std;

const double EPS = 1e-7;

long long c, d;
pair<double, int> p[300];

bool can(double t)
{
	double last = p[0].first - t + p[0].second * d;
	if (fabs(last - d - p[0].first) > t + EPS)
			return false;

	for (int i = 1; i < c; ++i)
	{
		if (p[i].first - t > last)
			last = p[i].first - t;
		last += p[i].second * d;
		if (fabs(last - d - p[i].first) > t + EPS)
			return false;
	}
	return true;
}

int main()
{
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		cin >> c >> d;
		double v = 0;

		for (int i = 0; i < c; ++i)
		{
			cin >> p[i].first >> p[i].second;
			v += p[i].second;
		}

		sort(p, p + c);
		
		double l = 0;
		double r = d * v;
		while (r - l > EPS)
		{
			double m = (l + r) / 2.0;
			if (can(m))
			{
				r = m;
			}
			else
			{
				l = m;
			}
		}

		cout << "Case #" << test << ": " << (l + r) / 2.0 << endl;
	}

	return 0;
}