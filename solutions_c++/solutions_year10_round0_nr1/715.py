#include <stdio.h>

int main() {
	int prob = 0;
	int tn;
	int n, k;
	for (scanf("%d", &tn); tn--; ) {
		scanf("%d%d", &n, &k);
		int ml = (1 << n) - 1;
		printf("Case #%d: ", ++prob);
		printf("%s\n", k % (1 << n) == ml ? "ON" : "OFF");
	}
	return 0;
}

