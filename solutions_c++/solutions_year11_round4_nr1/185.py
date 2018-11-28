#include <stdio.h>
#include <algorithm>
using namespace std;

struct walkway {
	int l, w;
	bool operator < (const walkway o) const {
		return w < o.w;
	}
} a[1010];
int cs, ct, x, s, r, t, n;

int main()
{
	double time, runt;
	int i, u, v, len;
	scanf("%d", &ct);
	for (cs = 1; cs <= ct; cs++) {
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		len = x;
		for (i = 0; i < n; i++) {
			scanf("%d%d%d", &u, &v, &a[i].w);
			a[i].l = v - u;
			len -= a[i].l;
		}
		a[n].l = len;
		a[n].w = 0;
		sort(a, a + n + 1);

		runt = t;
		time = 0;
		for (i = 0; i <= n; i++) {
			if (runt >= (double)a[i].l / (r + a[i].w)) {
				time += (double)a[i].l / (r + a[i].w);
				runt -= (double)a[i].l / (r + a[i].w);
			}
			else {
				time += runt + (double)(a[i].l - runt * (r + a[i].w)) / (s + a[i].w);
				runt = 0;
			}
		}

		printf("Case #%d: %.10lf\n", cs, time);
	}
	return 0;
}
