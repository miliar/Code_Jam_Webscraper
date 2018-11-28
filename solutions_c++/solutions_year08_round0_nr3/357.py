#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

double f, R, t, r, g;

inline bool hit(double x) {
	double a = g+r+r;
	if(x < 0) x = -x;
	x -= int(x / a) * a;
	return x < r+f || x > a-r-f;
}

double mc() {
	int n = 0, p = 0;
	for(int i=0; i<100000000; i++) {
		double x = (double)rand() / RAND_MAX * R * 2 - R, y = (double)rand() / RAND_MAX * R * 2 - R;
		if(x*x + y*y <= R*R) {
			n ++;
			if(x*x + y*y > (R-t-f)*(R-t-f) || hit(x) || hit(y))
				p ++;
		}
	}
	return (double)p / n;
}

double circleCut(double r, double x1, double x2) {
	double a1 = r*r/2*acos(x1/r) - x1*sqrt(r*r-x1*x1)/2;
	return a1 - (r*r/2*acos(x2/r) - x2*sqrt(r*r-x2*x2)/2);
}

double prob() {
	double s = 0, a = g-f-f, i=R-t-f;
	for(double x = r+f; x < i; x += g+r+r)
		for(double y = r+f; x*x+y*y < i*i; y += g+r+r)
			if((x+a)*(x+a) + (y+a)*(y+a) <= i*i)
				s += a*a;
			else
				if((x+a)*(x+a) + y*y < i*i)
					if(x*x + (y+a)*(y+a) < i*i) {
						double x1 = sqrt(i*i - (y+a)*(y+a));
						s += circleCut(i, x1, x+a) - (x+a-x1)*y + (x1-x)*a;
					}
					else
						s += circleCut(i, x, x+a) - y*a;
				else {
					double x1 = sqrt(i*i - y*y);
					if(x*x + (y+a)*(y+a) < i*i)
						s += circleCut(i, y, y+a) - x*a;
					else
						s += circleCut(i, x, x1) - (x1-x)*y;
				}
	cerr <<s <<endl;
	return 1 - s*4 / (acos(0.0)*2*R*R);
}

int main(int argc, char* argv[]) {
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		cin >>f >>R >>t >>r >>g;
		cout <<"Case #" <<i+1 <<": " <<prob() <<endl;
	}
}