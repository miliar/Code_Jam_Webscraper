#include <stdio.h>
#include <algorithm>
using namespace std;

int solve() {
	int N;
	scanf("%d", &N);
	int xmin = 10000000, xxor = 0, xsum = 0;
	for (int i = 0; i < N; i++) {
		int x; scanf("%d", &x);
		xxor ^= x;
		xmin = min(x, xmin);
		xsum += x;
	}
	if (xxor) return -1;
	return xsum - xmin;
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		int result = solve();
		if (result < 0) {
			printf("Case #%d: NO\n", i);
		} else {
			printf("Case #%d: %d\n", i, result);
		}
	}
	return 0;
}
