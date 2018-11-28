#include <cstdio>
#include <queue>
using namespace std;

int main() {
	freopen("roller.in", "r", stdin);
	freopen("roller.out", "w", stdout);
	int T, t, r, k, n, i, s;
	long long total;
	scanf("%d", &t);
	for (T = 1; T <= t; T++) {
		scanf("%d %d %d", &r, &k, &n);
		queue<int> g;
		for (i = 0; i < n; i++) {
			scanf("%d", &s);
			g.push(s);
		}
		total = 0;
		for (i = 0; i < r; i++) {
			s = 0;
			for (int j = 0; j < n && g.front() + s <= k; j++) {
				g.push(g.front());
				s += g.front();
				g.pop();
			}
			total += s;
		}
		printf("Case #%d: %lld\n", T, total);
	}
	return 0;
}
