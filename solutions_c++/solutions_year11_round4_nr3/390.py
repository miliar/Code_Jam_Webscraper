#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;
typedef long long ll;
const ll maxn = 1000001;
ll flag[maxn];
vector<ll> primer;

void generate() {
	for (ll i = 0; i < maxn; i++)
		flag[i] = 1;
	for (ll i = 2; i < maxn; i++) if (flag[i]) {
		primer.push_back(i);
		for (ll j = i * 2; j < maxn; j += i)
			flag[j]  = 0;
	}
//	printf("%lld\n", primer.size());
}

ll gcd(ll m, ll n) {
	if (n == 0) return m;
	else return gcd(n, m % n);
}

ll cal(ll n) {
	if (n == 1)
		return 0;
	ll res = 1;
	for (ll i = 0; i < primer.size(); i++) 
		if (n >= primer[i]) {
			ll t = n / primer[i] / primer[i];
			while (t) {
				res++;
				t /= primer[i];
			}
		}else
			break;
	return res;

}

int main() {
	generate();
/*
	for (ll i = 1; i < 100; i++)
		printf("%lld = %lld\n", i, cal(i));
 */
	ll T = 0;
	scanf("%lld", &T);
	for (ll k = 1; k <= T; k++) {
		ll t;
		scanf("%lld", &t);
		printf("Case #%lld: %lld\n", k, cal(t));
	}
	return 0;
}
