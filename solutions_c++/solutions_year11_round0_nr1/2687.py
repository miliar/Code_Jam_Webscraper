#include <cstdio>
#include <cstring>
#define ABS(x) ((x) > 0 ? (x) : -(x))
using namespace std;
const int MAXN = 105;
struct op {
	int rt, p;
} a[MAXN];
int T, N, ans, pto, ptb, poo, pob, time_require, i, t;
char c;

void init() {
	memset(a, 0, sizeof(a));
	scanf("%d", &N);
	for (i = 1; i <= N; i ++) {
		while (c = getchar(), c != 'O' && c != 'B');
		if (c == 'O') a[i].rt = 1; else a[i].rt = 2;
		scanf("%d", &a[i].p);
	}
}

void work() {
	for (pto = 1; pto <= N && a[pto].rt != 1; pto ++);
	for (ptb = 1; ptb <= N; ptb ++)
		if (a[ptb].rt == 2) break;
	poo = pob = 1;
	ans = 0;
	for (i = 1; i <= N; i ++) {
		if (a[i].rt == 1) {
			time_require = ABS(a[i].p - poo) + 1;
			if (ptb <= N)
			if (a[ptb].p > pob) {
				if (a[ptb].p - pob <= time_require) pob = a[ptb].p;
				else pob += time_require;
			} else {
				if (pob - a[ptb].p <= time_require) pob = a[ptb].p;
				else pob -= time_require;
			}
			for (++ pto; pto <= N && a[pto].rt != 1; pto ++);
			poo = a[i].p;
		} else {
			time_require = ABS(a[i].p - pob) + 1;
			if (pto <= N)
			if (a[pto].p > poo) {
				if (a[pto].p - poo <= time_require) poo = a[pto].p;
				else poo += time_require;
			} else {
				if (poo - a[pto].p <= time_require) poo = a[pto].p;
				else poo -= time_require;
			}
			for (++ ptb; ptb <= N && a[ptb].rt != 2; ptb ++);
			pob = a[i].p;
		}
		ans += time_require;
	}
	printf("Case #%d: %d\n", t, ans);
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	for (scanf("%d", &T), t = 1; t <= T; t ++) {
		init();
		work();
	}
	return 0;
}
