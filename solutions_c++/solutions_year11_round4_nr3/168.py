#include <cstdio>
#include <cmath>

#define N (1 << 20)

int T, n, cnt[N], ans;
bool ip[N];
long long x, y;

long long pp(long long a, long long b) {
	long long r = 1;
	while (b) {
		if (b&1)
			r = r*a;
		b >>= 1;
		a *= a;
	}
	return r;
}

int main() {
	for (int i = 0; i < N; ++i)
		ip[i] = 1;
	ip[0] = ip[1] = 0;
	for (int i = 0; i < N; ++i)
		if (ip[i])
			for (int j = i + i; j < N; j += i)
				ip[j] = 0;
	cnt[0] = 0;
	for (int i = 1; i < N; ++i)
		cnt[i] = cnt[i - 1] + ip[i];
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d:", r);
		ans = 0;
		scanf("%lld", &x);
		for (int i = 2; i <= 39; ++i) {
			y = pow(x, 1./i) - 1;
			while (pp(y, i) <= x)
				++y;
			ans += cnt[y - 1];
		}
		if (x > 1)
			++ans;
		printf(" %d\n", ans);
	}
	return 0;
}
