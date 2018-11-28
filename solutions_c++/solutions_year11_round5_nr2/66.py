#include <cstdio>

#define N 10001

int T, n, fre[N + 1], x, a, b, ans;

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d:", r);
		for (int i = 0; i <= N; ++i)
			fre[i] = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d", &x), ++fre[x];
		if (n < 2) {
			printf(" %d\n", n);
			continue;
		}
		b = 0;
		ans = N;
		for (a = 0; a < N; ++a) if (fre[a]) {
			if (a < b) b = a;
			while (b < N && fre[b] <= fre[b + 1])
				++b;
			if (b - a + 1 < ans)
				ans = b - a + 1;
			for (int i = a; i <= b; ++i)
				--fre[i];
			--a;
		}
		printf(" %d\n", ans);
	}
	return 0;
}
