#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cstdlib>
#include <cstdio>
#include <stack>
#include <map>
#include <cmath>
#include <ctime>
#include <memory.h>
#include <fstream>
#include <cassert>
using namespace std;
 
#ifdef MYDEBUG
#pragma comment(linker, "/stack:1000000000")
#endif

typedef pair<int, int> PII;
typedef long long LL;
typedef unsigned long long ULL;
 
#define MAX(a, b) ((a >= b) ? a : b)
#define MIN(a, b) ((a <= b) ? a : b)
#define ABS(a) ((a < 0) ? -(a) : a)
#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define sz size()
#define mp make_pair
#define pb push_back
#define HAS(S, v) ((S).find(v) != (S).end())
#define ALL(a) a.begin(), a.end()
#define RALL(a) a.rbegin(), a.rend()
#define CLR(a, b) memset(a, b, sizeof(a))
#define sqr(a) ((a) * (a))
#define V(t) vector<t>
#define VV(t) V(V(t))

V(int) D, L;
int dis;
int dp[10 * 1000 + 10];
int R(int v) {
	int &r = dp[v];
	if (r != -1) return r;
	if (v == 0) return r = D[0];
	int best = 0;
	FOR (i, 0, v)
		if (D[i] + R(i) >= D[v]) {
			int d = MIN(L[v], D[v] - D[i]);
			best = MAX(best, d);
		}
	return r = best;
}
bool solve() {
	int n = D.sz;
	FOR (i, 0, n)
		if (D[i] + R(i) >= dis)
			return true;
	return false;
}
int main() {
#ifdef MYDEBUG
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    clock_t beg = clock();
#endif

	int T;
	scanf("%d", &T);
	FOR (t, 0, T) {
		printf("Case #%d: ", t + 1);
		D.clear();
		L.clear();
		CLR(dp, -1);
		int n;
		scanf("%d", &n);
		D.resize(n);
		L.resize(n);
		FOR (i, 0, n)
			scanf("%d %d", &D[i], &L[i]);
		scanf("%d", &dis);
		if (solve()) printf("YES\n");
		else printf("NO\n");
	}

#ifdef MYDEBUG
    fprintf(stderr, "*** Total time: %.3lf ***\n", 1.0 * (clock() - beg) / CLOCKS_PER_SEC);
#endif
	return 0;
}
