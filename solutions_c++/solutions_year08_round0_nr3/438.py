#include <math.h>
#include <iostream>
#include <ios>
#include <sstream>
#include <iomanip>
#include <queue>
#include <tr1/unordered_map>
using namespace std;
using namespace std::tr1;

istream& in = cin;
ostream& out = cout;

static inline double cint(double r, double x, double y)
{
	double xr = x / r;
	double rrxx = r * r - x * x;
	if(xr > 1.0 || rrxx < 0.0)
		return r * r * M_PI / 4.0 - x * y;
	else
	{
		return (x * sqrt(r * r - x * x) + r * r * asin(xr)) / 2.0 - x * y;
	}
}

static inline double cint(double r, double x1, double x2, double y)
{
	if(x1 >= x2)
		return 0.0;

	double xr = x2 / r;
	double rrxx = r * r - x2 * x2;
	
	if(xr > 1.0 || rrxx < 0.0)
		return r * r * M_PI / 4.0 - x2 * y - cint(r, x1, y);
	else
	{
		return (x2 * sqrt(r * r - x2 * x2) - x1 * sqrt(r * r - x1 * x1) + r * r * (asin(xr) - asin(x1 / r))) / 2.0 + (x1 - x2) * y;
	}
}

int main(int argc, char** argv)
{
	int N;
	in >> N;
	for(int cas = 0; cas < N; ++cas)
	{
		double f, R, t, r, g;
		in >> f >> R >> t >> r >> g;
		
		double ir = R - t - f;
		
		double margin = r + f;
		double size = 2*r + g;
		double body = size - 2 * margin;
		
		int totfull = 0;
		double totarea = 0.0;
		
//		cerr << "ir = " << ir << " margin = " << margin << " body = " << body << " size = " << size << endl;
		
		for(int i = 0;; ++i)
		{
			double lx = i * size + margin;
			double rx = lx + body;
			
			if(lx > ir)
				break;
			
			int full = 0;

			if(rx < ir)
			{
				full = floor(sqrt(ir * ir - rx * rx) / size);
				totfull += full;
			}
			
			for(int j = full;; ++j)
			{
				double by = j * size + margin;
				double ty = by + body;
				
				if(rx * rx + ty * ty <= ir * ir)
				{
					++totfull;
//					cerr << "unexpected full at " << i << ' ' << j << ' ' << full << endl;
				}
				else 	if(lx * lx + by * by >= ir * ir)
					break;
				else
				{
					double cx = max(lx, (ty <= ir) ? sqrt(ir * ir - ty * ty) : lx);
					double dx = min(rx, (by <= ir) ? sqrt(ir * ir - by * by) : rx);
					
					double area = (cx - lx) * (ty - by) + cint(ir, cx, dx, by);
					totarea += area;
//					cerr << lx << ' ' << rx << ' ' << by << ' ' << ty << ' ' << cx << ' ' << dx << " -> " << area << endl;
				}
			}
		}
		
//		cerr << "Fulls: " << totfull << " -> " << totfull * body * body << " Partials: " << totarea << endl;
		totarea += totfull * body * body;
		
		double prob = 1.0 - ((4.0 / M_PI) * totarea / (R * R));

		out << "Case #" << (cas + 1) << ": " << fixed << setprecision(12) << prob << endl;
	}
}

