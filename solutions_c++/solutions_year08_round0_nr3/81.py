#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

double f, R, t, r, g;

const double PI = 3.1415926535897932384626433832795;

void input() {
	cin >> f >> R >> t >> r >> g;
}


double a, b, c;

void calceasy() {
	a = min(r + f, r+g/2);
	b = max(0.0, g-2*f);
	c = max(0.0, R - t - f);
}

bool isin(double x, double y) {
	return x*x + y*y < c*c;
}

double arc(double x) {
	double y = sqrt(c*c - x*x);
	return c*c*atan2(y,x)/2 - x*y/2;
}

double getintersection(double x1, double y1, double x2, double y2) {
	if(isin(x1,y1)) {
		if(isin(x2,y1)) {
			if(isin(x1,y2)) {
				if(isin(x2,y2)) {
					return (x2-x1)*(y2-y1);					
				} else {
					double ix1 = sqrt(c*c - y2*y2);
					return (ix1 - x1) * (y2-y1) + arc(ix1) - arc(x2) - (x2-ix1)*y1;
				}
			} else {
				return arc(x1) - arc(x2) - (x2-x1)*y1;
			}
		} else {
			if(isin(x1,y2)) {
				double ix1 = sqrt(c*c - y2*y2);
				double ix2 = sqrt(c*c - y1*y1);
				return (ix1 - x1) * (y2-y1) + arc(ix1) - arc(ix2) - (ix2-ix1) * y1;
			} else {
				double ix2 = sqrt(c*c - y1*y1);
				return arc(x1) - arc(ix2) - (ix2-x1)*y1;
			}
		}
	} else {
		return 0;
	}
}

int main() {
	int casen;
	cin >> casen;
	for(int casei=1;casei<=casen;casei++) {
		input();
		calceasy();
		
		double area = 0;
		for(double x1 = a; x1 < c; x1 += b+2*a) 
			for(double y1 = a; y1 < c; y1 += b+2*a) 
				area += getintersection(x1,y1,x1+b,y1+b);
		
		printf("Case #%d: %.6f\n", casei, 1- area*4 / (PI * R*R));
	}
	return 0;
}
