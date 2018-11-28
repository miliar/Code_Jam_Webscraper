#include <vector>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

#define FOR(i,n) for (int i = 0; i < (int) (n); i++)

struct vec2 {
	double x, y;
	vec2(){}
	vec2(double _x, double _y) { x = _x; y = _y; }
};
inline vec2 operator + (const vec2& a, const vec2& b) { return vec2(a.x + b.x, a.y + b.y); }
inline vec2 operator - (const vec2& a, const vec2& b) { return vec2(a.x - b.x, a.y - b.y); }
inline vec2 operator * (const vec2& a, double m) { return vec2(a.x * m, a.y * m); }
inline double lengthSqr(const vec2& a) { return a.x * a.x + a.y * a.y; }
inline double length(const vec2& a) { return sqrt(a.x * a.x + a.y * a.y); }
inline vec2 normalize(const vec2& a) { return a * (1.0 / length(a)); }

inline bool less_eq(double a, double b)
{
	return a < b || (fabs(a-b) < 1e-9);
}

int crossCircles(const vec2& a, double r1, const vec2& b, double r2, vec2 result[])
{
	vec2 h = b - a;
	double d = lengthSqr(h);
	if (fabs(d) < 1e-12) {
		if (fabs(r1-r2) > 1e-9) return 0;
		if (r1 > 1e-9) return -1;
		result[0] = a;
		return 1;
	}
	if (r1 < 1e-9) {
		result[0] = a;
		return (fabs(d - r2*r2) < 1e-9) ? 1 : 0;
	}
	if (r2 < 1e-9) {
		result[0] = b;
		return (fabs(d - r1*r1) < 1e-9) ? 1 : 0;
	}
	d = sqrt(d);
	if (d - r1 - r2 > 1e-9) return 0;
	if (fabs(d - r1 - r2) < 1e-9) {
		result[0] = a + (b-a)*(r1 / (r1+r2));
		return 1;
	}
	double R, r;
	vec2 sA;
	if (r1 > r2) {
		R = r1;
		r = r2;
		sA = a;
	} else {
		R = r2;
		r = r1;
		sA = b;
		h = a - b;
	}
	if (R - d - r > 1e-9) return 0;
	if (fabs(R-d-r) < 1e-9) {
		result[0] = sA + h * (R/d);
		return 1;
	}
	double x = (d*d - r*r + R*R)/(2*d);
	double f = sqrt(4*d*d*R*R - (d*d - r*r + R*R)*(d*d - r*r + R*R))/(2*d);
	vec2 nh = normalize(h);
	vec2 rh(nh.y, -nh.x); 
	vec2 t = sA + nh * x;
	result[0] = t + rh*f;
	result[1] = t - rh*f;
	return 2;
}

const int GEN = 10;
int n;
vec2 a[64];
double dists[64][64], minr[64][64], minrCoeff[64][64];
double r[64];
vec2 x[2], bestx[2];
int used[64];
int plog[6];
double answer;
double rad3;

void generate(void)
{
	n = GEN;
	FOR(i, n) {
		a[i] = vec2(drand48() * 100, drand48() * 100);
		r[i] = 1 + drand48() * 20;
	}
}

int intersect2(int i, int j, int k, double R, vec2& cross)
{
	double r0 = R - r[i];
	double r1 = R - r[j];
	double r2 = R - r[k];
	double L = dists[i][j];
	if (L + r1 < r0) {
		cross = a[i];
		return 1;
	}
	if (L + r0 < r1) {
		cross = a[j];
		return 1; 
	}
	vec2 result[2];
	int n = crossCircles(a[i], r0, a[j], r1, result);
	FOR(ii, n) {
		if (length(result[ii] - a[k]) < r2) {
			cross = result[ii];
			return 2;
		}
	}
	if (n >= 1) {
		
	}
	return 0;
}

bool intersect3(int a0, int a1, int a2, double R, vec2& cross)
{
	double r0 = R - r[a0];
	double r1 = R - r[a1];
	double r2 = R - r[a2];
	double radii[3] = {r0, r1, r2};
	vector<vec2> c;
	c.push_back(a[a0]);
	c.push_back(a[a1]);
	c.push_back(a[a2]);
	int p[3] = { a0, a1, a2 };
	for (int i = 0; i < 3; i++)
		for (int j = i + 1; j < 3; j++) {
			vec2 results[2];
			int n = crossCircles(a[p[i]], radii[i], a[p[j]], radii[j], results);
			FOR(k, n) c.push_back(results[k]);
		}
	for (int k = (int) c.size() - 1; k >= 0; k--) {
		if (less_eq(length(a[a0] - c[k]), radii[0]) && less_eq(length(a[a1] - c[k]), radii[1]) && less_eq(length(a[a2] - c[k]), radii[2]))
		{
			cross = c[k];
			if (k >= 3) return 2;
			return 1;
		}
	}
	return 0;
}

