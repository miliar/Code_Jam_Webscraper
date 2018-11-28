#include <cstdio>
#include <algorithm>
using namespace std;

#define N 16384

int T, n, p[N], x[N], y[N], ok[N], tx[N], ty[N], d, t;
bool ans;

bool cmp(int a, int b) {
	return x[a] < x[b];
}

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) scanf("%d%d", x + i, y + i), p[i] = i;
		sort(p, p + n, cmp);
		for (int i = 0; i < n; ++i) tx[i] = x[p[i]], ty[i] = y[p[i]];
		for (int i = 0; i < n; ++i) x[i] = tx[i], y[i] = ty[i];
		for (int i = 0; i < n; ++i) ok[i] = -1;
		ok[0] = 0;
		for (int i = 0; i < n; ++i) if (ok[i] != -1) {
			for (int j = i + 1; j < n && x[j] <= x[i] + x[i] - ok[i]; ++j) {
				t = x[i]; if (x[i] + y[j] < x[j]) t = x[j] - y[j]; if (t < 0) t = 0;
				if (ok[j] == -1 || t < ok[j]) ok[j] = t;
			}
		}
		scanf("%d", &d);
		ans = 0;
		for (int i = 0; i < n; ++i) if (ok[i] != -1 && d <= x[i] + x[i] - ok[i]) ans = 1;
		puts(ans ? "YES" : "NO");
	}
	return 0;
}
