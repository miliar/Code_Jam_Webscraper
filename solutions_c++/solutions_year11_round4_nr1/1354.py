#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

#define MAXN 1000
#define MP make_pair
#define F first
#define S second

const double eps = 1e-9;

int X, s, R, n;
double t;
vector < pair<double, double> > a, b;

inline bool cmp(pair<int, int> a1, pair<int, int> a2)
{
	return a1.S < a2.S;
}

inline double calc()
{
	double r = 0;
	for (int i = 0; i < a.size(); ++i)
		r += (double)a[i].S / (double)a[i].F;
	return r;
}

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	int tt;
	scanf("%d", &tt);
	for (int test = 0; test < tt; ++test)
	{
		scanf("%d%d%d%lf%d", &X, &s, &R, &t, &n);
		int tx = 0;
		a.clear();
		for (int i = 0; i < n; ++i)
		{
			int tb, te, tw;
			scanf("%d%d%d", &tb, &te, &tw);
			a.push_back(MP(tw + s, te - tb));
			tx += (te - tb);
		}
		if (X - tx > 0)
		{
			a.push_back(MP(s, X - tx));
			++n;
		}
		sort(a.begin(), a.end());
		for (int i = 0; i < n && abs(t) > eps; ++i)
		{
			double reqs = double(a[i].S) / double(a[i].F - s + R);
			if (t >= reqs)
			{
				t -= reqs;
				a[i].F = a[i].F - s + R;
			}
			else
			{
				double cov = double(a[i].F - s + R) * t;
				a[i].S -= cov;
				a.push_back(MP(a[i].F - s + R, cov));
				t = 0;
			}
		}
		printf("Case #%d: %.10lf\n", test + 1, calc());
	}
	return 0;
}
