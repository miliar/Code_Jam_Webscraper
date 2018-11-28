/*
 * Author: rush
 * Filename: B.cpp
 * Timestamp: 14/04/2012 13:25:24 CST
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#define OUT(x) cerr << #x << ": " << (x) << endl
#define SZ(x) ((int)x.size())
#define FOR(i, n) for (int i = 0; i < (n); ++i)
using namespace std;
typedef long long LL;

int gao1(int t) {
	int x = t / 3;
	if (t % 3 == 0 && x <= 10)
		return x;
	if (t % 3 == 1 && x + 1 <= 10)
		return x + 1;
	if (t % 3 == 2 && x + 1 <= 10)
		return x + 1;
	return -1;
}
int gao2(int t) {
	if (t < 2) return -1;
	int x = (t - 2) / 3;
	if (x + 2 <= 10) return x + 2;
	return -1;
}

int main() {
	int T, N, S, p, t[105];
	int dp[105][105];
	
	scanf("%d", &T);
	for (int id = 1; id <= T; ++id) {
		scanf("%d%d%d", &N, &S, &p);
		for (int i = 1; i <= N; ++i) scanf("%d", &t[i]);
		memset(dp, 0, sizeof(dp));
		for (int i = 1; i <= N; ++i) {
			for (int j = 0; j <= S; ++j) {
				dp[i][j] = dp[i - 1][j] + (gao1(t[i]) >= p);
				if (gao2(t[i]) != -1 && 0 <= j - 1) {
					dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + (gao2(t[i]) >= p));
				}
			}
		}
		printf("Case #%d: %d\n", id, dp[N][S]);
	}
	return 0;
}
