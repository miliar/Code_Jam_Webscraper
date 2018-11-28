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

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int tt;
	cin >> tt;
	REP (t, tt)
	{
		cfloat f, R, T, r, g;

		cin >> f >> R >> T >> r >> g;

		T+=f;
		r+=f;
		g-=2*f;

		cfloat step = R / 2000000;

		cfloat p0 = 0;
		cfloat p1 = 0;
		cfloat xx1 = r;
		cfloat xx2 = r+g;
		if (g<=0)
		{
			p0 = 1;
			p1 = 1;
		}
		else
		for (cfloat x = 0; x<R-1e-9; x+=step)
		{
			while (x>xx2)
			{
				xx1+=g+r+r;
				xx2+=g+r+r;
			}
			cfloat y = sqrtl(R*R-x*x);
			if (x>=R-T || (x<xx1) || (x>xx2))
			{
				p0 += y;
				p1 += y;
			}
			else
			{
				p0 += y;
				p1 += y;
				cfloat yy = sqrtl ((R-T)*(R-T)-x*x);

				cfloat y2 = r;
				while (y2<yy)
				{
					cfloat y3 = y2+g;
					y3<?=yy;
					p0 -= (y3-y2);
					y2+=g+2*r;
				}
			}
		}

		printf ("Case #%d: %.6lf\n", t+1, (double)(p0/p1));
	}

	return 0;
}
