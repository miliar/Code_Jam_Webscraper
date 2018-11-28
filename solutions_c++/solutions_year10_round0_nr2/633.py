#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


typedef unsigned long long ll;


ll gcd(ll a, ll b) {
    return b==0? a : gcd(b, a%b);
}

int main() {
	freopen("problem.in", "r", stdin);
	freopen("problem.out", "w", stdout);
	int T;
	scanf("%d", &T);
    int n;
    ll val[1024];
    for (int tid=1; tid<=T; ++tid) {
        scanf("%d", &n);
        for (int i=0; i<n; ++i) scanf("%lld", val+i);
        sort(val, val+n);
        ll res = val[1]-val[0];
        for (int i=2; i<n; ++i)
            res = gcd(res, val[i]-val[0]);
        ll target = (val[0] + res - 1)/ res;
        ll ans = target * res - val[0];
        
        printf("Case #%d: %lld\n", tid, ans);
		
	}
	return 0;
}
