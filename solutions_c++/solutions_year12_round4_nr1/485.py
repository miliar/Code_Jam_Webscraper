// Alex Fetisov

#include <cstdio>

void initf() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
}

#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <string>

using namespace std;

const int maxn = 10004;

typedef long long ll;

int n;
int len[maxn], dst[maxn];
int dp[maxn];

void solve() {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d%d", dst + i, len + i);
	}
	int target;
	scanf("%d", &target);
	ll curHeight = min(dst[0], len[0]);
	int frm = 0;
	dst[n+1] = target;
	dst[n+2] = 0;
	dp[0] = n+2;
	for (int i = 1; i <= n + 1; ++i) {
		dp[i] = 1000000;
		for (int j = 0; j < i; ++j) {
			if (dp[j] != 1000000) {
				ll cdst = min(dst[j] - dst[dp[j]], len[j]);
				if (dst[i] <= cdst + dst[j]) {
					dp[i] = min(dp[i], j);
				}
			}
		}
	}
	if (dp[n+1] != 1000000) {
		printf("YES\n");
	} else {
		printf("NO\n");
	}
	//while (1) {
	//	ll ndst = (ll)dst[frm] + curHeight;
	//	if (ndst >= target) {
	//		printf("YES\n");
	//		return;
	//	}
	//	int besti = -1;
	//	ll bestd = -1;
	//	for (int i = frm + 1; i < n; ++i) {
	//		if (dst[i] <= ndst) {
	//			ll calcHeight = min(dst[i] - dst[frm], len[i]);
	//			if (bestd < calcHeight + (ll)dst[i]) {
	//				bestd = calcHeight + (ll)dst[i];
	//				besti = i;
	//			}
	//		} else {
	//			break;
	//		}
	//	}
	//	if (besti == -1) {
	//		printf("NO\n");
	//		return;
	//	}
	//	curHeight = min(dst[besti] - dst[frm], len[besti]);
	//	frm = besti;
	//}
}

int main() {
	initf();
	int Test;
	scanf("%d", &Test);
	for (int i = 1; i <= Test; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}