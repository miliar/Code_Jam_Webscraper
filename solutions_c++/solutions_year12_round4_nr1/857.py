#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int N = 10001;
int a[N], b[N], c[N];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int i, j, k, r, n, t, tt;
	scanf("%d", &tt);
	for (t = 1; t <= tt; t++) {
		scanf("%d", &n);
		for (i = 0; i < n; i++)
			scanf("%d%d", &a[i], &b[i]);
		scanf("%d", &a[n]);

		memset(c, -1, sizeof(c));
		j = 0;
		c[0] = a[0];
		for (i = 1; i < n; i++) {
			while (j < i) {
				if (c[j] != -1 && a[j] + min(b[j], c[j]) >= a[i]) {
					c[i] = a[i] - a[j];
					break;
				} else {
					j ++;
				}
			}
		}
		k = 0;
		for (i = 0; i < n; i++)
			if (c[i] && a[i] + min(b[i], c[i]) >= a[n])
				k = 1;

		if (k)printf("Case #%d: YES\n", t);
		else printf("Case #%d: NO\n", t);
	}
	return 0;
}
