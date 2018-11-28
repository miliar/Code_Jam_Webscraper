#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <ctime>
#define MAXN 1003
using namespace std;
const int INF = 0x3f3f3f3f;
const double eps = 1e-7;
typedef long long LL;
typedef pair<int, int> pii;

double s, r, t;
int x, n;

struct SEG {
	int b, e;
	double w;
	void read() {
		scanf("%d %d %lf", &b, &e, &w);
	}
	bool operator<(const SEG &t) const {
		return w < t.w;
	}
} seg[MAXN];

int main() {
#ifndef ONLINE_JUDGE
//	freopen("in", "r", stdin);
//	freopen("out", "w", stdout);
#endif

	int dataset;
	scanf("%d", &dataset);
	for (int cas = 1; cas <= dataset; ++cas) {
		scanf("%d %lf %lf %lf %d", &x, &s, &r, &t, &n);

		int res = x;
		for (int i = 0; i < n; ++i) {
			seg[i].read();
			res -= (seg[i].e - seg[i].b);
		}
		seg[n].b = 0;
		seg[n].e = res;
		seg[n].w = 0;
		++n;

		sort(seg, seg + n);

		double final = 0;
		for (int i = 0; i < n; ++i) {
			double use = min(t, (seg[i].e - seg[i].b) / (seg[i].w + r));
			t -= use;

			double walk = (seg[i].w + r) * use;
			double rem = seg[i].e - seg[i].b - walk;
			final += use + rem / (seg[i].w + s);
		}

		printf("Case #%d: %.7lf\n", cas, final);
	}

	return 0;
}
