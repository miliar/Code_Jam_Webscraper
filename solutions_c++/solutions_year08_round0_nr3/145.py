#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

#define M_PI 3.1415926535897932384626433832795

std::ifstream in( L"C-small.in" );
std::ofstream out( L"C-small.out" );

double seg(double alpha)
{
	return 0.5*(alpha - sin(alpha));
}

double sp(double x, double y)
{
	double top_angle = acos(y);
	double right_angle = acos(x);

	double x1 = sqrt(1 - y*y);
	double y1 = sqrt(1 - x*x);

	double top_s = seg(2*top_angle) * 0.5;
	double right_s = seg(2*right_angle) * 0.5;
	double result = M_PI / 4;
	result -= top_s;
	result -= right_s;
	result -= x*y;
	return -result;
}

bool caps( double & x0, double & y0, double &x1, double & y1, double &hs, double &hns, double sg )
{
	bool cap[2][2];
	cap[0][0] = x0 * x0 + y0 * y0 < 1;
	cap[1][0] = x1 * x1 + y0 * y0 < 1;
	cap[0][1] = x0 * x0 + y1 * y1 < 1;
	cap[1][1] = x1 * x1 + y1 * y1 < 1;
	if( !cap[0][0] ) return true;
	if( cap[1][1] )
	{
		hs += sg * sg;
		return true;
	}
	if( cap[0][1] )
	{
		double xx0 = sqrt(1 - y1*y1);
		double p0 = (xx0-x0)*(y1-y0);
		hns += p0;
		x0 = xx0;
	}
	if( cap[1][0] )
	{
		double yy0 = sqrt(1 - x1*x1);
		double p0 = (yy0-y0)*(x1-x0);
		hns += p0;
		y0 = yy0;
	}

	return false;
}

double solve(double BigR, double SR, double sr, double sg)
{
	if( SR <= 0 ) return 1;
	if( sg <= 0 ) return 1;
	const double cs = sr*2 + sg;
	if( cs == 0 ) return 1;
	
	const int tc = int(ceil(SR / cs));

	double hs = 0,hns = 0;
	for(int gx = 0; gx != tc; ++gx)
	{
		const double px0 = gx * cs + sr;
		const double px1 = px0 + sg;
		if( px0 >= SR )continue;
		const double h0 = sqrt( SR * SR - px0 * px0 );
		int gy = 0;
		if( px1 < SR )
		{
			const double h1 = sqrt( SR * SR - px1 * px1 );
			const int tfc = floor(h1 / cs);

			gy += tfc;
			hs += tfc * sg * sg;
		}
		for(; gy != tc; ++gy)
		{
			const double py0 = gy * cs + sr;
			const double py1 = py0 + sg;

			double x0 = px0 / SR;
			double y0 = py0 / SR;
			double x1 = px1 / SR;
			double y1 = py1 / SR;

			if( caps(x0,y0,x1,y1,hs,hns,sg) ) continue;

			double p1 = sp(x0, y0);
			hns += p1;
		}
	}
	hs += hns * SR * SR;
	hs *= 4;
	return 1 - hs / (M_PI * BigR * BigR);
}

int main(void)
{
	int n = 0;
	in >> n;
	for(int i = 0; i != n; ++i)
	{
		double f, R, t, r, g;
		in >> f >> R >> t >> r >> g;
		out.precision(6);
		out << "Case #" << i+1 << ": " << std::fixed << solve(R, R - t - f, r + f, g - 2*f) << std::endl;
	}
	return 0;
}
