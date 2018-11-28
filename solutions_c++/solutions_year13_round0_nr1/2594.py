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

char f[7][7];

bool eqc(int r, int c, char ch) {
	return f[r][c] == ch || f[r][c] == 'T';
}

bool check(char ch) {
	//rows
	REP(r, 4) {
		int cnt = 0;
		REP(c, 4) cnt += eqc(r, c, ch);
		if (cnt == 4)
			return true;
	}

	// cols
	REP(c, 4) {
		int cnt = 0;
		REP(r, 4) cnt += eqc(r, c, ch);
		if (cnt == 4)
			return true;
	}

	int cnt = 0;
	FIR(4) cnt += eqc(i, i, ch);
	if (cnt == 4)
		return true;

	cnt = 0;
	FIR(4) cnt += eqc(3-i, i, ch);
	if (cnt == 4)
		return true;

	return false;
}

bool isDone() {
	REP(r, 4) REP(c, 4)
		if (f[r][c] == '.')
			return false;
	return true;
}

char* solve() {
	FIR(4) scanf("%s", f[i]);
	if (check('X')) return "X won";
	if (check('O')) return "O won";

	if (isDone())
		return "Draw";

	return "Game has not completed";
}

int main() {
//freopen("input.txt", "rt", stdin);
freopen("A-large.in", "rt", stdin);
freopen("A-large.out", "w", stdout);

	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		printf("Case #%d: %s\n", tc, solve());
	}

}
