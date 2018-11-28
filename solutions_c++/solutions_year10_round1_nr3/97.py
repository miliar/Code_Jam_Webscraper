#include <cstdio>

#define min(a, b) ((a) < (b) ? (a) : (b))
#define max(a, b) ((a) > (b) ? (a) : (b))

int T, A1[101], A2[101], B1[101], B2[101];
long long res[101];

int gcd(int a, int b) {
	if (a == 0) return b;
	return gcd(b % a, a);
}

int win(int a, int b) {
	if (a < b) return win(b, a);
	if (a == b) return 0;

	if (a >= 2 * b) {
		return 1;
	}
	return 1 - win(b, a - b);
}

int main() {
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);


	scanf("%d", &T);
	for (int q = 1; q <= T; q++) {
		scanf("%d %d %d %d", &A1[q], &A2[q], &B1[q], &B2[q]); 

		}


	int mn = 1;
	for (int i = 1; i <= 1000000; i++) {
			while (!win(i, mn)) {
				mn++;
			}

		for (int j = 1; j <= T; j++) {
			if (i >= A1[j] && i <= A2[j]) {
				res[j] += max(0, B2[j] - max(mn, B1[j]) + 1);
			}
			if (i >= B1[j] && i <= B2[j]) {
				res[j] += max(0, A2[j] - max(mn, A1[j]) + 1);
			}
		}
	}

	for (int q = 1; q <= T; q++) {
		printf("Case #%d: %lld\n", q, res[q]);
	}

	return 0;
}

