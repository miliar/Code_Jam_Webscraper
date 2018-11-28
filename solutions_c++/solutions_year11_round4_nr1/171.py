#include <cstdio>

#include <algorithm>
using namespace std;

struct Way{
	int b, e, w;
}w[3000];

bool cmp(const Way& w0, const Way& w1) {
	return w0.w < w1.w;
}

double work() {
	int x, s, r, n;
	double t;
	scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);
	int nowalk = x;
	for (int i = 0; i < n; ++i ) {
		scanf("%d%d%d", &w[i].b, &w[i].e, &w[i].w);
		nowalk -= w[i].e - w[i].b;
	}
	double ans = 0;
	sort(w, w + n, cmp);
	double v = t;
	if (v > nowalk * 1.0 / r)
		v = nowalk * 1.0 / r;
	ans += v;
	nowalk -= v * r;
	t -= v;
	ans += 1.0 * nowalk / s;
	for (int i = 0; i < n; ++i) {
		double l = w[i].e - w[i].b;
		v = l / (w[i].w + r);
		if (v > t)
			v = t;
		ans += v;
		t -= v;
		l -= v * (w[i].w + r);
		ans += l / (w[i].w + s);
	}
	return ans;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		printf("Case #%d: %.6lf\n", Ti, work());
	}
}
