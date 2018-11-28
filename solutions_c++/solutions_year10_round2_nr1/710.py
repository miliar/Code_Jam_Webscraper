#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int T, cs, n, m, l, ans;
struct str {
	char s[200];
	int count;
	bool operator < (const str &o) const {
		if (strcmp(s, o.s) < 0 || strcmp(s, o.s) == 0 && count < o.count) return 1;
			else return 0;
	}
} a[200];

int diff(char *x, char *y)
{
	int i, ret = 0;
	for (i = 0; x[i] && y[i]; i++)
		if (x[i] != y[i]) break;
	for (; y[i]; i++) 
		if (y[i] == '/') ret++;
	return ret;
}

int main()
{
//	freopen("A-small-attempt0.in", "r", stdin);
	int i, j;
	scanf("%d", &T);
	for (cs = 1; cs <= T; cs++) {
		scanf("%d%d", &n, &m);
		ans = 0;
		a[0].s[0] = '/';
		a[0].s[1] = 0;
		a[0].count = 0;
		l = 0;
		for (i = 0; i < n; i++) {
			l++;
			scanf("%s", a[l].s);
			j = strlen(a[l].s);
			a[l].s[j] = '/';
			a[l].s[j+1] = 0;
			a[l].count = 0;
		}
		for (i = 0; i < m; i++) {
			l++;
			scanf("%s", a[l].s);
			j = strlen(a[l].s);
			a[l].s[j] = '/';
			a[l].s[j+1] = 0;
			a[l].count = 1;
		}
		sort(a + 1, a + l + 1);
		ans = 0;
		for (i = 1; i <= l; i++) {
			if (a[i].count) ans += diff(a[i - 1].s, a[i].s);
		}
//		for (i = 0; i < l; i++) {
//			printf("%s\n", a[i].s);
//		}
		printf("Case #%d: %d\n", cs, ans);
	}
	return 0;
}
