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

const int MaxN = 5120;

int N, a[MaxN], b[MaxN], c[MaxN];
int bList[MaxN];

bool bCmp(int i, int j) {
	return b[i] < b[j];
}

int solve()
{
	scanf("%d", &N);
	REP(i, N)
		scanf("%d %d %d", &a[i], &b[i], &c[i]);

	VI aun(a, a+N), bun(b, b+N), cun(c, c+N);
	UNIQUE(aun);
	UNIQUE(bun);
	UNIQUE(cun);

	REP(i, N)
		bList[i] = i;
	sort(bList, bList+N, bCmp);

	int best = 0;
	REP(i, aun.sz) {
		int a0 = aun[i];
		priority_queue<int> cQ;

		int bInd = 0;
		REP(j, bun.sz) {
			int b0 = bun[j];
			if (a0 + b0 > 10000)
				break;

			while (bInd < N) {
				int x = bList[bInd];
				if (b[x] > b0)
					break; else
					bInd++;

				if (a[x] <= a0)
					cQ.push(c[x]);
			}

			int c0 = 10000-a0-b0;
			while (cQ.sz && (cQ.top() > c0))
				cQ.pop();
			best = max(best, (int) cQ.size());
		}
	}

	return best;
}

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 1; iTest <= nTest; iTest++)
		printf("Case #%d: %d\n", iTest, solve());

	return 0;
}
