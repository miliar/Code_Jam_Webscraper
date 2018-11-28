#include <cstdio>

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int N, K;
	    scanf("%d %d", &N, &K);
		bool ok = true;
		for (int i = 1; i <= N; ++i)
			if (!((K >> (i - 1)) & 1)) {
				ok = false;
				break;
			}
		printf("Case #%d: ", t);
		if (ok)
			printf("ON\n");
		else
			printf("OFF\n");

	}

	return 0;
}
