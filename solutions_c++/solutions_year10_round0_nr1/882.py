#include <stdio.h>

int main() {
	int _42, T;
	scanf(" %d", &T);
	for (int _42=1; _42 <= T; _42++) {
		printf("Case #%d: ", _42);

		int N, K;
		scanf(" %d %d", &N, &K);
		int snaps = (1 << N) - 1;
		if (K < snaps) printf("OFF\n");
		else if (K == snaps) printf("ON\n");
		else { // K > snaps
			if ((K-snaps) % (snaps+1) == 0) printf("ON\n");
			else printf("OFF\n");
		}
	}
	return 0;
}
