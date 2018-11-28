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

int R, C;
int cnt[Max][Max];
bool present[Max][Max];

inline bool isNotNull(int r, int c) {
	if ((r < 0) || (r >= R) || (c < 0) || (c >= C))
		return true;
	return cnt[r][c] > 0;
}

bool canPut(int r, int c)
{
	return (cnt[r-1][c-1] > 0) && (cnt[r-1][c  ] > 0) && (cnt[r-1][c+1] > 0) &&
		   (cnt[r  ][c-1] > 0) && (cnt[r  ][c  ] > 0) && (cnt[r  ][c+1] > 0) &&
		   (cnt[r+1][c-1] > 0) && (cnt[r+1][c  ] > 0) && (cnt[r+1][c+1] > 0);
}

void put(int r, int c, int v)
{
	cnt[r-1][c-1] += v;
	cnt[r-1][c  ] += v;
	cnt[r-1][c+1] += v;
	cnt[r  ][c-1] += v;
	cnt[r  ][c  ] += v;
	cnt[r  ][c+1] += v;
	cnt[r+1][c-1] += v;
	cnt[r+1][c  ] += v;
	cnt[r+1][c+1] += v;
}

int best;

void dfs(int r, int c)
{
	if (c > C) {
		c = 1;
		r++;
	}
	if (r > 1) {
		if (c == 1) {
			if (r-2 >= 1) {
				if (cnt[r-2][C] > 0)
					return;
				if ((C-1 > 0) && (cnt[r-2][C-1] > 0))
					return;
			}
		} else {
			if (c-2 >= 1)
				if (cnt[r-1][c-2] > 0)
					return;
		}
	}

	if (r > R) {
		REP(i, R) REP(j, C)
			if (cnt[i+1][j+1] > 0)
				return;

		/*		
		REP(i, R) {
			REP(j, C)
				putchar(present[i+1][j+1] ? '*' : '.');
			puts("");
		}
		*/
		int val = count(present[(R+1)/2], present[(R+1)/2]+C+2, true);
		best = max(best, val);
		return;
	}

	if (canPut(r, c)) {
		put(r, c, -1);
		present[r][c] = true;
			dfs(r, c+1);
		present[r][c] = false;
		put(r, c, +1);
	}

	dfs(r, c+1);
}

int solve()
{
	scanf("%d %d", &R, &C);
	REP(r, R+2) REP(c, C+2) {
		cnt[r][c] = INF;
		present[r][c] = false;
	}

	FOR(r, 1, R+1) FOR(c, 1, C+1)
		scanf("%d", &cnt[r][c]);

	best = -1;
	dfs(1, 1);
	return best;
}

int main()
{
/*
	freopen("input.txt", "wt", stdout);

	REP(xxx, 100) {
		puts("49 49");
		R = C = 49;
		REP(i, R) REP(j, C)
			cnt[i+1][j+1] = 0;
		REP(i, 200) {
			int x = 1 + rand() % 49, y = 1 + rand() % 49;
			if (present[y][x])
				continue;
			present[y][x] = true;
			put(y, x, +1);
		}
		REP(i, R) {
			REP(j, C)
				printf("%d ", cnt[i+1][j+1]);
			puts("");
		}
	}

	return 0;
*/
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small-attempt0.out", "wt", stdout);

	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 1; iTest <= nTest; iTest++)
		printf("Case #%d: %d\n", iTest, solve());

	return 0;
}
