#include <cstdio>

int t, n, k;

int main() {
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%d %d", &n, &k);
		bool ok = true;
		while (n) {
			if (k % 2 == 0) ok = false;
			k /= 2;
			n--;
		}
		printf("Case #%d: %s\n", i + 1, ok ? "ON" : "OFF");	
	}
	return 0;
}