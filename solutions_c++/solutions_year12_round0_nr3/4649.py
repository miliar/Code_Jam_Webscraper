#include <stdio.h>

static const int pow10[7] = {1, 10, 100, 1000, 10000, 100000, 1000000};

int N = 0;

int len(int a) {
	int res = 0;
	while (0 != a) {
		a /= 10;
		++res;
	}
	return res;
}

bool isPair(const int a, const int b) {
	int l = len(a);
	if (len(b) != l) {
		return false;
	}

	for (int i = 1; i < l; ++i) {
		int moda = a % pow10[i];
		int diva = a / pow10[i];
		int resa = moda * pow10[l - i] + diva;
		if (resa == b) {
			return true;
		}
	}

	return false;
}

int solve(const int a, const int b) {
	int res = 0;

	for (int i = a; i <= b; ++i) {
		for (int j = i + 1; j <= b; ++j) {
			if (isPair(i, j)) {
				++res;
			}
		}
	}

	return res;
}

int main() {
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);

	scanf("%d\n", &N);
	for (int i = 0; i < N; ++i) {
		int a = 0;
		int b = 0;
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", i + 1, solve(a, b));
	}

	return 0;
}
