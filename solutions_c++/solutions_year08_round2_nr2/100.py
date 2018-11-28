#include <cstdio>
#include <memory>

const int maxn = 1000100;

int total, casei, cases, ans;
long long NA, NB, NP;
int father[maxn];
long long prime[maxn + 1];

inline void prepare() {
	memset(prime, 255, sizeof prime);
	total = 0;
	for (long long i = 2; i <= maxn; ++i) if (prime[i]) {
		prime[total++] = i;
		for (long long j = i * i; j <= maxn; j += i) prime[j] = 0;
	}
}

inline void init() {
	scanf("%I64d%I64d%I64d", &NA, &NB, &NP);
}

inline int getRoot(long long now) {
	now -= NA;
	int i = now, j;
	while (father[i] != i) i = father[i];
	while (father[now] != now) {
		j = father[now];
		father[now] = i;
		now = j;
	}
	return i;
}

inline void process() {
	for (long long i = NA; i <= NB; ++i) father[i - NA] = i - NA;

	for (int i = 0; i < total && prime[i] <= NB - NA; ++i) if (prime[i] >= NP) {
		long long now = (NA / prime[i]) * prime[i];
		while (now < NA) now += prime[i];
		while (now + prime[i] <= NB) {
			if (getRoot(now + prime[i]) != getRoot(now)) father[father[now + prime[i] - NA]] = father[now - NA];
			now += prime[i];
		}
	}
}

inline void print() {
	ans = 0;
	for (long long i = NA; i <= NB; ++i) if (getRoot(i) == i - NA) ++ans;
	printf("Case #%d: %d\n", casei, ans);
}

int main() {
//	freopen("in.txt", "r", stdin); freopen("", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);

	prepare();
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}
}
