/** GCJ 2008: Problem C */

#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;


const double EPS = 1e-7, PI = 3.14159265358979323846;
double f, R, t, r, g;
double rad;


class Point {
	public:
		double x;
		double y;

		Point() {
			x = 0.0;
			y = 0.0;
		}
		
		Point(const Point& point) {
			x = point.x;
			y = point.y;
		}
		
		Point(double xx, double yy) {
			x = xx;
			y = yy;
		}
};


inline double getSegment(const Point& p1, const Point& p2) {
	// cout << "\t\t\t\tp1: (" << p1.x << ", " << p1.y << ")" << endl;
	// cout << "\t\t\t\tp2: (" << p2.x << ", " << p2.y << ")" << endl;

	double length = sqrt((p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y)) / 2.0;
	double radian_angle = asin(length / rad) * 2;
	
	double ret = (rad * rad * 0.5) * (radian_angle - sin(radian_angle));
	
	
	// cout << "\t\t\t\tlength: " << length << " radian_angle: " << radian_angle << " ret: " << ret << endl;
	
	return ret;
}


inline double get_7(const Point& bottomLeft) {
	Point p1, p2;

	p1.x = bottomLeft.x;
	p1.y = sqrt(rad * rad - p1.x * p1.x);

	p2.y = bottomLeft.y;
	p2.x = sqrt(rad * rad - p2.y * p2.y);

	double segment = getSegment(p1, p2);

	double length = p2.x - bottomLeft.x;
	double breadth = p1.y - bottomLeft.y;

	double rect = length * breadth;

	double tri = 0.5 * (p1.y - p2.y) * (p2.x - p1.x);

	return rect - tri + segment;
}


inline double get_5(const Point& bottomLeft, const Point& upLeft) {
	Point p1, p2;

	p1.y = upLeft.y;
	p1.x = sqrt(rad * rad - p1.y * p1.y);
	
	p2.y = bottomLeft.y;
	p2.x = sqrt(rad * rad - p2.y * p2.y);

	double segment = getSegment(p1, p2);

	double length = p2.x - bottomLeft.x;
	double breadth = upLeft.y - bottomLeft.y;

	double rect = length * breadth;

	double tri = 0.5 * (p1.y - p2.y) * (p2.x - p1.x);

	return rect - tri + segment;
}


inline double get_3(const Point& bottomLeft, const Point& bottomRight) {
	Point p1, p2;

	p1.x = bottomLeft.x;
	p1.y = sqrt(rad * rad - p1.x * p1.x);

	p2.x = bottomRight.x;
	p2.y = sqrt(rad * rad - p2.x * p2.x);

	double segment = getSegment(p1, p2);

	double length = bottomRight.x - bottomLeft.x;;
	double breadth = p1.y - bottomLeft.y;

	double rect = length * breadth;

	double tri = 0.5 * (p1.y - p2.y) * (p2.x - p1.x);

	return rect - tri + segment;
}


inline double get_1(const Point& bottomLeft, const Point& bottomRight, const Point& upLeft) {
	Point p1, p2;

	p1.y = upLeft.y;
	p1.x = sqrt(rad * rad - p1.y * p1.y);

	p2.x = bottomRight.x;
	p2.y = sqrt(rad * rad - p2.x * p2.x);

	double segment = getSegment(p1, p2);

	double length = bottomRight.x - bottomLeft.x;
	double breadth = upLeft.y - bottomLeft.y;

	double rect = length * breadth;

	double tri = 0.5 * (p1.y - p2.y) * (p2.x - p1.x);

	return rect - tri + segment;
}	


inline double get_0(const Point& bottomLeft, const Point& upRight) {
	double length = upRight.x - bottomLeft.x;
	double breadth = upRight.y - bottomLeft.y;
	return length * breadth;
}


inline int outside(const Point &p) {
	return (p.x * p.x + p.y * p.y) > rad * rad - EPS;
}


inline double solveRow(Point startBottomLeft) {
	Point bottomLeft(startBottomLeft);
	
	double ret = 0.0;
	while (!outside(bottomLeft)) {
		Point bottomRight(bottomLeft.x + g - 2 * f, bottomLeft.y);
		Point upLeft(bottomLeft.x, bottomLeft.y + g - 2 * f);
		Point upRight(bottomRight.x, upLeft.y);

		// cout << "\t\tbottomLeft: (" << bottomLeft.x << ", " << bottomLeft.y << ")" << endl;
		
		int code = 0;

		if (outside(upRight)) code |= 1;
		if (outside(upLeft))  code |= 2;
		if (outside(bottomRight)) code |= 4;
		
		
		// cout << "\t\t\tcode: " << code << endl;
		
		
		if (code == 0) {
			
			ret += get_0(bottomLeft, upRight);
		
		} else if (code == 1) {
			
			ret += get_1(bottomLeft, bottomRight, upLeft);
		
		} else if (code == 3) {
			
			ret += get_3(bottomLeft, bottomRight);

		} else if (code == 5) {

			ret += get_5(bottomLeft, upLeft);

		} else if (code == 7) {
				
			ret += get_7(bottomLeft);

		} else {
			// cout << "Code " << code << " didn't match any of the cases" << endl;
		}

		// cout << "\t\t\tret: " << ret << endl;


		bottomLeft.x += g + 2 * r;
	}

	return ret;
}


inline double solve() {

	rad = R - t - f;
	if (rad < EPS) return 1.0;
	
	Point bottomLeft(r + f, r + f);

	if (bottomLeft.x + g - 2 * f < bottomLeft.x + EPS) return 1.0;
	if (bottomLeft.y + g - 2 * f < bottomLeft.y + EPS) return 1.0;

	double escape = 0.0;
	int row = 0;
	while (!outside(bottomLeft)) {
		// cout << "\tSolving row: " << row << "(" << bottomLeft.x << ", " << bottomLeft.y << ")" << endl;
		escape += solveRow(bottomLeft);
		bottomLeft.y += g + 2 * r;
		// cout << "\tescape: " << escape << endl;
		row++;
	}

	// cout << "\tOutside the loop: (" << bottomLeft.x << ", " << bottomLeft.y << ")" << endl;


	escape *= 4;
	double area = PI * R * R;

	// cout << "escape: " << escape << " area: " << area << endl;
	
	return (area - escape) / area;
}


int main() {
	int N;
	cin >> N;
	for (int T = 1; T <= N; T++) {
		cin >> f >> R >> t >> r >> g;
		
		//cout << "f: " << f << " R: " << R << " t: " << t << " r: " << r << " g: " << g << endl;
		
		double ret = solve();

		//cout << "Case #" << T << ": " << ret << endl;

		printf("Case #%d: %.6lf\n", T, ret);

		//cout << "\n ----------------------------------------- \n";
	}

	return 0;
}




