#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std ;

#define	FILE_IN			"C-small.in"
#define	FILE_OUT		"C-small.out"
#define	INF					1000000
#define MIN(a, b)	((a) < (b) ? (a) : (b))
#define ch2int(c) ((c) - '0')

#define eps	1e-9
#define eq(a, b) ((a) > (b) - eps && (a) < (b) + eps)
#define ge(a, b) ((a) > (b) - eps)
#define le(a, b) ((a) < (b) + eps)
#define in(a, x, y) ((ge(a, x) && le(a, y)) || (ge(a, y) && le (a, x)))

ifstream inf(FILE_IN) ;
ofstream out(FILE_OUT) ;

double f, R, t, r, g ;

double pR, L ;

double inter(double x1, double y1, double x2, double y2) {
	if (eq(x1, x2)) {
		return sqrt(pR * pR - x1 * x1) ;
	}
	else {
		return sqrt(pR * pR - y1 * y1) ;
	}
}

double areacircle(double x1, double x2) {
	double fi1 = asin(x1 / pR), fi2 = asin(x2 / pR) ;
	double tmp = pR * pR / 4 * (sin(2 * fi2) - sin(2 * fi1)) + pR * pR / 2 * (fi2 - fi1) ;
	if (tmp > 0) return tmp ;
	else return -tmp ;
	
}

double calc(double x, double y) {
	double y1 = inter(x, y, x, y + L) ;
	double x1 = inter(x, y + L, x + L, y + L) ;
	double y2 = inter(x + L, y, x + L, y + L) ;
	double x2 = inter(x, y, x + L, y) ;

	if (in(x1, x, x + L)) {
		if (in(y2, y, y + L)) {
			return (x1 - x) * L + areacircle(x1, x + L) - y * (x + L - x1) ;
		}
		else {
			return (x1 - x) * L + areacircle(x1, x2) - y * (x2 - x1) ;
		}	
	}
	else {
		if (in(y1, y, y + L)) {
			if (in(y2, y, y + L)) {
				return areacircle(x, x + L) - y * (x + L - x) ;
			}
			else {
				return areacircle(x, x2) - y * (x2 - x) ;
			}
		}
		else {
			if (ge(y1, y + L)) {
				return L * L ;
			}
			else {
				return 0.0 ;
			}			
		}
	}		
}

bool isinside(double x, double y) {
	return eq(calc(x, y), L * L) ;
}

int main(int argc, char **argv) {
	int num_tests ;
	inf >> num_tests ;
	for (int test = 1 ; test <= num_tests ; test ++) {
		inf >> f >> R >> t >> r >> g ;
		
		L = g - 2 * f ;
		pR = R - t - f ;		
		
		double curx = r, cury = r ;
		int cnt = 0 ;
		double area = 0.0 ;
		while (le(curx + f, R)) {
			cury = r ;
			while (le(cury + f, R)) {
				area += calc(curx + f, cury + f) ;
				cury += g + 2 * r ;
			}
			curx += g + 2 * r ;
		}
		out << "Case #" << test << ": " << (1 - 4 * area / (R * R * M_PI)) << endl ;
	
	}
	out.flush() ;
	out.close() ;
	return 0 ;
}


