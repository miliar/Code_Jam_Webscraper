#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

#define For(i,n) for (int i = 0; i < n; ++i)
#define FOr(i,a,b) for (int i = a; i < b; ++i)
#define sqr(x) ((x)*(x))

int T, n;
double x[10], y[10], r[10], ans;

double min(double a, double b, double c) {
	if (a < b && a < c) return a;
	return b < c ? b : c;
}

double max(double a, double b) {
	return a < b ? b : a;
}

double dist(int a, int b) {
	return .5*(sqrt(sqr(x[a] - x[b]) + sqr(y[a] - y[b])) + r[a] + r[b]);
}

int main() {
	scanf("%d", &T);
	For(t,T) {
		printf("Case #%d: ", t + 1);
		scanf("%d", &n);
		For(i,n) scanf("%lf%lf%lf", x + i, y + i, r + i);
		if (n <= 2) ans = max(r[0], r[1]);
		else ans = min(max(r[0], dist(1,2)), max(r[1], dist(2,0)), max(r[2], dist(0,1)));
		printf("%lf\n", ans);
	}
	return 0;
}
