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

void solve(int iTest)
{
	i64 n, A, B, C, D, x0, y0, M;
	cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

	i64 cnt[3][3] = {{0,0,0}, {0,0,0}, {0,0,0}};
	i64 X = x0, Y = y0;
	REP(i, n) {
		cnt[X % 3][Y % 3]++;
		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
	}

	i64 total = 0;
	REP(i1, 3) REP(j1, 3)
	REP(i2, 3) REP(j2, 3)
	REP(i3, 3) REP(j3, 3) {
		if ((i1 + i2 + i3) % 3) continue;
		if ((j1 + j2 + j3) % 3) continue;
		int a1 = i1*3 + j1;
		int a2 = i2*3 + j2;
		int a3 = i3*3 + j3;
		if ((a1 > a2) || (a2 > a3))
			continue;

		i64 x1 = cnt[i1][j1];
		i64 x2 = cnt[i2][j2];
		i64 x3 = cnt[i3][j3];
		i64 d = 1;
		if ((a1 == a2) && (a2 != a3)) {
			x2--;
			d = 2;
		}
		if ((a2 == a3) && (a1 != a2)) {
			x3--;
			d = 2;
		}
		if ((a1 == a2) && (a2 == a3)) {
			x2 -= 1;
			x3 -= 2;
			d = 6;
		}

		total += x1*x2*x3/d;
	}

	cout << "Case #" << iTest << ": " << total << endl;
}

int main()
{
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small-attempt0.out", "wt", stdout);
	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 1; iTest <= nTest; iTest++)
		solve(iTest);
	return 0;
}
