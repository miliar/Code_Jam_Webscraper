#include <cstdio>
#include <algorithm>

using namespace std;

int n;
int a[1005];
int main() {
	int T; scanf("%d", &T);
	int cas = 0;
	while (T--) {
		int ret = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			ret += a[i];
		}
		int x = 0;
		int mn = 1<<28;
		for (int i = 0; i < n; ++i) {
			x ^= a[i];
			if (a[i] < mn) mn = a[i];
		}
		printf("Case #%d: ", ++cas);
		if (x) puts("NO");
		else {
			printf("%d\n", ret - mn);
		}
	}
	return 0;
}
