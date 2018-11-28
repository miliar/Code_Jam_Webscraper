#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
int n, m, I;
int a[109][30];
int key[109];
bool used[109];
int dp[1<<16][16];
int g[20][20];
bool cmp(int i, int j) {
	return a[i][I]<a[j][I];
}


bool check(int i, int j) {
	for (int k=0; k<m; ++k) if (a[i][k]>=a[j][k]) return false;
	return true;
}

int solve(int s, int p) {
	if (s==(1<<p)) return 1;
	if (dp[s][p]>=0) return dp[s][p];
	int ans = n;
	for (int i=0; i<n; ++i) if ( (s&(1<<i)) && i!=p) {
		if (g[p][i]) ans = min(solve(s^(1<<p), i), ans);
		else ans = min(solve(s^(1<<p), i)+1, ans);
	}
	return dp[s][p] = ans;
}


int main() {
	freopen("output.txt", "w", stdout);
	int cas, cass = 0;
	for (scanf("%d", &cas); cas--; ) {
		scanf("%d %d", &n, &m);
		for (int i=0; i<n; ++i)
		for (int j=0; j<m; ++j)
			scanf("%d", &a[i][j]);
		for (int i=0; i<n; ++i)
		for (int j=0; j<n; ++j)
			g[i][j] = check(i, j);
		int res = n;
		memset(dp, -1, sizeof(dp));
		for (int i=0; i<n; ++i) res = min(res, solve((1<<n)-1, i));
		printf("Case #%d: %d\n", ++cass, res);

	}
	return 0;
}