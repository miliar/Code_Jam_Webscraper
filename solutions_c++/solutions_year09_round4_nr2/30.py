#define _CRT_SECURE_NO_WARNINGS
#include <map> 
#include <set> 
#include <cmath> 
#include <queue> 
#include <vector> 
#include <string> 
#include <cstdio> 
#include <cstdlib> 
#include <climits> 
#include <cstring> 
#include <cassert> 
#include <numeric> 
#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include "float.h" 
#include <ctime> 
using namespace std; 

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

const int inf = 100000000;

int r, c, f;
char a[50][51];
int d[50][50][50][2];

void digdig(int i, int j, int cd) {	
	int j1 = j, j2 = j;
	while (j1-1 >= 0 && a[i][j1-1] == '.' && a[i+1][j1-1] == '#') 
		--j1;
	while (j2+1 < c && a[i][j2+1] == '.' && a[i+1][j2+1] == '#')
		++j2;
	if (j1-1 >= 0 && a[i][j1-1] == '.') {
		int ni = i+1;
		while (ni+1 < r && a[ni+1][j1-1] == '.')
			++ni;
		if (ni-i <= f) 
			remin(d[ni][j1-1][j1-1][0], cd);
	}
	if (j2+1 < c && a[i][j2+1] == '.') {
		int ni = i+1;
		while (ni+1 < r && a[ni+1][j2+1] == '.')
			++ni;
		if (ni-i <= f)
			remin(d[ni][j2+1][j2+1][0], cd);
	}
	if (j1 < j2) {
		FOR(j, j1, j2) {
			int ni = i+1;
			while (ni+1 < r && a[ni+1][j] == '.')
				++ni;
			if (ni-i <= f)
				remin(d[ni][j][j][0], cd+1);
		}
	}
	if (i+2 < r)
		FOR(nj1, j1, j2) FOR(nj2, nj1, j2) {
			if (nj1 > j1) {
				if (a[i+2][nj1] == '#')
					remin(d[i+1][nj1][nj2][0], cd+(nj2-nj1+1));
			}
			if (nj2 < j2) {
				if (a[i+2][nj2] == '#')
					remin(d[i+1][nj1][nj2][1], cd+(nj2-nj1+1));
			}
		}
}

void digdigdig(int i, int j1, int j2, int side) {
	vector<char> sav(j2-j1+1);
	FOR(j, j1, j2) {
		sav[j-j1] = a[i][j];
		a[i][j] = '.';
	}
	digdig(i, side == 0 ? j1 : j2, d[i][j1][j2][side]);
	FOR(j, j1, j2) 
		a[i][j] = sav[j-j1];
}

int solve() {
	REP(i, r) REP(j1, c) FOR(j2, j1, c-1) REP(side, 2)
		d[i][j1][j2][side] = inf;
	d[0][0][0][0] = 0;
	int res = inf;
	REP(i, r) REP(j1, c) FOR(j2, j1, c-1) REP(side, 2) {
		if (d[i][j1][j2][side] < inf)
			if (i == r-1) remin(res, d[i][j1][j2][side]);
			else digdigdig(i, j1, j2, side);
	}
	return res;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int ntests;
	scanf("%d", &ntests);
	FOR(test, 1, ntests) {
		scanf("%d%d%d", &r, &c, &f);
		REP(i, r) {
			scanf("%s", a[i]);
			assert((int)strlen(a[i]) == c);
		}
		int res = solve();
		printf("Case #%d: ", test);
		if (res >= inf) printf("No\n");
		else printf("Yes %d\n", res);
	}

	exit(0);
}
