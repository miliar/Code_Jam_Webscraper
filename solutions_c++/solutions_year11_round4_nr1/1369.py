#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

double x, s, r, t;

struct Walk {
	double b, e, w;
};

const int MAX = 1010;
Walk w[MAX];
int n;

int comp(const void *p, const void *q) {
	Walk *a = (Walk *) p;
	Walk *b = (Walk *) q;
	if (a->w < b->w) return -1;
	else if (a->w > b->w) return 1;
	return 0;
}

double solve() {
	double nowalkway = 0.0;

	double pos = 0;
	for (int i = 0; i < n; i++) {
		nowalkway += (w[i].b - pos);
		pos = w[i].e;
	}
	nowalkway += (x - pos);

	double time = 0;
	if (nowalkway / r >= t) {
		time += t;
		nowalkway -= (t * r);
		t = 0;
		time += (nowalkway / s);
	} else {
		double tmp = (nowalkway / r);
		time += tmp;
		t -= tmp;
	}

	// sort by w
	qsort(w, n, sizeof(Walk), comp);

	// solve for walkways
	for (int i = 0; i < n; i++) {
		// can I run the max with this walkway?
		double dist = w[i].e - w[i].b;
		if (dist / (r + w[i].w) >= t) {
			time += t;
			dist -= (t * (r + w[i].w));
			t = 0;
			time += (dist / (s + w[i].w));
		} else {
			double tmp = (dist / (r + w[i].w));
			time += tmp;
			t -= tmp;
		}
	}

	return time;
}

int main() {
	int cc, c;
	scanf("%d", &cc);
	for (int c = 1; c <= cc; ++c) {
		scanf("%lf %lf %lf %lf %d", &x, &s, &r, &t, &n);
		for (int i = 0; i < n; i++) {
			scanf("%lf %lf %lf", &w[i].b, &w[i].e, &w[i].w);
		}
		printf("Case #%d: %.9lf\n", c, solve());
	}

	return 0;
}
