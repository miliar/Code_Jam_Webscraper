#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <algorithm>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

typedef long double real;
#define eps 1e-9L
#define pi (2.0L * acosl(0.0L))

struct pnt {
	real x, y;
	pnt() { }
	pnt(real _x, real _y) : x(_x), y(_y) { }
	
	pnt operator + (const pnt& p) const {
		return pnt(x + p.x, y + p.y);
	}
	pnt operator - (const pnt& p) const {
		return pnt(x - p.x, y - p.y);
	}
	pnt operator * (real n) const {
		return pnt(x * n, y * n);
	}
	
	real operator ! () const {
		return x*x + y*y;
	}
};

inline real sqr(real x) { return x * x; }

inline bool inside(const pnt& p, real r) {
	return !p + eps < sqr(r);
}

inline real vec(const pnt& p1, const pnt& p2) {
	return p1.x * p2.y - p1.y * p2.x;
}

void intersect(const pnt& p1, const pnt& p2, real r, pnt& out) {
	real ll = 0.0L, rr = 1.0L;
	bool f = inside(p1, r);
	while(rr - ll > eps) {
		real m = (rr + ll) / 2.0L;
		out = p1 * m + p2 * (1.0L - m);
		if(inside(out, r) ^ f) ll = m;
		else rr = m;
	}
	out = p1 * ll + p2 * (1.0L - ll);
}

inline real gy(real x) {
	return x > 0.0L ? x : 0.0L;
}

int main() {
	int tt = 1, tc, i, j;
	for(scanf("%d", &tc); tt <= tc; tt++) {
		real f, t, R, r, g, rr;
		scanf("%Lf%Lf%Lf%Lf%Lf", &f, &R, &t, &r, &g);
		rr = R - t - f;
		pnt p1, p2;
		real S = 0.0L;
		if(g + eps > 2.0L * f) {
			for(p1.y = r + f; p1.y + eps < rr; p1.y += 2.0L*r + g)
				for(p1.x = r + f; p1.x + eps < rr; p1.x += 2.0L*r + g) {
					if(!inside(p1, rr)) break;
					p2 = p1 + pnt(g - 2.0L*f, g - 2.0L*f);
					if(inside(p2, rr)) {
						S += sqr(g - 2.0L*f);
						continue;
					}
				
					pnt pts[5] = { p1, pnt(p1.x, p2.y), p2, pnt(p2.x, p1.y), p1 };
//					fprintf(stderr, "(%Lf, %Lf) - (%Lf, %Lf)\n", p1.x, p1.y, p2.x, p2.y);
					real ss = 0.0L;
					pnt pp[4];
					int cc = 0;
					for(i = 0; i < 4; i++) {
						bool f1 = inside(pts[i], rr), f2 = inside(pts[i+1], rr);
						if(!f1 && !f2) continue;
						if(f1 && f2) {
							ss += vec(pts[i], pts[i+1]);
							continue;
						}
						intersect(pts[i], pts[i+1], rr, pp[cc++]);
						if(f1) ss += vec(pts[i], pp[cc-1]);
						else ss += vec(pp[cc-1], pts[i+1]);
					}
					assert(cc == 2);
//					fprintf(stderr, "!!(%Lf, %Lf) - (%Lf, %Lf)\n", pp[0].x, pp[0].y, pp[1].x, pp[1].y);
					ss -= (atan2l(pp[0].y, pp[0].x) - atan2l(pp[1].y, pp[1].x)) * sqr(rr);
					S += fabsl(ss) / 2.0L;
				}
		}
		real S1 = pi * sqr(R);
		printf("Case #%d: %.10Lf\n", tt, gy(1.0L - 4.0L*S/S1));
	}
	return 0;
}
