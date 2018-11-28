#include <cstdio>
#include <cmath>

using namespace std;

template<typename T> T max (T a, T b) {
	if (a > b)
		return a;
	return b;
}

long double solve_quar(long double a, long double b, long double c) {
	long double d = b*b - static_cast<long double>(4.0)*a*c;
	if (d >= 0) {
		d = sqrtl(d);
		return max((-b+d)/(static_cast<long double>(2.0)*a), (-b+d)/(static_cast<long double>(2.0)*a));
	}
	return -1;
}

long double sqr(long double x) {
	return x*x;
}

int main() {
	freopen("B-large.in", "r", stdin); // B-small-attempt0.in // C-large.in
	freopen("B-large.out", "w", stdout);
	int case_n;
	scanf("%d", &case_n);
	for (int case_i = 1; case_i <= case_n; ++case_i) {
		int N, A;
		long double D, t[2005], x[2005], a;
		scanf("%Lf%d%d", &D, &N, &A);
		for (int i = 0; i < N; ++i)
			scanf("%Lf%Lf", &t[i], &x[i]);
		printf("Case #%d:\n", case_i);
		for (int accel_a = 0; accel_a < A; ++accel_a) {
			scanf("%Lf", &a);
			long double max_t = static_cast<long double>(0.0), tmp_t, tmp_t2;
			for (int i = 0; i < N; ++i) {
				if (x[i] <= D) {
					tmp_t = sqrtl(x[i] * static_cast<long double>(2.0) / a);
					tmp_t = t[i] - tmp_t;
					if (tmp_t > max_t)
						max_t = tmp_t;
				} else {
					if (i > 0) {
						int j = i-1;
						while (j >= 0 && x[j] == x[i])
							--j;
						if (j < 0) {
							max_t = 0;
						} else {
							if (x[i-1] <= D) {
								tmp_t = sqrtl(D * static_cast<long double>(2.0) / a);
								tmp_t = (D - x[j]) / (x[i] - x[j]) * (t[i] - t[j]) + t[j] - tmp_t;
								if (tmp_t > max_t)
									max_t = tmp_t;
							}
						}
					} else {
						max_t = static_cast<long double>(0.0);
					}
					break;
				}
			}
			printf("%Lf\n", max_t + sqrtl(D * static_cast<long double>(2.0) / a));
		}

	}
	return 0;
}