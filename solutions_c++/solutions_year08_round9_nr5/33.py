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

const int Max = 64;

int countBits[0xFFFF];

int R, C;
char tbl[Max][Max];

int solve()
{
	scanf("%d %d", &R, &C);
	REP(i, R)
		scanf("%s", tbl[i]);

	VPII prev(1, PII(0, 0));
	REP(i, R) {
		int qMask = 0, bMask = 0;
		REP(j, C) {
			if (tbl[i][j] == '?')
				qMask |= (1 << j);
			if (tbl[i][j] == '#')
				bMask |= (1 << j);
		}

		//puts(tbl[i]);

		VPII thisList;
		thisList.reserve(1 << countBits[qMask]);
		for (int v = qMask; ; v = (v-1) & qMask) {
			int curMask = v | bMask;
			
			int happy = 4*countBits[curMask];
			int i1 = 1, i2 = 2;
			REP(j, C-1) {
				if ((curMask & i1) && (curMask & i2))
					happy -= 2;
				i1 <<= 1;
				i2 <<= 1;
			}

			int best = -1;
			REP(j, prev.sz) {
				int cur = prev[j].Y + happy - 2*countBits[prev[j].X & curMask];
				if (best < cur)
					best = cur;
			}

			thisList.pb( PII(curMask, best) );
			//REP(j, C)
			//	if (curMask & (1 << j))
			//		putchar('#'); else
			//		putchar('.');
			//printf("  -- %d\n", best);

			if (v == 0)
				break;
		}
		//puts("");

		prev.swap(thisList);
	}

	int ans = 0;
	REP(i, prev.sz)
		ans = max(ans, prev[i].Y);
	return ans;
}

int main()
{
	freopen("E-small-attempt0.in", "rt", stdin);
	//freopen("E-small-attempt0", "rt", stdin);

	countBits[0] = 0;
	FOR(i, 1, 0x10000)
		countBits[i] = countBits[i & (i-1)]+1;
	
	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 1; iTest <= nTest; iTest++)
		printf("Case #%d: %d\n", iTest, solve());

	return 0;
}
