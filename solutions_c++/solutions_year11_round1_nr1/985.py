#include<iostream>
using namespace std;

typedef long long ll;

ll gcd(ll a, ll b){
	if(b == 0) return a;
	return gcd(b, a % b);
}

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for(int t = 0; t < cas; t++){
		ll n, pd, pg;
		scanf("%lld%lld%lld", &n, &pd, &pg);
		int tp = 100 / gcd(pd, 100);
		int tpp = 100 / gcd(pg, 100);
		if(n < tp || (pd != 100 && pg == 100) || (pd != 0 && pg == 0)) printf("Case #%d: Broken\n", t + 1);
		else printf("Case #%d: Possible\n", t + 1);
	}
	return 0;
}