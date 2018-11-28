#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

#pragma warning(disable:4996)

typedef long long int64;
typedef int64 ll;


////////////////////////////////////////start///////////////////////////////////////////

const ll mod = 10007;
int W, H, R;
ll dp[110][110];
int direct[][2] = {{1, 2}, {2, 1}};

void solve(int tid) {
	for (int x=0; x<=H; ++x) for (int y=0; y<=W; ++y) {
		if (dp[x][y] == -1)
			continue;
		for(int i=0; i<2; ++i) {
			int pre_x = x - direct[i][0];
			int pre_y = y - direct[i][1];
			if (pre_x >= 1 && pre_y>=1 && dp[pre_x][pre_y] != -1) {
				dp[x][y] += dp[pre_x][pre_y];
				dp[x][y] %= mod;
			}
		}
		
	}
	printf("Case #%d: %lld\n", tid, dp[H][W]);
	
}

int main() {
	freopen("d:/input.in", "r", stdin);
	freopen("d:/output.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tid=1; tid<=T; ++tid) {
		scanf("%d %d %d", &H, &W, &R);
		memset(dp, 0, sizeof dp);
		for(int i=0; i<R; ++i) {
			int x, y;
			scanf("%d %d", &x, &y);
			dp[x][y] = -1;
		}
		dp[1][1] = 1;
		solve(tid);
	}
	return 0;
}