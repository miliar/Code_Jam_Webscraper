#include<iostream>
#include<math.h>
#include<string.h>

using namespace std;

const double pi = atan(1.0)*4;

double cross(double x0, double y0, double x1, double y1)
{
	return x0*y1-x1*y0;
}

double sq(double x0, double y0, double x1, double y1)
{
	return fabs(cross(x0, y0, x1, y1))/2.0;
}

int solve()
{
	double g, R, r, f, t;
	cin >> f >> R >> t >> r >> g;
	
	double x0, x1, y0, y1, lim;
	double k, x2, x3, y2, y3, len0, len1, sum, s;
	int i, j;
	
	if (f*2>g-1e-10) {
		cout << "1.000000" << endl;
		return 0;
	}
	
	sum = 0.0;
	s = (g-f-f)*(g-f-f);
	lim = R-t-f;
	for (i=0; ; i++) {
		x0 = (r*2+g)*i+r;
		x1 = x0+g;
		x0 += f;
		x1 -= f;
		if (x0>lim) break;
		for (j=0; ; j++) {
			y0 = (r*2+g)*j+r;
			y1 = y0+g;
			y0 += f;
			y1 -= f;
			if (y0>lim) break;
			
			len0 = sqrt(x0*x0+y0*y0);
			if (len0>lim) break;
			len1 = sqrt(x1*x1+y1*y1);
			if (len1<lim) {
				sum += s;
				continue;
			}
			
			//cout << i << " " << j << endl;
			
			k = 0.0;
			if (sqrt(x0*x0+y1*y1)<lim) {
				x2 = sqrt(lim*lim-y1*y1);
				y2 = y1;
				k -= sq(x0, y0, x0, y1);
				k += sq(x0, y1, x2, y2);
				//cout << "! " << x0 << " " << y1 << endl;
			}
			else {
				x2 = x0;
				y2 = sqrt(lim*lim-x0*x0);
				k -= sq(x0, y0, x2, y2);
			}
			if (sqrt(x1*x1+y0*y0)<lim) {
				x3 = x1;
				y3 = sqrt(lim*lim-x1*x1);
				k -= sq(x0, y0, x1, y0);
				k += sq(x1, y0, x3, y3);
			}
			else {
				x3 = sqrt(lim*lim-y0*y0);
				y3 = y0;
				k -= sq(x0, y0, x3, y3);
			}
			
			//cout << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
			
			k += lim*lim*asin(sq(x2, y2, x3, y3)*2/lim/lim)/2.0;
			/*
			cout << (x2*y2+(x3-x2)*(y2+y3)-x3*y3)/2 << endl;
			cout << sq(x2, y2, x3, y3) << endl;
			
			cout << atan2(y3, x3) << " " << asin(y3/lim) << " " << pi/2 << endl;
			cout << asin(sq(x2, y2, x3, y3)*2/lim/lim) << " " << atan2(y2, x2)-atan2(y3, x3) << endl;
			*/
			
			//cout << lim*lim*asin(sq(x2, y2, x3, y3)*2/lim/lim)/2.0 << endl;
			//cout << i << " " << j << " " << k << endl;
			sum += k;
		}
	}
	
	//cout << k << endl;
	//cout << lim*lim*pi/4 << endl;
	
	cout << 1.0-sum/(R*R*pi/4.0) << endl;
	
	return 0;
}

int main()
{
	cout.precision(6);
	cout.setf(ios::fixed);
	
	int c, cc=0;
	cin >> c;
	while (c--) {
		cout << "Case #" << ++cc << ": ";
		solve();
	}
	return 0;
}
