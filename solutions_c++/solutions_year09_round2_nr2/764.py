#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int MAXN = 109;

int a[MAXN];

int main() {
	freopen("F:\\B-large.in", "r", stdin);
	freopen("F:\\B-large.out", "w", stdout);
	int T;
	int i, j, len;
	char s[109];
	int cas = 0;

	scanf("%d", &T);
	while (T--) {
		scanf("%s", s);
		printf("Case #%d: ", ++cas);
		len = strlen(s);
		if (next_permutation(s, s + len)) {
			printf("%s\n", s);
		} else {
			int min = 0x3f3f3f3f, pos;
			char ans[109];
			for (i = 0; i < len; ++i) {
				if (s[i] != '0' && s[i] < min) {
					min = s[i];
					pos = i;
				}
			}
			printf("%c0", min);
			for (i = j = 0; i < len; ++i)
				if (i != pos) ans[j++] = s[i];
			sort(ans, ans + j);
			ans[j] = 0;
			printf("%s", ans);
			printf("\n");
		}
	}
	return 0;
}
