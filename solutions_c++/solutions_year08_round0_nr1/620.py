#include <stdio.h>
#include <string>
#include <cstring>
using namespace std;
int has[90000], rkb1[110], rkb2[110];
bool app[110];
char nam[110], sea[110][110];
inline void rk_init() {
	rkb1[0] = 1; rkb2[0] = 1;
	for (int i = 1; i < 105; ++i) {
		rkb1[i] = (rkb1[i - 1] << 3) % 307;
		rkb2[i] = rkb2[i - 1] * 31 % 293;
	}
}
inline int change(char c) {
	if (c >= 'a' && c <= 'z')
		return c - 97;
	else if (c >= 'A' && c <= 'Z')
		return c - 39;
	else if (c >= '0')
		return c + 4;
	else
		return 62;
}
inline int hash(char nam[]) {
	int i = 0, rk1 = 0, rk2 = 0, j;
	for (; nam[i] > 0; ++i) {
		j = change(nam[i]);
		rk1 = (rk1 + j * rkb1[i]) % 307;
		rk2 = (rk2 + j * rkb2[i]) % 293;
	}
	return rk1 * 293 + rk2;
}
int main() {
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int cas, t, n, m, i, j, ans, las;
	rk_init();
	for (scanf("%d", &cas), t = 1; t <= cas; ++t) {
		memset(has, 0, sizeof(has));
		for (scanf("%d ", &m), i = 1; i <= m; ++i) {
			gets(sea[i]);
			for (j = hash(sea[i]); has[j] > 0; ++j);
			has[j] = i;
		}
		memset(&app[1], true, m);
		for (scanf("%d ", &n), ans = 0, las = m, i = 0; i < n; ++i) {
			gets(nam);
			for (j = hash(nam); strcmp(sea[has[j]], nam) != 0; ++j);
			if (app[j = has[j]]) {
				--las;
				if (las == 0) {
					las = m - 1; ++ans;
					memset(&app[1], true, m);
				}
				app[j] = false;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
}