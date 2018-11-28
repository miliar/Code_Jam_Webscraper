#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int dist[110];

void process() {
	int x, s, r, t, n;
	int b, e, w;
	double res, lv, tm;
	scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
	memset(dist, 0, sizeof(dist));
	for (int i = 0; i < n; ++i) {
		scanf("%d%d%d", &b, &e, &w);
		dist[w] += e - b;
		x -= (e - b);
	}
	dist[0] += x;
	res = 0.0;
	lv = (double)t;
	for (int i = 0; i <= 100; ++i) {
		tm = dist[i] / (double)(i + r);
		if (lv > tm) {
			lv -= tm;
			res += tm;
		} else {
			res += lv;
			res += (dist[i] - lv * (i + r)) / (i + s);
			lv = 0.0;
		}
	}
	printf("%.9lf\n", res);
}

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int t = 1; t <= cas; ++t) {
		printf("Case #%d: ", t);
		process();
	}
	return 0;
}
