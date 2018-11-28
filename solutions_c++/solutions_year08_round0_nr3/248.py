/* kanekoC.cc
 */
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cassert>
// #define DETAIL
using namespace std;
int N;
double R, t, r, g;
const double pi = 3.14159265358979;
double area(double x0, double y0, double x1, double y1,
	    double x2, double y2) 
{
    double Rtf = R-t;
    double t2 = asin(y2/Rtf), t1 = asin(y1/Rtf), t0 = asin(y0/sqrt(x0*x0+y0*y0));
    double all = pi*Rtf*Rtf*(t2-t1)/2/pi;
    assert(t1 < t2);
    double l = fabs(x0*y1-x1*y0)/2.0, r = fabs(x0*y2-x2*y0)/2.0; 
    if (t1 <= t0 && t0 <= t2) {
	assert(all >= l+r);
	return all - l - r;
    }
    assert(t0 < t1);
    assert(all + l >= r);
    return all + l - r;
}
double area(double x0, double y0, double x1, double y1) 
{
    return area(x0, y0, x1, y0, x0, y1);
}
double safe_area(double x0, double y0)
{
    // triangle
    double Rt2 = (R-t)*(R-t);
    if (Rt2 <= y0*y0 || Rt2 <= x0*x0) return 0;
    if (x0 < y0) swap(x0, y0);
    double x1 = sqrt(Rt2-(y0*y0)), y1 = sqrt(Rt2-(x0*x0));
    if (x1 <= x0+g && y1 <= y0+g) {
#ifdef DETAIL
	cerr << "  s3 " << x1 << " " << y1 << " "
	     << endl;
#endif
	return area(x0, y0, x1, y1);
    }

    // 
    double y2 = y0+g, x2 = sqrt(Rt2-y2*y2);
    assert(x0 <= x2 && x2 <= x0+g);
    if (x1 <= x0+g) {
#ifdef DETAIL
	fprintf(stderr, "  s4 %lf %lf  %lf %lf\n", x1, y0, x2, y2);
#endif
	return (x2-x0)*g/2.0 + area(x0, y0, x1, y0, x2, y2);
    }
    // 
    double x4 = x0+g, y4 = sqrt(Rt2-x4*x4);
    double s = area(x0, y0, x4, y4, x2, y2);
    assert(y0 <= y4 && y4 <= y0+g);
    assert(x2 <= x4 && y2 >= y4);
#ifdef DETAIL
    cerr << "  s5 " << x4 << " " << y4 << " " << x2 << " " << y2 << endl;
#endif
    return s + g*(y4-y0)/2.0 + g*(x2-x0)/2.0;
}
int main()
{
    cerr << setprecision(6);
    cin >> N;
    for (int i=0; i<N; ++i) {
	double f;
	cin >> f >> R >> t >> r >> g;
	double denom = pi*R*R/4.0, n = 0, Rt2 = (R-t-f)*(R-t-f);
	int ns = 0;
	if (f*2 < g) {
	    g -= 2*f; t += f; r += f;
	    for (int yi=0; true; ++yi) {
		double y = yi*(2*r+g)+r;
		if (y >= R-t) break;
		for (int xi=0; ; ++xi) {
		    double x = xi*(2*r+g)+r;
		    if (x*x+y*y>=Rt2) break;
		    double x1 = x+g, y1 = y+g;
		    if (x1*x1 + y1*y1 < Rt2) {
			++ns; // square
			continue;
		    }
#ifdef DETAIL
		    fprintf(stderr, "box %lf %lf %lf %lf\n", x, y, x+g, y+g);
#endif
		    double s = safe_area(x, y);
#ifdef DETAIL
		    cerr << "  => " << s << endl;
#endif
		    n += s;
		}
	    }
	    n += g*g*ns;
	}
	printf("Case #%d: %.10lf\n", i+1, (denom-n)/denom);
    }
}
