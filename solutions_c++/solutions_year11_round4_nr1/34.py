#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <map>

#define maxn 1010

using namespace std;

struct node {
	int b, e, w;
} a[3010];
int t, x, s, r, n;
bool cmp(node x, node y) {
	return x.b < y.b;
}
bool cmp2(node i, node j) {
	return i.w + s < j.w + s;
}
int main() {
	int i,j,k;
	int tn,cp;
	for (scanf("%d",&tn),cp=1;cp<=tn;cp++) {
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		for (i = 0; i < n; ++i) scanf("%d%d%d", &a[i].b, &a[i].e, &a[i].w);
		sort(a,a+n,cmp);
		int last = 0, m = n;
		for (i = 0; i < n; ++i) {
			if (last < a[i].b) {
				a[m].b = last; a[m].e = a[i].b; a[m++].w = 0;
			}
			last = a[i].e;
		}
		if (last < x) {
			a[m].b = last; a[m].e = x; a[m++].w = 0;
		}

		sort(a, a + m, cmp2);
		double ans = 0, used = 0;
		for (i = 0; i < m; ++i) {
			if (used < t) {
				double run = (a[i].e - a[i].b) / (double)(a[i].w + r);
				if (used + run > t) {
					double left = (a[i].e - a[i].b) - (t - used) * (a[i].w + r);
					run = (t - used) + left / (double)(a[i].w + s);
					ans += run;
					used = t;
				}else {
					ans += run;
					used += run;
				}
			}
			else ans += (a[i].e - a[i].b) / (double)(a[i].w + s);
		}

		printf("Case #%d: %.8lf\n", cp, ans);
	}
	return 0;
}
