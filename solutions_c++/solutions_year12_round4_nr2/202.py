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
	cin  >> tt;
	REP (t, tt) {
		cout << "Case #" << t+1 << ":";
		int W, L, n;
		cin >> n >>W >> L;
		VPII r(n);
		REP (i, n) {
			cin >> r[i].X ;
			r[i].Y = i;
		}

		VI x(n);
		VI y(n);
		SORT (r);
		REVERSE(r);

		REP (i, n) {
			int xx = 0;
			if (i && x[i-1] + r[i-1].X + r[i].X <= W)
				xx = x[i-1] + r[i-1].X + r[i].X;
			int yy = 0;

			REP (j, i)
				if (abs(xx - x[j]) < r[i].X + r[j].X)
					yy = max (yy, y[j] + r[i].X + r[j].X);

			x[i] = xx;
			y[i] = yy;
			if (y[i] > L)
				while (1);
		}

		VI X(n);
		VI Y(n);

		REP(i, n) {
			X[r[i].Y] = x[i];
			Y[r[i].Y] = y[i];
		}

		REP (i, n)
			cout << " " << X[i] << " " << Y[i];
		cout << endl;
	}

	return 0;
}
