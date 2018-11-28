#include <cstdio>
#include <cassert>
#include <cmath>

typedef long double LD;
const LD EPS=1e-9;
const LD PI = 2.*acos(0.);

struct PT { LD x,y; PT(LD a=0.0, LD b=0.0) : x(a), y(b) {} };
LD trap(PT& a, PT& b) { return (0.5*(b.x - a.x)*(b.y + a.y)); }
LD dot(PT& a, PT& b) { return a.x*b.x + a.y*b.y; }
LD length(PT& a) { return sqrt(a.x*a.x + a.y*a.y); }
LD angle(PT& a, PT& b) { return acos(dot(a,b)/(length(a)*length(b))); }
LD triarea(PT& a, PT& b, PT& c) { return fabs(trap(a,b)+trap(b,c)+trap(c,a)); }
LD polyarea(int n, PT a=PT(), PT b=PT(), PT c=PT(), PT d=PT(), PT e=PT()) {
	PT vin[10] = {a,b,c,d,e};
	LD ret = 0.0;
	for (int i=0;i<n;++i) ret += trap(vin[i], vin[(i+1)%n]);
	return fabs(ret);
}

LD f,R,t,r,g,realr;
bool inside(LD x, LD y) { return x*x + y*y <= realr*realr + EPS; }
bool inside(PT a) { return inside(a.x,a.y); }
LD other(LD x) { // clips a coordinate to the boundary of the circle
	LD rootof = realr*realr - x*x;
	if (!(rootof > EPS)) return 0.;
	return sqrtl(rootof);
}
LD circular_segment(PT& a, PT& b) {// two points on the circumference.
	LD theta = angle(a,b);
	return realr*realr/2. * (theta - sin(theta));
}
bool oncircle(PT a) {
	if (fabs(realr*realr - (a.x*a.x + a.y*a.y) )>1e-9) return false;
	return 1;
}


int main() {
	int N;
	scanf("%d", &N);
	for (int z=1;z<=N;++z) {
		scanf("%llf %llf %llf %llf %llf", &f, &R, &t, &r, &g);
		printf("Case #%d: ", z);
		if (g<=2.*f) { printf("1.000000\n"); continue; }
		r += f;
		t += f;
		g -= 2.*f;
		realr = R-t;
		
		LD total = PI*R*R;
		LD bad = 0.;
		for (LD x=r; inside(x,0) ; x += g + 2.*r) {
			for (LD y = r; inside(x,y) ; y += g + 2.*r) {
				int cnt = 0;
				PT ul(x,y);     bool in_ul = inside(ul); cnt += in_ul;
				PT dl(x,y+g);   bool in_dl = inside(dl); cnt += in_dl;
				PT ur(x+g,y);   bool in_ur = inside(ur); cnt += in_ur;
				PT dr(x+g,y+g); bool in_dr = inside(dr); cnt += in_dr;
				if (cnt==4) { // Case 0: none out
					bad += g*g;
				}
				else if (cnt==3 && !in_dr) { // Case 1: down right out
					PT ex0(dr.x,other(dr.x));
					PT ex1(other(dr.y),dr.y);
					bad += polyarea(5,ul,ur,ex0,ex1,dl) + circular_segment(ex0,ex1);
				}
				else if (cnt==2 && !in_ur && !in_dr) { // Case 2: two out
					PT ex0(other(ur.y),ur.y);
					PT ex1(other(dr.y),dr.y);
					bad += polyarea(4,ul,ex0,ex1,dl) + circular_segment(ex0,ex1);
				}
				else if (cnt==2 && !in_dl && !in_dr) { // Case 3: two out
					PT ex0(dr.x,other(dr.x));
					PT ex1(dl.x,other(dl.x));
					bad += polyarea(4,ul,ur,ex0,ex1) + circular_segment(ex0,ex1);
				}
				else if (cnt==1 && in_ul) { // Case 4: one out
					PT ex0(other(ur.y), ur.y);
					assert(oncircle(ex0));
					PT ex1(dl.x, other(dl.x));
					assert(oncircle(ex1));
					bad += polyarea(3,ul,ex0,ex1) + circular_segment(ex0,ex1);
				}
				else assert(false);
			}
		}
		printf("%.6llf\n", (total-4.*bad)/total + EPS);
	}
}
