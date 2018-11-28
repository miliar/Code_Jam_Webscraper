#include <cstdio>
#include <math.h>
#include <string.h>
#define feq(x,y) (fabs((x)-(y))<eps)
#define flt(x,y) ((x)<(y)-eps)
#define fgt(x,y) ((x)>(y)+eps)
#define fle(x,y) ((x)<(y)+eps)
#define fge(x,y) ((x)>(y)-eps)
using namespace std;
const double inf = 1e40, eps = 1e-9;
struct P{
	double x, y;
	P(){ }
	P(double x,double y):x(x),y(y){ }
	P operator+(P p){ return P(x+p.x, y+p.y); }
	P operator-(P p){ return P(x-p.x, y-p.y); }
	P operator*(double k){ return P(x*k, y*k); }
	double operator*(P p){ return x*p.x + y*p.y; }
	double operator^(P p){ return x*p.y - y*p.x; }
	double len(){ return sqrt(x*x+y*y); }
	double bear(){ return atan2(y,x); }
	bool operator<(const P &p)const {       // For sort: by x then y
		if (feq(x,p.x)) return flt(y,p.y);
		return flt(x,p.x);
	}
	bool operator==(const P &p)const { return feq(x,p.x) && feq(y,p.y); }
	P rot(){ return P(-y,x); }      // Rotating CCW for  90 degree
	P rot(double the) {     // Rotate CCW for  the radian
		return P(x*cos(the)-y*sin(the), y*sin(the)+x*cos(the));
	}
};
// Segment(Line)-Segment(Line) Intersection
// Answer = a+ab*s   c+cd*t
// Return TRUE <=> Valid Intersection
// CAUTION:  Check valid values of    s and t
bool inter(P a, P b, P c, P d) {
	P cd = d-c, ab = b-a;
	if (feq(cd^ab, 0))      return 0;
	double t = ((a^ab) - (c^ab)) / (cd^ab);
	double s = ((c^cd) - (a^cd)) / (ab^cd);
	if (flt(t,0) || fgt(t,1))       return 0;
	if (flt(s,0) || fgt(s,1))       return 0;
	return 1;
}

int main(){
	int T, ca = 0;
	scanf("%d", &T);
	while (T--){
		int n;
		P la[1010], ra[1010];
		scanf("%d", &n);
		for (int i=0; i<n; i++){
			int y1 ,y2;
			scanf("%d%d", &y1, &y2);
			la[i] = P(0, y1);
			ra[i] = P(10, y2);
		}

		int res, c = 0;
		for (int i=0; i<n; i++)
			for (int j=i+1; j<n; j++)
				if (inter(la[i], ra[i], la[j], ra[j]))
					c++;
		printf("Case #%d: %d\n", ++ca, c);
	}
	return 0;
}
