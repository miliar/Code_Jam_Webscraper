#include <iostream>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int test, n, k;
	scanf("%d", &test);
	for (int testID = 0;testID < test;testID++) {
		scanf("%d %d", &n, &k);
		bool can = true;
		for (int i = 1;i <= n;i++) {
			long long s = (1ll << i), m = k % s;
			if (m < s / 2) {
				can = false;
				break;
			}
		}
		if (can) {
			printf("Case #%d: ON\n", testID + 1);
		}
		else {
			printf("Case #%d: OFF\n", testID + 1);
		}
	}
	return 0;
}