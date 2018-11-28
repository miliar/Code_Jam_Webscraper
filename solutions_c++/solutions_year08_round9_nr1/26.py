#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;

#define x first
#define y second

int T, x[5000], y[5000], z[5000], ans, n, C, Z, m;
pair <int, int> p[5000];

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		ans = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d%d%d", x + i, y + i, z + i);
		for (int i = 0; i < n; ++i) {
			C = z[i];
			Z = 10000 - C;
			m = 0;
			for (int j = 0; j < n; ++j)
			  if (z[j] <= C) {
					p[m].x = x[j];
					p[m].y = y[j];
					++m;
   			}
			sort(p, p + m);
			priority_queue <int> q;
			for (int j = 0; j < m; ++j) {
				q.push(p[j].y);
				while (!q.empty() && Z < p[j].x + q.top())
					q.pop();
				if (ans < q.size())
					ans = q.size();
			}
		}
		printf("Case #%d: %d\n", r, ans);
	}
	return 0;
}
