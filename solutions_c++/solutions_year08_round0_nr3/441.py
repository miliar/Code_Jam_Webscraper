#include <cstdio>
#include <cmath>

const double eps = 1e-9;
const double pi = acos(-1.0);

int casei, cases;
double fly, Radius, thick, rad, gap, Rt, ans;

inline void init() {
	scanf("%lf%lf%lf%lf%lf", &fly, &Radius, &thick, &rad, &gap);
}

inline int sgn(double now) {
	if (now > eps) return 1;
	if (now < -eps) return -1;
	return 0;
}

inline double sqr(double now) {
	return now * now;
}

inline double dis(double px, double py) {
	return sqrt(sqr(px) + sqr(py));
}

inline bool calc(double px1, double py1, double px2, double py2, double& area) {
	if (sgn(dis(px2, py2) - Rt) <= 0) {
		area = (px2 - px1) * (py2 - py1); return true;
	}
	if (sgn(dis(px1, py1) - Rt) >= 0) {
		area = 0; return false;
	}

	double tmp, ppx1, ppy1, ppx2, ppy2, theta;
	if (sgn(dis(px1, py2) - Rt) <= 0) {
		ppy1 = py2; ppx1 = sqrt(sqr(Rt) - sqr(ppy1));
		if (sgn(dis(px2, py1) - Rt) <= 0) {
			ppx2 = px2; ppy2 = sqrt(sqr(Rt) - sqr(ppx2));
			area = (px2 - px1) * (py2 - py1) - (px2 - ppx1) * (py2 - ppy2) * 0.5;
		}
		else {
			ppy2 = py1; ppx2 = sqrt(sqr(Rt) - sqr(ppy2));
			area = (ppx1 + ppx2 - px1 - px1) * (py2 - py1) * 0.5;
		}
	}
	else {
		ppx1 = px1; ppy1 = sqrt(sqr(Rt) - sqr(ppx1));
		if (sgn(dis(px2, py1) - Rt) <= 0) {
			ppx2 = px2; ppy2 = sqrt(sqr(Rt) - sqr(ppx2));
			area = (ppy2 + ppy1 - py1 - py1) * (px2 - px1) * 0.5;
		}
		else {
			ppy2 = py1; ppx2 = sqrt(sqr(Rt) - sqr(ppy2));
			area = (ppy1 - py1) * (ppx2 - px1) * 0.5;
		}
	}
	tmp = dis(ppx2 - ppx1, ppy2 - ppy1) * 0.5;
	theta = asin(tmp / Rt);
	area += sqr(Rt) * theta - sqr(tmp) / tan(theta);

	return true;
}

inline void process() {
	if (sgn(fly + fly - gap) >= 0) {
		ans = 1;
		return;
	}
	if (sgn(Radius - thick - fly) <= 0) {
		ans = 1;
		return;
	}
	ans = 0;

	Rt = Radius - thick - fly;
	double x, y, area;
	y = 0;
	while (sgn(Radius - thick - y) > 0) {
		x = 0;
		while (calc(x + rad + fly, y + rad + fly, x + rad + gap - fly, y + rad + gap - fly, area)) {
			ans += area;
			x += rad + rad + gap;
		}
		y += rad + rad + gap;
	}

	ans = ans * 4 / sqr(Radius) / pi;
	ans = 1 - ans;
}

inline void print() {
	printf("Case #%d: %.6lf\n", casei, ans);
}

int main() {
//	freopen("in.txt", "r", stdin);
//	freopen("", "w", stdout);

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c-small.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}
}
