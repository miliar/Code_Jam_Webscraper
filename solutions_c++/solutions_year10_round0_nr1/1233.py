#include <cstdio>

int t, n, k, d, it;

int main() {
	scanf("%d", &t);
	for(it = 1; it <= t; ++it) {
		scanf("%d%d", &n, &k);
		d = (1 << n) - 1;
		printf("Case #%d: ", it);
		if(k - d >= 0 && (k - d) % (d + 1) == 0) {
			puts("ON");
		} else {
			puts("OFF");
		}
	}
	return 0; }
