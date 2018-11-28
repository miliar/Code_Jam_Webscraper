#include <stdio.h>

int main() {
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		int N, L, H;
		scanf("%d%d%d", &N, &L, &H);
		int f[10000];
		for (int i = 0; i < N; i++) {
			scanf("%d", &f[i]);
		}

		int valid = -1;
		for (valid = L; valid <= H; valid++) {
			bool found = true;
			for (int j = 0; j < N; j++) {
				if ((valid % f[j] != 0) && (f[j] % valid != 0)) {
					found = false;
				}
			}

			if (found) {
				break;
			}
		}

		if (valid <= H && valid >= L) {
			printf("Case #%d: %d\n", t, valid);
		} else {
			printf("Case #%d: NO\n", t);
		}

	}

	return 0;

	return 0;
}
