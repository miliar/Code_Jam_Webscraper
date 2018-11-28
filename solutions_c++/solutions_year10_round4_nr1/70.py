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

bool match(char c1, char c2) {
	return c1 == '.' || c2 == '.' || c1 == c2;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int ntests;
	scanf("%d", &ntests);
	FOR(test, 1, ntests) {
		printf("Case #%d: ", test);
		int n;
		scanf("%d", &n);
		vector<string> field(2*n-1, string(2*n-1, '.'));
		vector<int> dleft(2*n-1), dright(2*n-1);
		int L = n-1, R = n-1;
		REP(i, n) {
			dleft[i] = L--;
			dright[i] = R++;
		}
		L += 2; R -= 2;
		FOR(i, n, 2*n-2) {
			dleft[i] = L++;
			dright[i] = R--;
		}

		REP(i, 2*n-1) 
			for (int j = dleft[i]; j <= dright[i]; j += 2)
				scanf(" %c", &field[i][j]);

		vector<bool> hor(2*n-1), vert(2*n-1);
		REP(i, 2*n-1) {
			hor[i] = true;
			for (int i1 = i-1, i2 = i+1; i1 >= 0 && i2 < 2*n-1; --i1, ++i2) {
				REP(j, 2*n-1) 
					if (!match(field[i1][j], field[i2][j]))
						hor[i] = false;
			}
		}
		REP(j, 2*n-1) {
			vert[j] = true;
			for (int j1 = j-1, j2 = j+1; j1 >= 0 && j2 < 2*n-1; --j1, ++j2) {
				REP(i, 2*n-1)
					if (!match(field[i][j1], field[i][j2]))
						vert[j] = false;
			}
		}

		int res = INT_MAX;
		REP(i, 2*n-1) REP(j, 2*n-1)
			if (hor[i] && vert[j]) {
				int m = 0;
				REP(k, 2*n-1) {
					remax(m, abs(i-k)+abs(j-dleft[k])+1);
					remax(m, abs(i-k)+abs(j-dright[k])+1);
				}
				remin(res, sqr(m)-sqr(n));
			}
		printf("%d\n", res);
	}
}
