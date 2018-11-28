#include <cstdio>
#include <set>
#define D 5000
#define L 15
using namespace std;
char str[D][L + 1];
int main()
{
	int l, d, n, i, j, k;
	char c, rest[10];
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-small.out", "w", stdout);
	scanf("%d%d%d", &l, &d, &n);
	gets(rest);
	for (i = 0; i < d; ++i) {
		gets(str[i]);
	}
	for (i = 1; i <= n; ++i) {
		set<char> st[l];
		int ans = 0;
		printf("Case #%d: ", i);
		for (j = 0; j < l; ++j) {
			c = getchar();
			if (c == '(') {
				while ((c = getchar()) != ')') {
					st[j].insert(c);
				}
			} else st[j].insert(c);
		}
		gets(rest);
		for (j = 0; j < d; ++j) {
			for (k = 0; k < l; ++k) {
				if (st[k].find(str[j][k]) == st[k].end())
					break;
			}
			if (k == l)
				ans ++;
		}
		printf("%d\n", ans);
	}
}
