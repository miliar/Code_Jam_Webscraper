#include <cstdio>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;
const int maxn = 10000 + 10;

typedef long long INT;
int T, n;
INT d[maxn], l[maxn], sd[maxn], D;
bool enq[maxn];

bool gao() {
	for (int i = 0; i <= n; ++i)
		enq[i] = sd[i] = 0;
	queue<int> q;
	q.push(1);
	enq[1] = true;
	sd[1] = d[1] + min(d[1], l[1]);
	int u;
	INT tmp;
	while (!q.empty()) {
		u = q.front();
		enq[u] = false;
		q.pop();
		for (int i = 1; i <= n; ++i)
			if (d[u] <= d[i] && d[i] <= sd[u] &&
					(tmp = d[i] + min(abs(d[u] - d[i]), l[i])) > sd[i]) {
				sd[i] = tmp;
				if (!enq[i]) {
					enq[i] = true;
					q.push(i);
				}
			}
	}
	for (int i = 1; i <= n; ++i)
		if (sd[i] >= D)
			return true;
	return false;
}

int main() {
	scanf("%d", &T);
	for (int index = 1; index <= T; ++index) {
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i) {
			scanf("%lld%lld", &d[i], &l[i]);
		}
		scanf("%lld", &D);
		printf("Case #%d: %s\n", index, gao() ? "YES" : "NO");
	}
	return 0;
}
