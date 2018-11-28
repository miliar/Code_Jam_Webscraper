#include <cstdio>


void solve() {
	int N, S, p; scanf("%d%d%d", &N, &S, &p);

	int ans = 0;
	for (int i = 0; i < N; i++) {
		int x; scanf("%d", &x);
		
		int a = (x + 2) / 3;
		int b = (x + 4) / 3;

		if (a >= p) ans++;
		else if (b >= p && S && x >= 2) ans++, S--;
	}

	printf("%d\n", ans);
}

int main() {
	int T; scanf("%d", &T);

	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
