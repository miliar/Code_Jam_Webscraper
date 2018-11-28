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
typedef long double cfloat;
typedef pair<cfloat, cfloat> PII;
typedef vector<cfloat> VI;
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

    	int n;
    	cin >> n;

    	VPII a(n);
    	VI r(n);
    	REP (i, n)
			cin >> a[i].X >> a[i].Y >> r[i];

    	long double res = 0;

    	if (n==3)
    	{
    		res = 1e100;

    		REP (i, 3)
				FOR (j, i+1, 3)
				{
					cfloat l = hypotl (abs(a[i].X - a[j].X), abs(a[i].Y - a[j].Y));
					cfloat r1 = r[i];
					cfloat r2 = r[j];
					cfloat r3 = r[3-i-j];

					if (r1<r2)
						swap (r1, r2);

					if (r2+l<r1)
						res <?= max(r2, r3);
					else
						res <?= max((r2+r1+l)/2, r3);
				}
    	}
    	else
    	{
    		REP (i, n)
				res >?= r[i];
    	}

    	printf ("%.6lf\n", (double)res);
    }

    return 0;
}
