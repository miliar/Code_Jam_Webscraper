#include <cstdio>
#include <algorithm>
using namespace std;

#define CODE C-large

#define INPUT QUOTE(CODE)".in"
#define OUTPUT QUOTE(CODE)".out"
#define _QUOTE(x) #x
#define QUOTE(x) _QUOTE(x)

#define MOD 100003
#define MAXN 502

int c[MAXN][MAXN];
int C(int n, int k) {
	if (n < 0 || k < 0)
		return 0;
	int &r = c[n][k];
	if (r >= 0)
		return r;
	if (k > n)
		return r = 0;
	if (n == 0 || k == n)
		return r = 1;
	return r = (C(n-1, k) + C(n-1, k-1)) % MOD;
}

int w[MAXN][MAXN];
int W(int n, int i) {
	int &r = w[n][i];
	if (r >= 0)
		return r;
	if (i == 1)
		return r = 1;
	r = 0;
	for (int j = 1; j < i; ++j) {
		r = (r + (long long) W(i, j) * C(n - i - 1, i - j - 1)) % MOD;
	}
	return r;
}

int solve() {
	fill(w[0], w[MAXN], -1);
	int n;
	scanf("%d", &n);
	int r = 0;
	for (int i = 1; i <= n; ++i)
		r = (r + W(n, i)) % MOD;
	return r;
}

int main() {
	fill(c[0], c[MAXN], -1);
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}
