#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 128;

int main() {
	int re, n, ans;
	char buf[MAXN];
	int cnt[MAXN], p[MAXN];

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s", buf);
			cnt[i] = n - 1;
			while (cnt[i] >= 0 && buf[cnt[i]] == '0') {
				--cnt[i];
			}
		}
		ans = 0;
		for (int i = 0; i < n; ++i) {
			int k = -1;
			if (cnt[i] > i) {
				for (int j = i + 1; j < n; ++j) {
					if (cnt[j] <= i) {
						k = j;
						break;
					}
				}
			} else {
				k = i;
			}
			ans += k - i;
			for (int j = k; j > i; --j) {
				cnt[j] = cnt[j - 1];
			}
		}
		printf("Case #%d: %d\n", ri, ans);
	}

	return 0;
}

