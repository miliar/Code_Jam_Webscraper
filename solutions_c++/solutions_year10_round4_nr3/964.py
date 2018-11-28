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

struct Stripe
{
	int x, yMin, yMax;
	Stripe() {}
	Stripe(int a, int b, int c) : x(a), yMin(b), yMax(c) {}
};

inline bool operator<(const Stripe& a, const Stripe& b)
{
	if (a.x != b.x) return a.x < b.x;
	if (a.yMin != b.yMin) return a.yMin < b.yMin;
	return a.yMax < b.yMax;
}

typedef vector<Stripe> State;

void simplify(State& s)
{
	SORT(s);
	int k = 0;
	FOR(i, 1, s.sz) {
		if (s[k].x != s[i].x) {
			k++;
			s[k] = s[i];
			continue;
		}

		if (s[k].yMax+1 < s[i].yMin) {
			k++;
			s[k] = s[i];
		} else {
			s[k].yMax = s[i].yMax;
		}
	}
	s.resize(k+1);
}

bool has(const State& s, int x, int y)
{
	int L = 0, R = s.sz;
	while (R-L > 2) {
		int M = (L+R) >> 1;
		if (s[M].x == x && s[M].yMin <= y && y <= s[M].yMax)
			return true;

		if (s[M].x < x  || s[M].x == x && s[M].yMax < y)
			L = M; else
			R = M;
	}

	FOR(M, L, R)
		if (s[M].x == x && s[M].yMin <= y && y <= s[M].yMax)
			return true;

	return false;
}

bool table[2][256][256];

int solve2()
{
	memset(table[0], 0, sizeof(table[0]));
	int R;
	scanf("%d", &R);
	REP(i, R) {
		int x1, y1, x2, y2;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		FOR(x, x1, x2+1)
		FOR(y, y1, y2+1)
			table[0][x][y] = true;
	}

	for (int generation = 0; ; generation++) {
		int cur = generation % 2;
		int next = cur ^ 1;
		memset(table[next], 0, sizeof(table[next]));

		bool isEmpty = true;
		REP(x, 128) REP(y, 128) {
			if (table[cur][x][y]) {
				isEmpty = false;
				if (table[cur][x-1][y] || table[cur][x][y-1])
					table[next][x][y] = true;
			} else if (x && y)
				if (table[cur][x-1][y] && table[cur][x][y-1])
					table[next][x][y] = true;
		}

		if (isEmpty)
			return generation;
	}
}

int solve()
{
	int R;
	scanf("%d", &R);
	State s;
	REP(i, R) {
		int x1, y1, x2, y2;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		FOR(x, x1, x2+1)
			s.pb(Stripe(x, y1, y2));
	}

	simplify(s);

	int generation = 0;
	while (s.sz > 0) {
		generation++;
		State sNext;
		sNext.reserve(s.sz);

		REP(i, s.sz) {
			Stripe cur = s[i];
			if (has(s, cur.x-1, cur.yMax+1))
				cur.yMax++;
			if (!has(s, cur.x-1, cur.yMin))
				cur.yMin++;

			if (cur.yMin > cur.yMax)
				continue;

			if (sNext.empty()) {
				sNext.pb(cur);
			} else {
				if (sNext.back().x == cur.x &&
					sNext.back().yMax+1 == cur.yMin) {
						sNext.back().yMax = cur.yMax;
				} else
					sNext.pb(cur);
			}
		}

		s.swap(sNext);
	}

	return generation;
}

int main()
{
	string file_name;
	file_name = "example"; 
    freopen((file_name + ".in").c_str(), "r", stdin);
    freopen((file_name + ".out").c_str(), "w+", stdout);

	int nTest = 0;
	scanf("%d", &nTest);
	for (int iTest = 1; iTest <= nTest; iTest++) {
		printf("Case #%d: %d\n", iTest, solve2());
	}

    return 0;
}
