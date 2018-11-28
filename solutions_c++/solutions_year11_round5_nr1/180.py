#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include "string.h"
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

typedef long double cfloat;



cfloat square(const VPII& a, cfloat x)
{
	cfloat res = 0;
	REP (i, a.size()-1)
	{
		cfloat x1 = a[i].X;
		cfloat x2 = a[i+1].X;
		cfloat y1 = a[i].Y;
		cfloat y2 = a[i+1].Y;

		if (x1 > x)
			break;

		if (x2 > x)
		{
			y2 = (x-x1)/(x2-x1)*(y2-y1) + y1;
			x2 = x;
		}

		res += (y1+y2)/2*(x2-x1);
	}

	return res;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int tt;
	cin >> tt;
	REP (t, tt)
	{
		printf ("Case #%d:\n", t+1);

		int w, l, u, g;

		cin >> w >> l >> u >> g;
		VPII a(l), b(u);

		REP (i, l)
			cin >> a[i].X >> a[i].Y;

		REP (i, u)
			cin >> b[i].X >> b[i].Y;

		cfloat s = square(b, w) - square(a, w);

		REP(i, g-1)
		{
			cfloat ss = (s/g)*(i+1);

			cfloat x1 = 0;
			cfloat x2 = w;

			REP (j, 200)
			{
				cfloat x = (x1+x2)/2;

				cfloat r = square(b, x) - square(a, x);

				if (r > ss)
					x2 = x;
				else
					x1 = x;
			}

			printf ("%.6lf\n", (double)x1);
		}
	}

	return 0;
}
