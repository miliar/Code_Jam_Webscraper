#include<stdio.h>
#include<math.h>
double rr, g;
const double PI=3.1415926535897932384626433832795;
double area, lx, ly;
void nextpt(double x, double y) {
	area+=lx*y-ly*x;
	lx=x; ly=y;
}

void initarea(double x, double y) {
	area=0;
	lx=x; ly=y;
}

template<class _Ty> inline
_Ty sqr(const _Ty &a) { return a*a; }

template<class _Ty> inline
_Ty abs(const _Ty &a) { return a>=0?a:-a; }

bool isIn(double x, double y) { return sqr(x)+sqr(y)<sqr(rr); }

double another(double one) { return sqrt(sqr(rr)-sqr(one)); }

double arc(double x1, double y1, double x2, double y2) {
	double a1=atan2(y1, x1), a2=atan2(y2, x2);
	double da=abs(a1-a2);
	return sqr(rr)*da/2-abs(x1*y2-x2*y1)/2;
}

double calcarea(double x, double y) {
	if(x>y) {
		double t=x;
		x=y; y=t;
	}

	if(isIn(x+g, y+g)) {			//4
		return sqr(g);
	} else if(isIn(x, y+g)) {		//3
		double x1=another(y+g), y1=another(x+g);
		initarea(x, y);
		nextpt(x+g, y);
		nextpt(x+g, y1);
		nextpt(x1, y+g);
		nextpt(x, y+g);
		nextpt(x, y);
		return abs(area/2)+arc(x1, y+g, x+g, y1);
	} else if(isIn(x+g, y)) {		//2
		double y1=another(x), y2=another(x+g);
		initarea(x, y);
		nextpt(x+g, y);
		nextpt(x+g, y2);
		nextpt(x, y1);
		nextpt(x, y);
		return abs(area/2)+arc(x, y1, x+g, y2);
	} else {						//1
		double y1=another(x), x1=another(y);
		initarea(x, y);
		nextpt(x1, y);
		nextpt(x, y1);
		nextpt(x, y);
		return abs(area/2)+arc(x, y1, x1, y);
	}
}

int main() {
	int N;
	scanf("%d", &N);
	for(int cas=1;cas<=N;cas++) {
		double f, R, t, r;
		scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
		t+=f; r+=f; g-=2*f;
		if(g<=0 || t>=R) {
			printf("Case #%d: %.6lf\n", cas, 1.0);
			continue;
		}
		rr=R-t;

		double sum=0;
		for(double x=r;x<rr;x+=g+2*r)
			for(double y=r;isIn(x, y);y+=g+2*r)
				sum+=calcarea(x, y);
		
		printf("Case #%d: %.6lf\n", cas, 1-sum*4/(PI*R*R));
	}
	return 0;
}