#include <cstdio>
#include <algorithm>
#include <cstring>

namespace gcj{
	using namespace std;

	const int MAXN = 1005;
	struct walkway{
		int b, e, w;
		friend bool operator< (const walkway& l, const walkway& r) {
			return l.w < r.w;
		}
	};

	walkway cors[MAXN];

	void solve(int T) {
		int x, s, r, t, n;
		int wwlen = 0, rlen;
		double res = 0.0, rt;

		scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
		for (int  i = 0; i < n; i ++)
			scanf("%d %d %d", &cors[i].b, &cors[i].e, &cors[i].w), wwlen += cors[i].e - cors[i].b;
		rlen = x - wwlen;
		rt = t;
		sort(cors, cors + n);

		if(rlen >= t * r)
			res = 1.0 * (rlen - t * r) / s + t, rt = 0.0;
		else
			res = 1.0 * rlen / r, rt -= res;

		for (int  i = 0; i < n; i ++) {
			if (rt <= 0.0) {
				res += 1.0 * (cors[i].e - cors[i].b) / (s + cors[i].w);
				continue;
			}
			if (1.0 * (cors[i].e - cors[i].b) / (r + cors[i].w) <= rt) {
				res += 1.0 * (cors[i].e - cors[i].b) / (r + cors[i].w);
				rt -= 1.0 * (cors[i].e - cors[i].b) / (r + cors[i].w);
			} else {
				res += 1.0 * (cors[i].e - cors[i].b - (r + cors[i].w) * rt) / (s + cors[i].w) + rt;
				rt = 0.0;
			}
		}

		printf("Case #%d: %.9lf\n", T + 1, res);
	}

	void solve() {
		int t;
		scanf("%d", &t);
		for (int i = 0; i < t; i ++)
			solve(i);
	}
}

int main() {
	freopen("E:/OWenT/GCJ/R2/A-large.in", "r", stdin);
	freopen("E:/OWenT/GCJ/R2/A-large.out", "w", stdout);

	gcj::solve();
	return 0;
}
