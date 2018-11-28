using namespace std;

#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>
#define FOR(i,a,n) for(LL i=a; i<n; i++)
#define REP(i,n) FOR(i,0,n)
#define MAX 35001
#define GI ({LL _; scanf("%Ld", &_);_;})
#define LINF (1LL<<60)
#define sz size()
#define pb push_back
#define mkp make_pair
#define eps 1e-15
#define DINF 1e100
typedef long long LL;
typedef vector<int> VI;


LL n, a[101];
LL dp[MAX];
LL cur;

bool ok(LL diff) {
	for(int i = n-1;i>=0;i--) if(diff % a[i] == 0) {
		cur = diff / a[i];
		return true;
	}
	cur = -1;
	return false;
}
int main() {
	LL kases = GI+1;	
	FOR(kase, 1, kases) {
		LL big;
		cin >> big >> n;
		REP(j,MAX) dp[j] = LINF;

		REP(i,n) a[i] = GI;
		sort(a,a+n);
		//if(kase == 1) continue;
		dp[0] = 0LL;
		LL ans = big+1, mx=a[0];

		REP(i,n) {
		mx = max(a[i],mx);
			for(LL j = a[i]; j < MAX && j <= big; j++) {
				dp[j] = min(dp[j-a[i]]+1, dp[j]);
				if(dp[j] < LINF && ok(big-j)) {
					ans = min(ans, dp[j] + cur);

				}
				if(big % j == 0 && dp[j] < ans) {
					ans = min(ans, (big/j) * dp[j]);
				}
			}
		}	
		/*

		REP(j,MAX) dp[j] = LINF;
		dp[0] = 0LL;

		REP(i,n) {
			for(LL j = a[i]; j < MAX && j <= big; j++) {
				dp[j] = min(dp[j-a[i]]+1, dp[j]);
				if(dp[j] < LINF && ok(big-j)) {
					if(dp[j] + cur == ans && mx != (big-j)/cur) {
						cout << j <<" "<< big-j <<" " << dp[j] <<" + " << cur << " = " << dp[j]+cur << " (" << (big-j)/cur<<") "<<endl;

					}
				}
				if(big % j == 0 && dp[j] < ans && (big/j) * dp[j] == ans) {
				cout << big <<"/"<<j<<"*"<<dp[j] <<" = " << (big/j)*dp[j] <<endl;
					
				}
			}
		}	
		*/
		if(ans > big)
			printf("Case #%d: IMPOSSIBLE\n", kase);
		else {
			printf("Case #%d: ", kase);
			cout << ans << endl;
		}
	}
}