double findMinRadius(int k, int a0, int a1, int a2)
{
	int p[3] = {a0, a1, a2}, pc = 3;
	if (p[1] == p[2]) pc--;
	FOR(zz,2) if (pc > 1 && p[0] == p[1]) {
		p[1] = p[2];
		pc--;
	}
	switch (pc) {
		case 1:
		{
			x[k] = a[p[0]];
			return r[p[0]];
		}
		case 2:
		{
			x[k] = a[p[0]] + (a[p[1]] - a[p[0]]) * minrCoeff[p[0]][p[1]];
			return minr[p[0]][p[1]];
		}
		case 3:
		{
			double maxr = 0;
			FOR(i, 3) maxr = max(maxr, r[p[i]]);
			double l = maxr;
			double r = l;
			
			while (!intersect3(p[0], p[1], p[2], r, x[k])) 
				r *= 2.0;
			while (fabs(l-r) > 1e-9) {
				double m = (r + l) / 2.0;
				if (intersect3(p[0], p[1], p[2], m, x[k])) {
					r = m;
				} else {
					l = m;
				}
			}
			intersect3(p[0], p[1], p[2], (r + l) / 2.0, x[k]);
			return (r + l) / 2.0;
		}
	}
}

void bt(int lev, int last)
{
	if (lev == 6) {
		double R = findMinRadius(1, plog[3], plog[4], plog[5]);
		double temp = max(R, rad3);
		bool good = true;
		FOR(i, n) {
			bool some = false;
			FOR(j, 2) {
				if (less_eq(length(a[i] - x[j]) + r[i], temp))
					some = true;
			}
			if (!some) {
				good = false;
				break;
			}
		}
		if (good && temp < answer) {
			memcpy(bestx, x, sizeof(bestx));
			answer = temp;
		}
		return;
	}
	if (lev == 3) {
		rad3 = findMinRadius(0, plog[0], plog[1], plog[2]);
		last = 0;
	}
	int badmask = (lev < 3) ? (7 << 3) : 7;
	for (int i = last; i < n; i++) {
		if (used[i] & badmask) continue;
		used[i] |= (1 << lev);
		plog[lev] = i;
		bt(lev + 1, i);
		used[i] &= ~(1 << lev);
	}
}

void display(void)
{
	FOR(show, 2) {
		FILE* f = fopen("/home/vesko/tvis", "wt");
		for (int i = 0; i < n; i++)
			fprintf(f, "c %.6lf %.6lf %.6lf\n", a[i].x, a[i].y, r[i]);
		if (show) {
			FOR(i, 2)
				fprintf(f, "c %.6lf %.6lf %.6lf\n", bestx[i].x, bestx[i].y, answer);
		}
		fprintf(f, "d\n");
		fclose(f);
		system("/home/vesko/develop/vis/src/vis /home/vesko/tvis");
	}
}

void solve(bool dodisplay = false)
{
	if (n == 1) {
		answer = r[0];
		x[0] = x[1] = a[0];
		return;
	}
	answer = 1e99;
	FOR(i, n) FOR(j, n) {
		dists[i][j] = length(a[i] - a[j]);
		vector<double> vv;
		vv.push_back(0.0);
		vv.push_back(-r[i]);
		vv.push_back(+r[i]);
		vv.push_back(dists[i][j]);
		vv.push_back(dists[i][j] - r[j]);
		vv.push_back(dists[i][j] + r[j]);
		sort(vv.begin(), vv.end());
		minr[i][j] = (vv[vv.size()-1] - vv[0])/2;
		minrCoeff[i][j] = ((vv[vv.size()-1] + vv[0]) / 2.0) / dists[i][j];
	}
	rad3 = 0;
	bt(0, 0);
	//printf("Answer = %.6lf\n", answer);
	if (dodisplay) display();
}


int xmain(void)
{
	while (1) {
		generate();
		solve();
	}
	return 0;
}

int main(int argc, char** argv)
{
	//freopen("/home/vesko/gcj/d.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	FOR(tc, T) {
		scanf("%d", &n);
		FOR(i, n) scanf("%lf%lf%lf", &a[i].x, &a[i].y, &r[i]);
		solve(argc > 1);
		printf("Case #%d: %.8lf\n", tc + 1, answer);
	}
	return 0;
}
