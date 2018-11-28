#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    for (int line = 1; line <= t; line++) {
	int n, k;
	scanf("%d %d", &n, &k);

	int mask = (1 << n) - 1;
	printf("Case #%d: ", line);
	if ((k & mask) == mask) printf("ON\n");
	else printf("OFF\n");
    }
}
