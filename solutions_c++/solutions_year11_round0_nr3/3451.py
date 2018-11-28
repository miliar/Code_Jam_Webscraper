#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int nTests;
	scanf("%d", &nTests);
	for (int test = 1; test <= nTests; ++test) {
		int n;
		scanf("%d", &n);
		int SUM = 0;
		int MIN = 1e6;
		int XOR = 0;
		for (int i = 1; i <= n; ++i) {
			int x;
			scanf("%d", &x);
			SUM += x;
			XOR ^= x;
			MIN = min(MIN, x);
		}
		printf("Case #%d: ", test);
		if (XOR == 0) {
			printf("%d\n", SUM - MIN);
		} else {
			printf("NO\n");
		}
	}
	return 0;
}
