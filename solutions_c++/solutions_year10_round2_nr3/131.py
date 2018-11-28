#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cassert>
#include <queue>
#include <set>
#include <map>
#include <string>
using namespace std;
typedef vector<int> vint;
typedef long long lint;
typedef pair<int, int> pii;
#define pb push_back
#define mp make_pair
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()

int dp[555][555];
int visited[555][555];
const int MOD = 100003;


int C[555][555];

void initC() {
	for(int i = 0; i < 555; ++i) {
		C[i][0] = 1;
	}
	for(int n = 1; n < 555; ++n) {
		for(int k = 1; k <= n; ++k) {
			C[n][k] = (C[n - 1][k] + C[n - 1][k - 1]) % MOD;
		}
	}
}

int Pure(int x, int pos) {
	if(visited[x][pos])
		return dp[x][pos];
	visited[x][pos] = 1;
	if(pos >= x) {
		return dp[x][pos] = 0;
	}
	if(pos == 1) {
		return dp[x][pos] = 1;
	}
	dp[x][pos] = 0;
	for(int i = 1; i <= pos - 1; ++i) {
		/*if(x - pos >= pos - i)
			dp[x][pos] += Pure(pos, i);*/
		int between = x - pos - 1;
		int places = pos - i - 1;
		if(places > between)
			continue;
		dp[x][pos] += (lint)C[between][places] * Pure(pos, i) % MOD;
		dp[x][pos] %= MOD;
	}
	return dp[x][pos];
}

void Solve(int test) {
	int n;
	scanf("%d", &n);
	int ans = 0;
	for(int i = 1; i <= n - 1; ++i) {
		ans += Pure(n, i);
		ans %= MOD;
	}
	printf("Case #%d: %d\n", test, ans);
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
#endif
	initC();
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i)
		Solve(i);
	return 0;
}