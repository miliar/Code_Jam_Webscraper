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


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int tt;
	cin >> tt;
	REP (t, tt)
	{
		printf ("Case #%d: ", t+1);

		VPII a;
		double t;
		int x, s, r, n;
		cin >> x >> s >> r >> t >> n;
		r-=s;

		while (n--)
		{
			int xx, yy, w;
			cin >> xx >> yy >> w;
			a.pb (PII (w+s, yy-xx));
			x-=yy-xx;
		}
		a.pb (PII(s, x));

		SORT (a);
		double res = 0;

		REP (i, a.size())
		{
			//cout << a[i].X << " " << a[i].Y << endl;
			double d = a[i].Y;
			double tt = d / (r+a[i].X);
			if (tt>t)
				tt = t;
			t-=tt;
			res += tt;

			//cout << res << endl;

			d -= tt*(r+a[i].X);

			res += d / a[i].X;
			//cout << res << endl;
		}

		printf ("%.6lf\n", res);


	}

	return 0;
}
