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

int m, want, a, b;
int v[500000], change[56000];
int f[500000][2];
#define INF 10000000

int val(int pos, int p1, int p2) {
	if (v[pos]) return p1 & p2;
	return p1 | p2;
}

int val2(int pos, int p1, int p2) {
	if (v[pos]) return p1 | p2;
	return p1 & p2;
}

void go(int pos) {
	if (pos > a) {
		f[pos][v[pos]] = 0;
		return;
	}

	int left = 2*pos;
	int right = left+1;
	go(left); go(right);
	
	int zero = INF, one = INF;
	FOR(t1, 0, 2) FOR(t2, 0, 2) {
		int k = val(pos, t1, t2);
		f[pos][k] = min(f[pos][k], f[left][t1] + f[right][t2]);
	}

	if(change[pos]) {
		FOR(t1, 0, 2) FOR(t2, 0, 2) {
			int k = val2(pos, t1, t2);
			f[pos][k] = min(f[pos][k], f[left][t1] + f[right][t2] + 1);
		}
	}
}

struct Task {
	
	void input() {
		scanf("%d %d", &m, &want);
		a = (m-1)/2;
		b = a + (m+1)/2;
		FORE(i, 1, a) scanf("%d %d", &v[i], &change[i]);
		FORE(i, a + 1, b) scanf("%d", &v[i]);
		FORE(i, 1, b) f[i][0] = f[i][1] = INF;
	}



	int solve() {
		go(1);
		return f[1][want];		
	}
};

int main() {
freopen("A-large.in", "rt", stdin);
freopen("A-large.out", "w", stdout);

	int tc; cin >>tc;
	REP(TC, tc) {
		Task t;
		t.input();
		int res = t.solve();
		if (res >= INF)
			printf("Case #%d: IMPOSSIBLE\n", TC+1, res);
		else
			printf("Case #%d: %d\n", TC+1, res);
	}

fclose(stdout);
}
