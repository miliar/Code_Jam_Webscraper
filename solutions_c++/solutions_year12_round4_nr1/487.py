#include <cstdio>
#include <cstring>
#include <algorithm>

const int N = 20000;
const int inf = 2e9;
int d[N], l[N], mx[N];

int main() {
	int t, n;
	scanf("%d", &t);
	for (int it = 0; it < t; ++it) {
		scanf("%d", &n);
		d[0] = 0;
		l[n + 1] = inf;
		for (int i = 1; i <= n; ++i)
			scanf("%d%d", &d[i], &l[i]);
		scanf("%d", &d[n + 1]);
		memset(mx, -1, sizeof(mx));
		mx[0] = 1;
		bool ok = false;
		for (int i = 0; i <= n; ++i) {
			if (mx[i] == n + 1) {
				ok = true;
				break;
			}
			int k = i;
			for (int j = i + 1; j <= mx[i]; ++j) {
				while ((k <= n) && (d[k + 1] - d[j] <= std::min(l[j], d[j] - d[i])))
					++k;
				if (mx[j] < k)
					mx[j] = k;
			}
		}
		printf("Case #%d: %s\n", it + 1, ok ? "YES" : "NO");
	}
}