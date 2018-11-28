#include <cstdio>
#include <cstring>


int C, D, n;
char a[300][300];
bool b[300][300];
char stk[1000], sn;

int main() {
	int T; scanf("%d", &T);
	int cas = 0;
	while (T--) {
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		scanf("%d", &C);
		for (int i = 0; i < C; ++i) {
			char s[4];
			scanf("%s", s);
			a[s[0]][s[1]] = a[s[1]][s[0]] = s[2];
		}
		scanf("%d", &D);
		for (int i = 0; i < D; ++i) {
			char s[4];
			scanf("%s", s);
			b[s[0]][s[1]] = b[s[1]][s[0]] = 1;
		}
		char s[105];
		scanf("%d", &n);
		scanf("%s", s);
		sn = 0;
		for (int i = 0; i < n; ++i) {
			stk[sn++] = s[i];
			if (sn > 1) {
				char cc = a[stk[sn - 1]][stk[sn - 2]];
				if (cc) {
					--sn;
					stk[sn - 1] = cc;
				} else {
					for (int k = 0; k <= sn - 1; ++k) {
						if (b[stk[sn - 1]][stk[k]]) {
							sn = 0;
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: [", ++cas);
		for (int i = 0; i < sn; ++i) {
			printf(i == sn - 1?"%c":"%c, ", stk[i]);
		}
		puts("]");
	}
	return 0;
}
