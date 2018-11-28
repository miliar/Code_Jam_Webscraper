#include <cstdio>

void Solve() {
	int A, B;
	scanf("%d %d", &A, &B);
	int ans = 0;
	for (int n = A; n < B; n++) {
		int pow10 = 1;
		for (; pow10 * 10 <= n; pow10 *= 10);
		int curr = n;
		while (1) {
			int lastDigit = curr % 10;
			curr = curr / 10 + lastDigit * pow10;
			if (curr == n) break;
			if (curr > n && curr <= B) ans++;
		}
	}
	printf("%d\n", ans);
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		printf("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}