#include <cstdio>
#include <cstddef>
#include <cmath>
#include <cassert>
#include <algorithm>

const long double INF = 1e8;

const size_t NMAX = 3;

size_t N;


inline long double Hypot(long double x, long double y) {
	return sqrtl(x * x + y * y);
}


long double processCase1(long double x, long double y, long double r) {
	return r;
}


long double processCase2(long double x0, long double y0, long double r0, 
						 long double x1, long double y1, long double r1) {
	return std::max(r0, r1);
}


long double processCase3(long double x0, long double y0, long double r0, 
						 long double x1, long double y1, long double r1,
						 long double x2, long double y2, long double r2) {
	const long double r01 = (Hypot(x0 - x1, y0 - y1) + r0 + r1) / 2;
	const long double r12 = (Hypot(x1 - x2, y1 - y2) + r1 + r2) / 2;
	const long double r20 = (Hypot(x2 - x0, y2 - y0) + r2 + r0) / 2;

	long double r = INF;

	r = std::min(r, std::max(r01, r2));
	r = std::min(r, std::max(r12, r0));
	r = std::min(r, std::max(r20, r1));
	
	return r;
}

int main() {
	size_t C;
	scanf("%u", &C);
	long double x0, y0, r0;
	long double x1, y1, r1;
	long double x2, y2, r2;

	for(size_t c = 0; c < C; ++c) {
		long double ans = 0;

		scanf("%u", &N);
		switch( N ) {
		case 1:
			scanf("%Lf%Lf%Lf", &x0, &y0, &r0);
			ans = processCase1(x0, y0, r0);
			break;
		
		case 2:
			scanf("%Lf%Lf%Lf", &x0, &y0, &r0);
			scanf("%Lf%Lf%Lf", &x1, &y1, &r1);
			ans = processCase2(x0, y0, r0, x1, y1, r1);
			break;

		case 3:
			scanf("%Lf%Lf%Lf", &x0, &y0, &r0);
			scanf("%Lf%Lf%Lf", &x1, &y1, &r1);
			scanf("%Lf%Lf%Lf", &x2, &y2, &r2);
			ans = processCase3(x0, y0, r0, x1, y1, r1, x2, y2, r2);
			break;

		default:
			assert( 0 );
		}

		printf("Case #%u: %.6Lf\n", c + 1, ans);
	}

	return 0;
}