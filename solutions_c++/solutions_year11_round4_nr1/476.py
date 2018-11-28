#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

struct node {
	int b, e, w;
} a[1010];

bool operator<(const node &node1, const node &node2) {
	return node1.w < node2.w;
}

int main(int argc, char** argv) {
	int T;
	scanf("%d", &T);
	for (int nCase = 1; nCase <= T; ++nCase) {
		int x, s, r, t, n;
		double ans = 0;
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		double run = t;
		double left = x;
		for (int i = 0; i < n; ++i) {
			scanf("%d%d%d", &a[i].b, &a[i].e, &a[i].w);
			left -= a[i].e - a[i].b;
		}
		sort(a, a + n);
		if (left < r * run) {
			ans += left / r;
			run -= left / r;
		} else {
			ans += run + (left - r * run) / s;
			run = 0.;
		}
		for (int i = 0; i < n; ++i) {
			//printf(" %d %f %f\n", i, ans, run);
			if (a[i].e - a[i].b < (r + a[i].w) * run) {
				ans += (double) (a[i].e - a[i].b) / (r + a[i].w);
				run -= (double) (a[i].e - a[i].b) / (r + a[i].w);
			} else {
				ans += run + ((double) a[i].e - a[i].b - (r + a[i].w) * run) / (double) (s + a[i].w);
				run = 0.;
			}
		}
		printf("Case #%d: %f\n", nCase, ans);
	}
	return 0;
}
