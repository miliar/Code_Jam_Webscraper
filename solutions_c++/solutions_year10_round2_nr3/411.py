#include <stdio.h>
#define N 501
typedef long long ll;

ll A[N + 1][N + 1];

ll cmb(ll n, ll s) {
	ll r = 1;
	if (s < 0 || n < s) return 0;
	if (n - s < s) s = n - s;
	for (int i = 0; i < s; i++)
	 r = r * (n - i) / (i + 1);
	return r;
}

void init() {
	for (int i = 2; i <= N; i++) {
		A[i][1] = 1;
		for (int j = 2; j < i; j++) {
			ll sum = 0;
			for (int k = 1; k < j; k++) {
				sum += A[j][k] * cmb(i - j - 1, j - k - 1);
			}
			A[i][j] = sum % 100003;
		}
	}
}

int solve(ll n) {
	ll sum = 0;
	for (int i = 1; i < n; i++) sum += A[n][i];
	return sum % 100003;
}

int main() {
	int n, x;
	init();
	scanf("%d", &n);
	for (int case_x = 1; case_x <= n; case_x++) {
		scanf("%d", &x);
		printf("Case #%d: %d\n", case_x, solve(x));
	}
}