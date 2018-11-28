#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef pair <int, int> PII;

int n, K, B, t;
PII a[50];

int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d%d%d%d", &n, &K, &B, &t);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i].first);
		}
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i].second);
		}
		sort(a, a + n);
		int res = 0, c = 0;
		for (int i = n - 1; i >= 0 && K > 0; i--) {
			if ((LL)a[i].first + (LL)t * a[i].second >= B) {
				res += c;
				K--;
			} else {
				c++;
			}
		}
		if (K > 0) {
			printf("Case #%d: IMPOSSIBLE\n", cas);
		} else {
			printf("Case #%d: %d\n", cas, res);
		}
	}
	return 0;
}
