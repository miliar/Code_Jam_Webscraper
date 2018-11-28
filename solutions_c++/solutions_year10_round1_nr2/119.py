#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
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

int f[128][256];
int D, I, M, n;
int a[128];

int change(int from , int to) {
	int d = abs(from - to);
	if (M) {
		return min(d, ( (d+ M-1) / M) * I);
	}

	return d;
}

bool ok(int a, int b) {
	return abs(a-b) <= M;
}

int solve() {
	cin >> D >> I >> M >> n;
	FI cin >> a[i];
	FIR(256) f[n][i] = 0;
	FORD(pos, n-1, 0) FIR(256) {
		int& res = f[pos][i];
		res = change(a[pos],i) + (n-1-pos)*D;
		res = min(res, D + f[pos+1][i]);
		
		FJR(256) if (ok(a[pos], j))
			res = min(res, change(a[pos],i) + f[pos+1][j]);

		FJR(256) if (ok(i, j))
			res = min(res, abs(a[pos] -i) + f[pos+1][j]);
	}

	int res = n*D;
	FIR(256) res = min(res, f[0][i]);
	return res;
}


int main() {
freopen("B-small-attempt0.in", "rt", stdin);
freopen("B-small-attempt0.out", "w", stdout);


	int tests;
	cin >> tests;
	FORE(T, 1, tests) {
		int res = solve();
		printf("Case #%d: %d\n", T, res);
	}
}
