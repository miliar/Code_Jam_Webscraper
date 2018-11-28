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

const int maxn = 100, maxk = 25;

int n, k;
int price[maxn][maxk];
bool adj[maxn][maxn];
int yx[maxn];
bool vis[maxn];

bool isBelow(int i, int j) {
	REP(p, k)
		if (price[j][p] <= price[i][p])
			return false;
	return true;
}

bool dfs(int x) {
	if (vis[x]) return false;
	vis[x] = true;
	REP(y, n)
		if (adj[x][y] && (yx[y] == -1 || dfs(yx[y]))) {
			yx[y] = x;
			return true;
		}
	return false;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int ntests;
	scanf("%d", &ntests);
	FOR(test, 1, ntests) {
		scanf("%d%d", &n, &k);
		REP(i, n) REP(j, k)
			scanf("%d", &price[i][j]);
		REP(i, n) REP(j, n)
			adj[i][j] = isBelow(i, j);
		fill(yx, yx+n, -1);
		int res = n;
		REP(i, n) {
			fill(vis, vis+n, false);
			if (dfs(i)) --res;
		}
		printf("Case #%d: %d\n", test, res);
	}

	exit(0);
}
