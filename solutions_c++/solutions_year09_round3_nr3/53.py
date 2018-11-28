#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
const int N = 109;
int dp[N][N];
int n, m, pos[N];
int res(int l, int r) {
	if (l>=r) return 0;
	if (dp[l][r]>=0) return dp[l][r];
	int ans = 0xfffffff;
	for (int i=l; i<r; ++i) {
		ans = min(ans, res(l, i) + res(i+1, r) + pos[r+1]-pos[l]-2 );
	}
	return dp[l][r] = ans;
}

int main() {
	int cas, cass=0;
	for (scanf("%d", &cas); cas--; ) {
		printf("Case #%d: ", ++cass);
		scanf("%d %d", &m, &n);
		for (int i=1; i<=n;++i) scanf("%d", &pos[i]);
		pos[0] = 0;
		pos[n+1] = m+1;
		memset(dp, -1, sizeof(dp));
		printf("%d\n", res(0, n));
	}
	return 0;
	
}
				
