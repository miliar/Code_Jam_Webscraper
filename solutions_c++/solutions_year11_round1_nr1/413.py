#include <cstdio>

typedef long long lint;

int main() {
	int ntests, pd, pg;
	lint n;
	scanf("%d", &ntests);
	
	for (int test = 1; test <= ntests; test++) {
		scanf("%lld %d %d", &n, &pd, &pg);
		
		bool possible = false;

		for (lint i = 1; i <= n; i++) {
			if ((100 % i == 0) && pd % (100 / i) == 0) {
				possible = true;
				break;
			}
		}
		
		if (possible) {
			if (pg == 0 && pd != 0) {
				possible = false;
			}
			
			if (pg == 100 && pd != 100) {
				possible = false;
			}
		}
		
		printf("Case #%d: ", test);
		if (possible) {
			puts("Possible");
		} else {
			puts("Broken");
		}
	}
	return 0;
}

