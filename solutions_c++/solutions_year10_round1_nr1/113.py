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

int n, k;
char a[64][64], t[64][64];

int dx[] = {0, 1, 1, 1};
int dy[] = {1, 0, 1, -1};

bool check(int y, int x, char c) {
	FOR(d, 0, 4) {
		bool ok = true;
		FOR(i, 0, k) {
			int yy = y+i*dy[d];
			int xx = x+i*dx[d];
			if (yy < 0 || yy >=n || xx < 0 || xx >= n) {
				ok = false;
				break;
			}

			if (t[yy][xx] !=c) {
				ok = false;
				break;
			}
		}
		if (ok) return true;
	}
	return false;
}

string solve() {
	cin >> n >> k;
	FI cin >> a[i];
	REP(y, n) REP(x, n) t[x][n-1-y] = a[y][x];

	REP(s, n) FORD(y, n-1, 1) REP(x, n) {
		if (t[y][x] == '.') {
			t[y][x] = t[y-1][x];
			t[y-1][x] = '.';
		}
	}

	bool red = false, blue = false;
	FI FJ {
		if (!red && check(i, j, 'R')) red = true;
		if (!blue && check(i, j, 'B')) blue = true;
	}

	if(red && blue) return "Both";
	if (red) return "Red";
	if (blue) return "Blue";

	return "Neither";
}


int main() {
freopen("A-large.in", "rt", stdin);
freopen("A-large.out", "w", stdout);


	int tests;
	cin >> tests;
	FORE(T, 1, tests) {
		string res = solve();
		printf("Case #%d: %s\n", T, res.c_str());
	}
}
