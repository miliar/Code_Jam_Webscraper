#include <cstdio>

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T, N, K;

	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		scanf("%d %d", &N, &K);

		printf("Case #%d: ", i);

		if (K % (1<<N) == (1<<N) - 1) {
			puts("ON");
		} else {
			puts("OFF");
		}
	}

}
