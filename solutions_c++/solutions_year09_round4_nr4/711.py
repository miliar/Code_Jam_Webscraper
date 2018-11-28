#include <cstdio>
#include <algorithm>
#include <math.h>
#define maxn 100

using namespace std;

struct cerc {
	double x, y, r;
};

int n, i, j;
cerc v[maxn], mid;
double sol;
int tt, q;

void read() {
	int i;
	scanf("%d", &n);
	for (i = 1; i <= n; i++)
		scanf("%lf%lf%lf", &v[i].x, &v[i].y, &v[i].r);
}

inline double dist(cerc a, cerc b) {
	return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

inline double doit(cerc p1, cerc p2, cerc p3) {
	double sol;
	mid.x = (p1.x + p2.x) / 2.0;
	mid.y = (p1.y + p2.y) / 2.0;
//	if (q == 6)	fprintf(stderr, "%lf\n", dist(p1, p2) / 2.0);
	sol = (dist(p1, p2) / 2.0 + (p1.r + p2.r) / 2.0);
	
///	if (q == 7)	fprintf(stderr, "%lf\n", sol);
	sol = max(sol, p3.r);
	return sol;
}

void solve() {
	sol = 2000000000;
	if (n == 1) {
		sol = v[1].r;
		return;
	}

	if (n == 2) {
		mid.x = (v[1].x + v[2].x) / 2.0;
		mid.y = (v[1].y + v[2].y) / 2.0;
//		sol = max(dist(mid, v[1]) + v[1].r, dist(mid, v[2]) + v[2].r);
		sol = dist(v[1], v[2]) / 2.0 + (v[1].r + v[2].r) / 2.0;
//		if (q == 4)
//			fprintf(stderr, "%lf %lf %lf\n", sol, dist(mid, v[1]), dist(mid, v[2]));
		sol = min(sol, max(v[1].r, v[2].r));
		return;
	}

	sol = doit(v[1], v[2], v[3]);
//	if (q == 6)	fprintf(stderr, "%lf\n", sol);
	sol = min(sol, doit(v[1], v[3], v[2]));
//	if (q == 6)	fprintf(stderr, "%lf\n", sol);
	sol = min(sol, doit(v[2], v[3], v[1]));
//	if (q == 6)	fprintf(stderr, "%lf\n", sol);
}

int main() {
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);

	scanf("%d", &tt);
	for (q = 1; q <= tt; q++) {
		read();
		solve();
		printf("Case #%d: %lf\n", q, sol);
	}

	return 0;
}
