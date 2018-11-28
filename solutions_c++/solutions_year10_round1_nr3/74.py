#include <cstdio>
#include <cmath>
using namespace std;

const double z = (sqrt(double(5)) + 1)/2, eps = 1e-12;

long long g(double a, double b) {
	if (b < a) return 0;
	long long c = a*(1 - eps) + 1;
	long long d = b*(1 + eps);
	return d - c + 1;
}

long long f(long long a, long long b) {
	if (a == 0 || b == 0) return 0;
	long long r;
	if (b < a) {
		r = a;
		a = b;
		b = r;
	}
	r = 0;
	for (long long i = 1; i <= a; ++i)
		r += g(double(.5), i/z) + g(i*z, double(b + .5));
	return r;
}

int T, a, b, c, d;

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d%d%d%d", &a, &b, &c, &d), --a, --c;
		printf("%lld\n", f(b, d) + f(a, c) - f(b, c) - f(a, d));
	}
	return 0;
}
