#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <numeric>
#include <cctype>
#include <climits>
#include <cassert>
using namespace std;

typedef long long int64; 
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return int(c.size()); }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }
template<typename T> bool remin(T& x, T y) { if (x <= y) return false; x = y; return true; }
template<typename T> bool remax(T& x, T y) { if (x >= y) return false; x = y; return true; }

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n) - 1); i >= 0; --i)

bool a[101][101], b[101][101];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int ntests;
	scanf("%d", &ntests);
	FOR(test, 1, ntests) {
		printf("Case #%d: ", test);
		int r;
		scanf("%d", &r);
		memset(a, 0, sizeof(a));
		REP(z, r) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			FOR(i, x1, x2) FOR(j, y1, y2) a[i][j] = true;
		}
		int res = -1;
		for (;;) {
			++res;
			memset(b, 0, sizeof(b));
			bool doBreak = true;
			FOR(i, 1, 100) FOR(j, 1, 100)
				if (a[i][j]) {
					doBreak = false;
					if (a[i-1][j] || a[i][j-1]) b[i][j] = true;
				} else {
					if (a[i-1][j] && a[i][j-1]) b[i][j] = true;
				}
			if (doBreak) break;
			memcpy(a, b, sizeof(a));
		}
		printf("%d\n", res);
	}
}
