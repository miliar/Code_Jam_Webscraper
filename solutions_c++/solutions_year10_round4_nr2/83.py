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

const int inf = 1000000000;
int n;
vector<int> M;
vector<vector<int> > C;
vector<vector<vector<int> > > dp;

int solve(int i, int j, int k) {
	if (i == -1) 
		return k >= M[j] ? 0 : inf;
	while (size(dp[i][j]) < k+1) {
		int x = size(dp[i][j]);
		dp[i][j].push_back(inf);
		int t1 = solve(i-1, 2*j, x+1)+solve(i-1, 2*j+1, x+1)+C[i][j];
		int t2 = solve(i-1, 2*j, x)+solve(i-1, 2*j+1, x);
		remin(dp[i][j][x], min(t1, t2));
	}
	return dp[i][j][k];
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int ntests;
	scanf("%d", &ntests);
	FOR(test, 1, ntests) {
		printf("Case #%d: ", test);
		scanf("%d", &n);
		M.resize(1<<n);
		REP(i, 1<<n) {
			scanf("%d", &M[i]);
			M[i] = n-M[i];
		}
		C.resize(n);
		dp.clear();
		dp.resize(n);
		REP(i, n) {
			C[i].resize(1<<(n-1-i));
			dp[i].resize(1<<(n-1-i));
			REP(j, size(C[i])) scanf("%d", &C[i][j]);
		}
		printf("%d\n", solve(n-1, 0, 0));
	}
}
