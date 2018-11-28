#include<stdio.h>
#include<string>
const int maxl = 3005;
const int maxn = 2005;
struct Like {
	int id, malt;
}likes[maxl];
int st[maxn], cnt[maxn];
int pos;
int malt[maxn];
int f[maxn];
int main() {
	int T;
	scanf("%d", &T);
	for (int casen = 1; casen <= T; casen++) {
		int n, m;
		scanf("%d%d", &n, &m);
		pos = 0;
		memset(f, 0, sizeof(f));
		for (int i = 0; i < m; i++) {
			scanf("%d", &cnt[i]);
			st[i] = pos;
			for (int j = 0; j < cnt[i]; j++) {
				int x, y;
				scanf("%d%d", &x, &y);
				likes[pos].id = x;
				likes[pos].malt = y;
				pos++;
				if (y == 1) {
					f[i] = x;
				}
			}
		}
		memset(malt, 0, sizeof(malt));
		int over;
		while (1) {
			over = 1;
			for (int i = 0; i < m; i++) {
				int sat = 0;
				for (int j = st[i]; j < st[i] + cnt[i]; j++) {
					if (malt[likes[j].id] == likes[j].malt) {
						sat = 1;
						break;
					}
				}
				if (!sat) {
					if (f[i] != 0) {
						if (malt[f[i]] == 0) {
							malt[f[i]] = 1;
							over = 0;
							break;
						} else {
							over = -1;
							break;
						}
					} else {
						over = -1;
						break;
					}
				}
			}
			if (over != 0) {
				break;
			}
		}
		if (over == 1) {
			printf("Case #%d:", casen);
			for (int i = 1; i <= n; i++) {
				printf(" %d", malt[i]);
			}
			printf("\n");
		} else {
			printf("Case #%d: IMPOSSIBLE\n", casen);
		}
	}
	return 0;
}
