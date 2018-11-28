#include <iostream>
#include <cmath>
using namespace std;

const int I = 1579135;

int main()
{
    int n;
    cin >> n;
    for (int k = 1; k <= n; ++k)
    {
	double f, R, t, r, g;
	cin >> f >> R >> t >> r >> g;
	double s = g + 2.*r;
	R /= s; t /= s; r /= s; f /= s;
	r += f; t += f;
	double p = 0., q = 0.;
	double z = R - t;
	double m = floor(z)*(1. - 2.*r);
	z -= floor(z);
	if (z >= 1. - r)
	    m += 1. - 2.*r;
	else if (z > r)
	    m += z - r;
	if (r < .5)
	{
	    for (int i = 0; i < I; ++i) {
		double x = (i + .5)*m/I;
		x /= 1. - 2.*r;
		double h = x - floor(x);
		x = floor(x) + h*(1. - 2.*r) + r;
		double l = sqrt((R - t)*(R - t) - x*x);
		p += floor(l)*(1. - 2.*r);
		l -= floor(l);
		if (l >= 1. - r)
		    p += 1. - 2.*r;
		else if (l > r)
		    p += l - r;
	    }
	}
	q = M_PI/4. * R*I*R/m;
	cout << "Case #" << k << ": ";
	cout.flags(ios::fixed);
	cout.precision(8);
	cout << (1. - p/q) << endl;
    }
}
