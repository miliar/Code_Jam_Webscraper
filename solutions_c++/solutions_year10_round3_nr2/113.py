#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int main() {
	int t, tc = 0;
	freopen("E://in.txt", "r", stdin);
	freopen("E://out.txt", "w", stdout);
	scanf("%d", &t);
	while(t--) {
		long long l, p, c;
		scanf("%lld%lld%lld", &l, &p, &c);
		int ans = 0;
		while(l * c < p) {
			c = c * c;
			ans++;
		}
		printf("Case #%d: %d\n", ++tc, ans);
	}
	return 0;
}