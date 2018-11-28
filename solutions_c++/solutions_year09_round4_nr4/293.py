#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int maxn = 10;

struct Point {
	double x, y;
	
	Point() {
	}
	
	Point(double x, double y) : x(x), y(y) {
	}
	
	double Length() const {
		return sqrt(x * x + y * y);
	}
	
	void Input() {
		scanf("%lf %lf", &x, &y);
	}
};

Point operator - (const Point &a, const Point &b) {
	return Point(a.x - b.x, a.y - b.y);
}

Point posi[maxn];
double radius[maxn];
int n;

double Calc(int a, int b) {
	double r1 = radius[a];
	double r2 = radius[b];
	double d = (posi[a] - posi[b]).Length();
	return (max(r1, r2 - d) + d + max(r2, r1 - d)) / 2;
}

void Solve() {
	scanf("%d", &n);
	int i;
	for (i = 0; i < n; i++) {
		posi[i].Input();
		scanf("%lf", &radius[i]);
	}
	switch (n) {
		case 1 : printf("%.10lf\n", radius[0]); break;
		case 2 : printf("%.10lf\n", max(radius[0], radius[1])); break;
		case 3 : {
			double ans1 = max(Calc(0, 1), radius[2]);
			double ans2 = max(Calc(0, 2), radius[1]);
			double ans3 = max(Calc(1, 2), radius[0]);
			printf("%.10lf\n", min(min(ans1, ans2), ans3)); break;
		} break;
	}
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}