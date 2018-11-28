#pragma comment(linker, "/stack:64000000")

#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <queue>

using namespace std;

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++)
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)(v).size()

typedef long long llong;

const int MAXN = 10000 + 10;
int dp[MAXN];
int D[MAXN], L[MAXN];

char* solve() {
	memset(dp, 0, sizeof(dp));
	int n;
	scanf("%d", &n);
	REP(i, n) {
		scanf("%d %d", &D[i], &L[i]);
	}
	int F;
	scanf("%d", &F);
	dp[0] = D[0];
	REP(i, n) {
		for (int j = i + 1; j < n; j++) {
			if (D[i] + dp[i] >= D[j]) {
				dp[j] = max(dp[j], min(D[j] - D[i], L[j]));
			}
		}
	}
	REP(i, n) {
		if (D[i] + dp[i] >= F) {
			return "YES";
		}
	}
	return "NO";
}

int main() {
#ifdef LOCAL
	freopen("A-large_round2.in", "r", stdin);
	freopen("A-large_output.out", "w", stdout);
#endif	
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		printf("Case #%d: %s\n", test, solve());
	}
	return 0;
}