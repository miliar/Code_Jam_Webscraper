#include <stdio.h>

int main() {
	int tc, n, k;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		scanf("%d %d", &n, &k);
		if ((k & ((1<<n)-1)) == ((1<<n)-1))
			puts("ON");
		else
			puts("OFF");
	}
	return 0;
}
