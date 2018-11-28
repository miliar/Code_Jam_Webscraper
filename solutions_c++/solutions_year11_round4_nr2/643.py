#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cassert>
#include <memory.h>
#include <ctype.h>

#include <iostream>

#include <string>
#include <complex>
#include <numeric>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <sstream>

//#pragma comment(linker, "/stack:64000000")

using namespace std;

template<typename TYPE> inline TYPE sqr(const TYPE& a) { return (a) * (a); }

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))

typedef long long li;
typedef double ld;
typedef pair<int, int> pt;

const int INF = 1000 * 1000 * 1000;
const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 20;

int r, c, d;
int a[N][N];
int z[N][N];

bool check(int k) {
	for(int x = 0; x + k <= r; ++x) {
		for(int y = 0; y + k <= c; ++y) {
			int x1 = x + k - 1, y1 = y + k - 1;
			ld xc = x + k / 2.0, yc = y + k / 2.0;
			ld sx = 0, sy = 0;
			for(int i = y + 1; i < y1; ++i) {
				sx += (d + a[x][i]) * (x + 0.5 - xc);
				sy += (d + a[x][i]) * (i + 0.5 - yc);
				sx += (d + a[x1][i]) * (x1 + 0.5 - xc);
				sy += (d + a[x1][i]) * (i + 0.5 - yc);
			}
			for(int j = x + 1; j < x1; ++j) {
				for(int i = y; i <= y1; ++i) {
					sx += (d + a[j][i]) * (j + 0.5 - xc);
					sy += (d + a[j][i]) * (i + 0.5 - yc);
				}
			}
			if(fabs(sx) < EPS && fabs(sy) < EPS)
				return true;
		}
	}
	return false;
}

void solve(int it) {
	scanf("%d%d%d\n", &r, &c, &d);
	forn(i, r) {
		forn(j, c) {
			char c;
			scanf("%c", &c);
			a[i][j] = c - '0';
		}
		scanf("\n");
	}
	for(int k = min(r, c); k >= 3; --k) {
		if(check(k)) {
			printf("Case #%d: %d\n", it, k);
			return;
		}
	}
	printf("Case #%d: IMPOSSIBLE\n", it);
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

  	int test;
  	scanf("%d\n", &test);
  	for1(it, test) {
  		solve(it);
  	}

	return 0;
}
