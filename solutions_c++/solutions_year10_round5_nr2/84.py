#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

typedef long long ll;

const ll INF = 1000000000000000005LL;
const int sINF = 999666111;


#define MAXDP 120000
int dp[MAXDP][2];

ll tsolve(int b[], ll l, int n, int di)
{
	for (int i = 0; i < MAXDP; i++) {
		dp[i][0] = sINF;
		dp[i][1] = sINF;
	}
	dp[0][0] = dp[0][1] = 0;
	queue<int> q;
	q.push(0);
	int mod = b[di];
	while (!q.empty()) {
		int start = q.front();
		q.pop();
		for (int i = di + 1; i < n; i++) if (i != di) {
			int x = (start + b[i]) % mod;
			int y = (start + b[i]) / mod;
			if (dp[x][0] > dp[start][0] + 1 - y/* || (dp[x][0] == dp[start][0] + 1 && y > dp[x][1])*/) {
				//printf("add %d, updated dp with %d, old = %d\n", x, dp[start][0] + 1, dp[x][0]);
				dp[x][0] = dp[start][0] + 1 - y;
				dp[x][1] = y + dp[start][1];
				q.push(x);
			}
// 			printf("."); fflush(stdout);
			
			
		}
	}
	ll rem  = l % (ll) mod;
	ll div = l / (ll) mod;
	if (dp[rem][0] != sINF && dp[rem][1] <= div)
		return div + dp[rem][0];
	return INF;
}


void solve(void)
{
	int n;
	ll l;
	scanf("%lld%d", &l, &n);
	int b[120];
	for (int i = 0; i < n; i++)
		scanf("%d", &b[i]);
	sort(b, b + n);
	reverse(b, b+n);
	ll ans = INF;
	for (int i = 0; i < n; i++) {
		ans = min(ans, tsolve(b, l, n, i));
	}
	if (ans == INF) printf("IMPOSSIBLE\n");
	else printf("%lld\n", ans);
}


int main(void)
{
// 	freopen("b.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}
