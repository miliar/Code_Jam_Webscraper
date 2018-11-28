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

inline PII operator - (const PII &a, const PII &b) { return PII(a.X-b.X, a.Y-b.Y); }

const int Module = 10007;

int W, H, N;
map<PII, int> numWays;

int countPow(int N)
{
	int r = 0;
	while (N >= Module)
		r += N /= Module;
	return r;
}

int gcd(int a, int b)
{
	while (b != 0) {
		int r = a % b;
		a = b;
		b = r;
	}
	return a;
}

int binom(int N, int K)
{
	int p = countPow(N) - countPow(N-K) - countPow(K);
	if (p > 0)
		return 0;

	VI e(K);
	REP(i, K)
		e[i] = N-i;
	FOR(j, 2, K+1) {
		int v = j;
		for (int t = 0; t < e.sz; t++) {
			int d = gcd(e[t], v);
			if (d == 1)
				continue;

			e[t] /= d;
			if (e[t] == 1) {
				e[t] = e.back();
				e.pop_back();
				t--;
			}

			v /= d;
			if (v == 1)
				break;
		}
	}
	int res = 1;
	REP(i, e.sz)
		res = (res * (e[i] % Module)) % Module;
	return res;
}

int countWays(PII p)
{
	if (p.X > p.Y)
		swap(p.X, p.Y);
	if ((p.X + p.Y) % 3 != 0)
		return 0;

	int k = (p.X + p.Y) / 3;
	p.X -= k;
	p.Y -= k;
	if ((p.X < 0) || (p.Y < 0))
		return 0;
	if (p.X+p.Y == 0)
		return 1;

	if (numWays.count(p))
		return numWays[p];

	return numWays[p] = binom(p.X+p.Y, p.X);
}

int solve()
{
	scanf("%d %d %d", &H, &W, &N);
	VPII rock(N);
	REP(i, N)
		scanf("%d %d", &rock[i].Y, &rock[i].X);

	SORT(rock);
	int total = 0;
	REP(mask, 1 << rock.sz) {
		VPII route;
		route.pb(PII(1,1));
		REP(j, rock.sz)
			if (mask & (1 << j))
				route.pb(rock[j]);
		route.pb(PII(W,H));

		int cur = 1;
		REP(i, route.sz-1)
			cur = (cur * countWays(route[i+1] - route[i])) % Module;
		
		if (route.sz % 2 == 1)
			total -= cur; else
			total += cur;
	}
	total %= Module;
	if (total < 0)
		total += Module;
	return total;
}

int main()
{
	freopen("D-small-attempt0.in", "rt", stdin);
	freopen("D-small-attempt0.out", "wt", stdout);
	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 1; iTest <= nTest; iTest++)
		cout << "Case #" << iTest << ": " << solve() << endl;
	return 0;
}
