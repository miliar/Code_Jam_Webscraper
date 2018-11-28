#include <cstdio>
#include <cstdlib>
char a[40][40];
int tmp;
int idx[40];
int main ()
{
	int t, ca, i, j, k, n, ans;
	char rest[10];
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	for (ca = 1; ca <= t; ++ ca) {
		scanf("%d", &n);
		gets(rest);
		for (i = 0; i < n; ++ i) {
			for (j = 0; j < n; ++ j)
				scanf("%c", &a[i][j]);
			gets(rest);
		}
		for (i = 0; i < n; ++ i)
			idx[i] = i;
		ans = 0;
		for (i = 0; i < n; ++ i) {
			for (j = i + 1; j < n; ++ j)
				if (a[idx[i]][j] == '1')
					break;
			if (j < n) {
				for (j = i + 1; j < n; ++ j) {
					for (k = i + 1; k < n; ++ k)
						if (a[idx[j]][k] == '1')
							break;
					if (k == n)
						break;
				}
				tmp = idx[j];
				for (k = j; k > i; -- k)
					idx[k] = idx[k - 1];
				idx[i] = tmp;
				ans += j - i;
			}
		}
		printf("Case #%d: %d\n", ca, ans);
	}
}
