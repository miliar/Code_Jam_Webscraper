#include <cstdio>
using namespace std;
const int MAXN = 1005;
int i, j, k, s1, s2, N, M, t, T, ans, sum;
int c[MAXN];

void init() {
	scanf("%d", &N);
	for (i = 0; i < N; i ++)
		scanf("%d", &c[i]);
}

void work() {
	ans = 0;
	for (i = 1; i < (1 << N) - 1; i ++) {
		sum = s1 = s2 = 0;
		for (j = 0; j < N; j ++)
			if ((i >> j) & 1) {
				sum += c[j];
				s1 ^= c[j];
			} else s2 ^= c[j];
		if (s1 == s2) ans >?= sum;
	}
	if (ans == 0) printf("Case #%d: NO\n", t);
	else printf("Case #%d: %d\n", t, ans);
}

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	for (scanf("%d", &T), t = 1; t <= T; t ++) {
		init();
		work();
	}
	return 0;
}
