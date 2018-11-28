#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;

const int MAXN = 10000 + 1000;
int d[MAXN], l[MAXN];

int main() {
	freopen("Al.in", "r", stdin); freopen("Al.out", "w", stdout);
	int Tc, n, D;
	scanf("%d", &Tc);
	for (int re = 1; re <= Tc; ++re) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d", &d[i], &l[i]);
		}
		scanf("%d", &D);

		queue<int> qidx;
		queue<int> qreach;
		qidx.push(0);
		qreach.push(d[0] * 2);
		for (int i = 1; i < n && !qidx.empty(); ++i) {
			while (!qreach.empty()) {
				if (qreach.front() >= d[i]) {
					qidx.push(i);
					qreach.push(min(d[i] - d[qidx.front()], l[i]) + d[i]);
					break;
				} else {
					qreach.pop();
					qidx.pop();
				}
			}
		}
		printf("Case #%d: ", re);
		bool ok = false;
		while (!qreach.empty() && !ok) {
			if (qreach.front() >= D) {
				ok = true;
			}
			qreach.pop();
		}
		if (ok) {
			puts("YES");
		} else {
			puts("NO");
		}
	}
	return 0;
}
