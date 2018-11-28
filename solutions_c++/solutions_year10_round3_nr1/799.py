/*
	2010-05-22 Google Code Jam Round 1C Question A
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <complex>   // for data-structure complex -> Point
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

const double EPS = 1e-7; // usually use 1e-7, 1e-9, 1e-11, 1e-13, ...
int dblcmp (double a, double b) {
	if (fabs (a-b) < EPS) return 0;
	return a < b ? -1 : 1;
}
typedef complex<double> Point; // or complex<int>, but not recommanded;
double cross (Point a, Point b) {
	// casting can be omitted if Point is complex<double>
    return (double) real(a) * imag(b) - (double) imag(a) * real(b);
}

int ccw (Point a, Point b, Point c) { // short version
	return dblcmp (cross (b-a, c-a), 0);
}
bool properIntersectSS (const Point &s0, const Point &s1, const Point &t0, const Point &t1) {
    return ccw (s0, s1, t0) * ccw (s0, s1, t1) < 0 &&
           ccw (t0, t1, s0) * ccw (t0, t1, s1) < 0;
}

Point segs [1024][2];

int main()
{
	int kase, serial=0, n, soln, Ay, By;
	Point A, B;
	scanf ("%d", &kase);
	while (kase--)
	{
		// BEGIN test case
		soln = 0;
		scanf ("%d", &n);
		for (int i=0; i<n; ++i) {
			scanf ("%d %d", &Ay, &By);
			segs[i][0] = A = Point (0, Ay);
			segs[i][1] = B = Point (100, By);
			for (int k=0; k<i; ++k) {
				if (properIntersectSS (A, B, segs[k][0], segs[k][1]))
					++soln;
			}
		}

		printf ("Case #%d: %d\n", ++serial, soln);
		// END test case
	}
	return 0;
}
