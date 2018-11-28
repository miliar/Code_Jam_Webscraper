#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int T, idx = 0; scanf("%d", &T);
	while (T--) {
		int n; scanf("%d", &n);
		long long ans = 0;
		long long x[n], y[n];
		for (int i = 0; i < n; ++i) scanf("%lld", x+i);
		for (int i = 0; i < n; ++i) scanf("%lld", y+i);
		sort(x, x+n);
		sort(y, y+n);
		for (int i = 0; i < n; ++i)
			ans += x[i]*y[n-i-1];
		printf("Case #%d: %lld\n", ++idx, ans);
	}
	return 0;
}
