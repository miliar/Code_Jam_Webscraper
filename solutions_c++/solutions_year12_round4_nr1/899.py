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

#define GI(n) scanf("%d", &n)
#define GI2(n,m) scanf("%d %d", &n, &m)

int d[11000];
int len[11000];
int q[11000];
int n;

bool solve() {
	GI(n); FI GI2(d[i], len[i]);
	GI(d[n]); len[n] = 1;
	FORE(i, 0, n)  q[i] = 0;

	q[0] = d[0];
	FI FORE(j, i+1, n) {
		if (d[i] + q[i] >= d[j]) {
			q[j] = max(q[j], min(d[j] - d[i], len[j]));
		} else 
			break;
	}

	return q[n];

}

int main() {

//freopen("input.txt", "rt", stdin);
freopen("A-large.in", "rt", stdin);
freopen("A-large.out", "w", stdout);

	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		int res = solve();

		printf("Case #%d: ", tc);
		puts(res ? "YES" : "NO");
	}
}
