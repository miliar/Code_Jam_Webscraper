#include <iostream>
#include <functional>
#include <algorithm>
#include <vector>
#include <list>
#include <math.h>
#include <cassert>


using namespace std;

double _y(double x, double R_i) {
	return sqrt(R_i*R_i - x*x);
}

double _x(double x, double R_i) {
	return sqrt(R_i*R_i - x*x);
}

class point { 
	public:
		double x, y;
		point operator() (double &_x, double &_y) {
			x = _x; y = _y; return *this;
		}
};

bool inside(point p, double R_i){
	if (R_i*R_i < p.x*p.x + p.y*p.y)
		return false;
	return true;
}

double segment_area(double x1, double y1, double x2, double y2, double R_i) {
	double c = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
	double th = 2 * asin(c/(2*R_i));
	double a = 0.5 * R_i*R_i * (th - sin(th));
//	cerr << "  SEGA: " << a << endl;
	return a;
}

double square_area(double x1, double y1, double x2, double y2, double R_i) {
	point corners[4];
		// 0 -- 1
		// |    |
		// |    |
		// 2 -- 3
	corners[0](x1, y2);
	corners[1](x2, y2);
	corners[2](x1, y1);
	corners[3](x2, y1);

	bool ins[4];
	for (int i=0; i<4; i++) {
		ins[i]=inside(corners[i], R_i);
//		cerr << "  ("<<corners[i].x << "," << corners[i].y << "): " << ins[i] << endl;
	}
	
	if (ins[0] && ins[1] && ins[2] && ins[3] )
		return (x2-x1)*(y2-y1);

	if (!ins[0] && !ins[1] && !ins[2] && !ins[3] )
		return 0;

	if (!ins[0] && !ins[1] && ins[2] && ins[3] ){
		// No top line.
		corners[0].y = _y(corners[0].x, R_i);
		corners[1].y = _y(corners[1].x, R_i);

		return (x2-x1)*0.5*(corners[0].y-corners[2].y + corners[1].y - corners[3].y) + segment_area(corners[0].x,corners[0].y, corners[1].x, corners[1].y, R_i);
	}
	if (ins[0] && !ins[1] && ins[2] && !ins[3] ){
		// No right line
		corners[1].x = _x(corners[1].y, R_i);
		corners[3].x = _x(corners[3].y, R_i);
		
		return (y2-y1)*0.5*(corners[1].x-corners[0].x + corners[3].x - corners[2].x) + segment_area(corners[1].x,corners[1].y, corners[3].x, corners[3].y, R_i);
	}

	if (!ins[0] && !ins[1] && ins[2] && !ins[3] ){
		// Only bottom left
		corners[0].y = _y(corners[0].x, R_i);
		corners[3].x = _x(corners[3].y, R_i);

		return (corners[0].y-corners[2].y)*(corners[3].x-corners[2].x)*0.5 + segment_area(corners[0].x, corners[0].y, corners[3].x, corners[3].y, R_i);
	}
	
	if (ins[0] && !ins[1] && ins[2] && ins[3] ){
		// Top right gone
		corners[0].x = _x(corners[1].y, R_i);
		corners[3].y = _y(corners[1].x, R_i);

		return (x2-x1)*(y2-y1) - (corners[0].x-corners[1].x)*(corners[3].y-corners[1].y)*0.5 + segment_area(corners[0].x, corners[0].y, corners[3].x, corners[3].y, R_i);
	}	

	assert(0);
	return -1;
}

void process_case() {
	double f, R, t, r, g;
	cin >> f >> R >> t >> r >> g;
	g -= 2*f;

	if (g <= 0 ){
		cout << 1 << endl;
		return;
	}
	double R_i = R-t-f;
	double d = g+2*r+2*f;
	double va = 0;
	for (double x=r+f; x<R_i+d; x+=d){
		for (double y=r+f; y<_y(x, R_i)+d; y+=d) {
//			cerr << "X: " << x << " Y: " << y << endl;
			double a = square_area(x,y,x+g, y+g, R_i);
//			cerr << " A: " << a << endl;
			va += a;
		}
	}
	double ta = M_PI * R * R * 0.25;
//	cerr << "TA: " << ta << "VA: " << va << endl;
	cout << 1-(va/ta) << endl;
}

int main() {
	int N;
	cin >> N;
	for (int i=0; i<N; i++){
		cout << "Case #" << i+1 << ": ";
		process_case();
	}
	return 0;
}
