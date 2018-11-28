#include <iostream>
#include <cstdio>

using namespace std;

typedef long long ll;

ll ps[1000000];
int prime[1000010];

int main() {
	int T;
	cin >> T;
	int p = 0;
	for(int i = 2; i <= 1000000; ++i) if(!prime[i]) {
		ps[p++] = i;
		for(int j = 2 * i; j <= 1000000; j += i) prime[j] = 1;
	}
	for(int t = 1; t <= T; ++t) {
		ll n;
		cin >> n;
		ll res = 0;
		for(int i = 0; i < p && ps[i] * ps[i] <= n; ++i) {
			++res;
			for(ll j = ps[i] * ps[i]; j <= n / ps[i]; j *= ps[i]) ++res;
		}
		if(n != 1) ++res;
		printf("Case #%d: ", t);
		cout << res << endl;
	}
	return 0;
}
