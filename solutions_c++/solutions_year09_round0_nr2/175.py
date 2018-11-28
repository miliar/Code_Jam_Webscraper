#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#include <memory.h>
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

int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};

typedef pair<int, int> PI;
typedef vector<PI> VPI;

int bd[100][100];
char cd[100][100];
VPI d[100][100];
int w, h;


void go(int r, int c, char let) {
	cd[r][c] = let;
	FIR(d[r][c].size()) {
		PI p = d[r][c][i];
		go(p.first, p.second, let);
	}
}

char mapping[500];

void solve() {
	cin >> h >> w;
	REP(r, h) REP(c, w) cin >> bd[r][c];
	FIR(100) FJR(100) d[i][j].clear();
	memset(cd, 0, sizeof cd);

	REP(r, h) REP(c, w) {
		int rr=r, cc = c;
		FIR(4) {
			int nr = r + dr[i], nc = c + dc[i];
			if (nr < 0 || nc < 0 || nr >= h || nc >= w) continue;
			if (bd[nr][nc] < bd[rr][cc]) rr = nr, cc = nc;
		}

		if (rr != r || cc != c) 
			d[rr][cc].push_back(PI(r, c));
		else 
			cd[r][c] = 1;
	}

	char let = 'a';
	REP(r, h) REP(c, w) if (cd[r][c] == 1) {
		go(r, c, let);
		++let;
	}

	memset(mapping, 0, sizeof mapping);
	let = 'a';
	REP(r, h) REP(c, w) if (!mapping[ cd[r][c] ]) {
		mapping[ cd[r][c] ] = let++;
	}

	REP(r, h) {
		REP(c, w) printf("%c ", mapping[ cd[r][c] ] ); 
		printf("\n");
	}

}

int main( int argc, char* argv[] ) {
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "w", stdout);

	int cases;
	cin >> cases;
	FORE(i, 1, cases) {
		printf("Case #%d:\n", i);
		solve();
	}
}