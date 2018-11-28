#include <cstdlib>
#include <cstring>
#include <memory>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define NEED_BIG_INT 0
#define DEBUG_FLAG 1

#if NEED_BIG_INT
#include <gmpxx.h>
typedef mpz_class bint;
typedef mpq_class brational;
typedef mpf_class bdecimal;
// compile with -lgmpxx -lgmp (may need -lm too)
#endif

#if DEBUG_FLAG
#define dbg(...) cerr << #__VA_ARGS__ << ": " << __VA_ARGS__ << endl
#define cdbg(...) cerr << __VA_ARGS__ << endl
#else
#define debug(r)
#define dbg(...)
#endif

const int inf = 1000000000;
int N;
int M[1024];
int p[10][512];
int dp[10][10][512];

int f(int l, int b, int n) {
	if (l == -1 && b < N-M[n]) return inf;
	else if (l == -1) return 0;
	if (dp[l][b][n] != -1) return dp[l][b][n];
	return dp[l][b][n] = min(inf, min(f(l-1, b, n+n) + f(l-1, b, n+n+1), p[l][n] + f(l-1, b+1, n+n) + f(l-1, b+1, n+n+1)));
}

int main() {
	//string fname = "B-small-attempt0";
	string fname = "B-large";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int CASES;
	scanf("%d", &CASES);
	for (int CASE = 1; CASE <= CASES; ++CASE) {
		scanf("%d", &N);
		for (int i = 0; i < (1<<N); ++i)
			scanf("%d", &M[i]);
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < (1 << (N-i-1)); ++j)
				scanf("%d", &p[i][j]);
		memset(dp, -1, sizeof(dp));
		printf("Case #%d: %d\n", CASE, f(N-1, 0, 0));
	}

	return 0;
}
