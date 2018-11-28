#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

struct Rectangle {
	int l, r, u, d;
};

bool connected(Rectangle a, Rectangle b) {
	return max(a.l - 1, b.l) <= min(a.r + 1, b.r) && max(a.u - 1, b.u) <= min(a.d + 1, b.d);
}

int p[1001];
Rectangle t[1001];

int gp(int x) {
	if (p[x] != x) p[x] = gp(p[x]);
	return p[x];
}

int n;

void alg() {
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		scanf("%d %d %d %d", &t[i].l, &t[i].u, &t[i].r, &t[i].d);
		p[i] = i;
	}
	int res = 0;
	for (int i = 1; i <= n; ++i) {
		for (int j = i + 1; j <= n; ++j) {
			if (connected(t[i], t[j])) {
				p[gp(i)] = gp(p[j]);
			}
		}
	}
	for (int i = 1; i <= n; ++i) {
		int ul = 1000000000, r = 0, d = 0;
		for (int j = 1; j <= n; ++j) {
			if (gp(j) == i) {
				ul = min(ul, t[j].u + t[j].l);
				r = max(r, t[j].r);
				d = max(d, t[j].d);
			}
		}
		res = max(res, r + d - ul + 1);
	}
	printf("%d\n", res);
}

int main() {
	int d;
	scanf("%d", &d);
	for (int i = 1; i <= d; ++i) {
		printf("Case #%d: ", i);
		alg();
	}
}
