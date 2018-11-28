using namespace std;

#include <iostream>
#include <map>
#include <vector>
#include <cmath>
#include <queue>
#define FOR(i,a,n) for(int i=a; i<n; i++)
#define REP(i,n) FOR(i,0,n)
#define MAX 1000
#define GI ({int _; scanf("%d", &_);_;})
#define INF (LL)1e18
#define sz size()
#define pb push_back
#define mkp make_pair
#define eps 1e-15
#define DINF 1e100
typedef long long LL;

int main() {
	int kases = GI+1;
	LL n, k;
	FOR(kase, 1, kases) {
		n=GI, k=GI;
		LL dp[n];
		string ans = "OFF";
		dp[0] = 1;
		FOR(i,1,n) dp[i] = 2*dp[i-1] + 1;

		LL p = dp[n-1];
		if(p <= k) {
			LL num = k+1, den = p+1;
			if(num % den == 0) ans = "ON";
		}
		printf("Case #%d: %s\n", kase, ans.c_str());
	}
}
