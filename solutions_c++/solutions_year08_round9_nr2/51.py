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

// BEGIN CUT HERE
#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef long long i64;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
// END CUT HERE

int W, H;
int vx, vy, ux, uy;

inline bool inside(int x, int y) { return (x >= 0) && (x < W) && (y >= 0) && (y < H); }

int go(int x, int y)
{
	set<PII> s;
	VPII r;
	r.push_back(PII(x,y));
	s.insert(r[0]);

	for (int i = 0; i < r.sz; i++) {
		PII a = r[i];
		PII av = PII(a.X + vx, a.Y + vy);
		PII au = PII(a.X + ux, a.Y + uy);
		if (inside(av.X, av.Y) && (s.count(av) == 0)) {
			s.insert(av);
			r.pb(av);
		}
		if (inside(au.X, au.Y) && (s.count(au) == 0)) {
			s.insert(au);
			r.pb(au);
		}
	}

	return s.sz;
}

int solveLine()
{
	int L1 = go(0, 0);
	int L2 = go(W-1, 0);
	int L3 = go(0, H-1);
	int L4 = go(W-1, H-1);

	return max(max(L1, L2), max(L3, L4));
}

int solve()
{
	scanf("%d %d %d %d %d %d", &W, &H, &vx, &vy, &ux, &uy);

	int x0, y0;
	scanf("%d %d", &x0, &y0);
	return go(x0, y0);
/*
	if (vx*uy - vy*ux == 0)
		return solveLine();

	int best = -1;
	REP(x, W) REP(y, H) {
		if (inside(x-vx, y-vy) || inside(x-ux, y-uy))
			continue;

		best = max(best, go(x, y));
	}
	return best;
*/
}

int main()
{
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small-attempt0.out", "wt", stdout);

	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 1; iTest <= nTest; iTest++)
		printf("Case #%d: %d\n", iTest, solve());

	return 0;
}
	