#include <iostream>
#include <cstdio>

using namespace std;

typedef long long ll;

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int n, r = 0, a, mi = 10000000;
		ll res = 0;
		cin >> n;
		for(int i = 0; i < n; ++i) {
			cin >> a;
			res += a;
			r ^= a;
			mi = min(mi, a);
		}
		printf("Case #%d: ", t);
		if(r == 0) printf("%lld\n", res - mi);
		else puts("NO");
	}
	return 0;
}
