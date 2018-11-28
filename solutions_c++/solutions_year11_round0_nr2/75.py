#include <cstdio>
#include <cstring>

int T, n, sn;
char s[256], c[27][27], t[4], st[256];
bool d[27][27];

int main() {
	scanf("%d", &T);
	for (int r = 0; r < T; ) {
		printf("Case #%d: ", ++r);
		memset(c, 0, sizeof(c));
		memset(d, 0, sizeof(d));
		sn = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s", t);
			c[*t&31][t[1]&31] = c[t[1]&31][*t&31] = t[2]&31;
		}
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s", t);
			d[*t&31][t[1]&31] = d[t[1]&31][*t&31] = 1;
		}
		scanf("%d%s", &n, s);
		for (int i = 0; i < n; ++i) {
			st[sn] = s[i]&31;
			++sn;
			if (1 < sn && c[st[sn - 1]][st[sn - 2]])
				st[sn - 2] = c[st[sn - 1]][st[sn - 2]], --sn;
			else
				for (int j = 0; j < sn; ++j)
					if (d[st[j]][s[i]&31])
						sn = 0;
		}
		if (sn) {
			printf("[%c", *st + 64);
			for (int i = 1; i < sn; ++i)
				printf(", %c", st[i] + 64);
			printf("]\n");
		} else
			puts("[]");
	}
	return 0;
}
