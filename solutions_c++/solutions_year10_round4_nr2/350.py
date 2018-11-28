#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <memory.h>
#include <queue>

using namespace std;

typedef vector<long long> VI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)
#define GI(n) scanf("%d", &n)
#define GI2(n, m) scanf("%d %d", &n, &m)

int c[1024];
int cost[10][1024];
int p, n;

#define INF 1000000000000000LL

VI go(int a, int r) {
	if(r == 0) {
		VI v(p+1, INF);
		int k = min(c[a], c[a+1]);
		int acost = cost[0][a/2];
		v[k] = acost;
		FIR(k) v[i] = 0;
		return v;
	}

	VI pl = go(a, r-1), pr = go(a + (1 << r), r-1);
	int acost = cost[r][a >> (r+1)];
	
	VI v(p+1, INF);
	FORD(miss, p-1, 0) {
		v[miss] = min(v[miss], pl[miss+1] + pr[miss+1]);
	}

	FORD(miss, p, 0) {
		v[miss] = min(v[miss], acost+pl[miss] + pr[miss]);
	}

	return v;
}

int solve() {
	GI(p);
	n = 1 << p;
	FI GI(c[i]);
	for (int r = 0, sz = n/2; r < p; ++r, sz /=2) 
		FIR(sz) GI(cost[r][i]);
	

	VI v = go(0, p-1);
	return *min_element(ALL(v));
}

int main() {
freopen("B-large.in", "rt", stdin);
freopen("B-large.out", "w", stdout);


	int ncases;
	GI(ncases);
	FORE(ncase, 1, ncases) {
		int res = solve();
		printf("Case #%d: %d\n", ncase, res);
	}
}
