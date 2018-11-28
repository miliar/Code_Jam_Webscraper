#include <cstdio>
#include <map>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

#define CODE D-small-attempt0

#define INPUT QUOTE(CODE)".in"
#define OUTPUT QUOTE(CODE)".out"
#define _QUOTE(x) #x
#define QUOTE(x) _QUOTE(x)

#define MAXN 2
#define MAXM 10

typedef pair<int, int> point;
typedef pair<double, double> pointf;
#define X first
#define Y second

int n, m;
point P[MAXN];
point Q[MAXM];

point vec(point a, point b) {
	return point(b.X - a.X, b.Y - a.Y);
}
pointf vec(pointf a, pointf b) {
	return pointf(b.X - a.X, b.Y - a.Y);
}

int cross(point a, point b) {
	return a.X * b.Y - a.Y * b.X;
}
int dot(point a, point b) {
	return a.X * b.X + a.Y * b.Y;
}

void read() {
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; ++i)
		scanf("%d %d", &P[i].X, &P[i].Y);
	for (int i = 0; i < m; ++i)
		scanf("%d %d", &Q[i].X, &Q[i].Y);
}

double dist(pointf a, pointf b) {
	pointf v = vec(a, b);
	return hypot(v.X, v.Y);
}

double sliceArea(double r, double ang) {
	double segArea = r * r * ang / 2;
	double triArea = r * r * sin(ang) / 2;
	return segArea - triArea;
}

double angle(point o, point a, point b) {
	a = vec(o, a);
	b = vec(o, b);
	double aa = atan2(a.Y, a.X);
	double ab = atan2(b.Y, b.X);
	double ang = aa - ab;
	if (ang < 0)
		ang += 2 * M_PI;
	if (ang > M_PI)
		ang = 2 * M_PI - ang;
	return ang;
}

double area(point bucket) {
	double a0 = angle(P[0], bucket, P[1]) * 2;
	double a1 = angle(P[1], bucket, P[0]) * 2;
	double area = sliceArea(dist(P[0], bucket), a0) + sliceArea(dist(P[1], bucket), a1);
	return area;
}

void solve() {
	read();
	for (int i = 0; i < m; ++i) {
		double a = area(Q[i]);
		printf(" %.7lf", a);
	}
}

int main() {
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		printf("Case #%d:", i);
		solve();
		printf("\n");
	}
	return 0;
}
