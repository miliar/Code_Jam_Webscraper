#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <map>
#include <queue>
#include <set>
#include <functional>

using namespace std;

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

typedef pair<int, int> PI;
typedef vector<PI> VPI;

LL a[1000], b[1000];

struct Task {
	int n;

	void input() {
		cin >> n;
		FI cin >> a[i];
		FI cin >> b[i];
	}
	LL solve() {
		sort(a,a+n); sort(b,b+n);
		LL res = 0;
		FI res += a[i] * b[n-1-i];
		return res;
	}
};

int main() {
freopen("A-large.in", "rt", stdin);
freopen("A-large.out", "w", stdout);

	int tc; cin >>tc;
	REP(TC, tc) {
		Task t;
		t.input();
		LL res = t.solve();
		printf("Case #%d: %lld\n", TC+1, res);
	}

fclose(stdout);
}
