#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

using namespace std;


struct Z
{
	double b, e, v;
	bool operator < (const Z& z) const
	{
		return v < z.v;
	}
};

bool cmp(Z a, Z b)
{
	return a.b < b.b;
}

int n;
Z z[5010];
double s, r, x;
double t;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int _t = 0; _t < T; ++_t)
	{
		cin >> x >> s >> r >> t >> n;
		for (int i = 0; i < n; ++i)
			cin >> z[i].b >> z[i].e >> z[i].v;

		sort(z, z + n, cmp);
		int lx = 0;
		int nn = n;
		for (int i = 0; i < n; ++i)
		{
			if (z[i].b > lx + 1e-7)
			{
				z[nn].b = lx;
				z[nn].e = z[i].b;
				z[nn].v = 0;
				++nn;
			}
			lx = z[i].e;
		}

		if (lx + 1e-7 < x)
		{
			z[nn].b = lx;
			z[nn].e = x;
			z[nn].v = 0;
			++nn;
		}
		n = nn;



		sort(z, z + n);
		double res = 0;
		for (int i = 0; i < n; ++i)
		{
			
			double L = z[i].e - z[i].b;
			double v = z[i].v + r;
			double nt = min(t, L / v);
			if (t > 0)
			{
				res += nt;
				t -= nt;
				L -= nt * v;
			}
			if (L > 0)
			{
				v = z[i].v + s;
				res += L / v;
			}
			
		}
		

		printf("Case #%d: %.6lf\n", _t + 1, res);
		
	}

	return 0;
}