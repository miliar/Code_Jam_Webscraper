#include <cstdio>

int main() {
	int t, n, k;
	scanf("%d", &t);
	for (int kase = 0; kase < t; ++kase) {
		scanf("%d%d", &n, &k);
		int ans = 1;
		while (n != 0) {			
			if ((k & 1) != 1) {
				ans = 0;
				break;
			} else {
				k >>= 1;
				n --;
			}
		}
		printf("Case #%d: %s\n", kase + 1, ans ? "ON" : "OFF");
	}
	return 0;
}

