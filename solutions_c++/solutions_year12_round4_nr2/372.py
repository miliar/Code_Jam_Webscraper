#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

typedef long long LL;

#define MAXN 1010

int U, n, x, y;
struct Cir {
	int r, num;
}cir[MAXN];

int a[MAXN];
int X[MAXN], Y[MAXN];
bool used[MAXN];

LL sqr(int r) {
	return (LL)r * r;
}

bool cross(int x1, int y1, int r1, int x2, int y2, int r2) {
	return sqr(y1 - y2) + sqr(x1 - x2) < sqr(r1 + r2);
}

bool valid() {
	int u = U;
	int x1 = X[u], y1 = Y[u], r1 = cir[u].r;
	if(x1 < 0 || x1 > x || y1 < 0 || y1 > y) return false;
	for(int i = 0; i < n; ++i) {
		int v = a[i];
		if(u != v && used[v]) {
			int x2 = X[v], y2 = Y[v], r2 = cir[v].r;
			if(cross(x1, y1, r1, x2, y2, r2)) return false;
		}
	}
	return true;
}

bool cmp(Cir c1, Cir c2) {
	return c1.r < c2.r;
}

bool cmp2(Cir c1, Cir c2) {
	return c1.num < c2.num;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		scanf("%d%d%d", &n, &x, &y);
		for(int i = 0; i < n; ++i) {
			scanf("%d", &cir[i].r);
			cir[i].num = i;
		}

		sort(cir, cir + n, cmp);
		for(int i = 0; i < n; ++i) a[i] = cir[i].num;
		sort(cir, cir + n, cmp2);
		bool solved = false;
		int times = 1;
		do {
			memset(used, false, sizeof(used));
			used[a[0]] = true;
			X[a[0]] = 0, Y[a[0]] = 0;
			bool ok = true;
			for(int i = 1; i < n && ok; ++i) {
				int u = a[i];
				U = u;
				for(int j = 0; j < n; ++j) {
					int v = a[j];
					if(i != j && used[v]) {
						X[u] = X[v] - cir[u].r - cir[v].r;
						Y[u] = Y[v] - cir[v].r + cir[u].r;
						if(valid()) {
							used[u] = true;break;
						}

						X[u] = X[v] - cir[v].r - cir[u].r;
						Y[u] = Y[v] + cir[v].r - cir[u].r;
						if(valid()) {
							used[u] = true;break;
						}

						X[u] = X[v] - cir[v].r + cir[u].r;
						Y[u] = Y[v] + cir[v].r + cir[u].r;
						if(valid()) {
							used[u] = true;break;
						}

						X[u] = X[v] + cir[v].r - cir[u].r;
						Y[u] = Y[v] + cir[v].r + cir[u].r;
						if(valid()) {
							used[u] = true;break;
						}

						X[u] = X[v] + cir[v].r + cir[u].r;
						Y[u] = Y[v] + cir[v].r - cir[u].r;
						if(valid()) {
							used[u] = true;break;
						}

						X[u] = X[v] + cir[v].r + cir[u].r;
						Y[u] = Y[v] - cir[v].r + cir[u].r;
						if(valid()) {
							used[u] = true;break;
						}

						X[u] = X[v] + cir[v].r - cir[u].r;
						Y[u] = Y[v] - cir[v].r - cir[u].r;
						if(valid()) {
							used[u] = true;break;
						}

						X[u] = X[v] - cir[v].r + cir[u].r;
						Y[u] = Y[v] - cir[v].r - cir[u].r;
						if(valid()) {
							used[u] = true;break;
						}

					}
				}
				if(!used[u]) ok = false;
			}
			if(ok) {
				solved = true;break;
			}
			random_shuffle(a, a + n);
		} while(times--);
		if(!solved) puts("--------");
		printf("Case #%d:", cas);
		for(int i = 0; i < n; ++i) printf(" %d %d", X[i], Y[i]);
		puts("");

	}
	return 0;
}
