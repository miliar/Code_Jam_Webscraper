#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
#include <queue>
#include <set>
#include <stack>
#include <list>

using namespace std;

//GyS Loves Algorithm
#define X first
#define Y second
#define all(x) x.begin(), x.end()
#define mk(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define rep(x, n) for (int x = 0; x < n; x++)
#define range(x, a, b)for (int x = a; x <= b; x++)
#define sz(x) x.size()
#define setv(x, y) memset(x, y, sizeof(x))
#define repi(it, x) for (typeof(x.begin()) it = x.begin(); it != x.end(); ++it)
#define pl() printf("\n")

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
int dp[10100];
int d[10100], l[10100];

int main()
{
	int T;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int cn = 1; cn <= T; cn++) {
		int n;
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) {
			scanf("%d%d", &d[i], &l[i]);
		}
		int D;
		scanf("%d", &D);
		memset(dp, 0, sizeof(dp));
		int ans;
		dp[1] = d[1] + d[1];
		ans = dp[1];
		for (int i = 2; i <= n; i++) {
			dp[i] = 0;
			for (int j = 1; j < i; j++) {
				if (dp[j] >= d[i]) {
					dp[i] = max(dp[i], d[i] + min(l[i], d[i] - d[j]));
				}
			}
			ans = max(ans, dp[i]);
		}
		printf("Case #%d: %s\n", cn, ans >= D ? "YES" : "NO");
	}
	return 0;
}
