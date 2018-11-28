#include <stdio.h>
int main() {
	int ca, cases = 0;
	int n, i, k;
	scanf("%d", &ca);
	while (ca--) {
		scanf("%d%d", &n, &k);
		printf("Case #%d: %s\n", ++cases, ((((k % (1<<n)) + 1) % (1<<n)) == 0)? "ON":"OFF");
	}
	return 0;
}