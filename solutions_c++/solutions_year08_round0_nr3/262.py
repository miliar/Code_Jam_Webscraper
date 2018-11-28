#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <assert.h>

using namespace std;

const double pi = 3.141592653589793238462643383279;

double slice(double x1, double y1, double x2, double y2, double rad)
{
	double dx = x2-x1;
	double dy = y2-y1;
	double c = sqrt(dx*dx+dy*dy);
	double theta = 2 * asin(c / (2*rad));
	double res = rad*rad*(theta-sin(theta))/2;
	assert(res>=0);
	return res;
}

bool checkSlice1(double x1, double y1, double x2, double y2, double rad, double g, double *area)
{
	if (rad<y2 || rad<x2) return false;
	double xs = sqrt(rad*rad-y2*y2);
	if (xs<x1 || xs>x2) return false;
	double ys = sqrt(rad*rad-x2*x2);
	if (ys<y1 || ys>y2) return false;
	*area = g*g - (x2-xs)*(y2-ys)/2 + slice(xs,y2,x2,ys,rad);
	assert(*area>=0);
	return true;
}

bool checkSlice2(double x1, double y1, double x2, double y2, double rad, double g, double *area)
{
	if (rad<y2 || rad<y1) return false;
	double xs1 = sqrt(rad*rad-y2*y2);
	if (xs1<x1 || xs1>x2) return false;
	double xs2 = sqrt(rad*rad-y1*y1);
	if (xs2<x1 || xs2>x2) return false;
	*area = (xs1-x1)*g + (xs2-xs1)*g/2 + slice(xs1,y2,xs2,y1,rad);
	assert(*area>=0);
	return true;
}

bool checkSlice3(double x1, double y1, double x2, double y2, double rad, double g, double *area)
{
	if (rad<x1 || rad<x2) return false;
	double ys1 = sqrt(rad*rad-x1*x1);
	if (ys1<y1 || ys1>y2) return false;
	double ys2 = sqrt(rad*rad-x2*x2);
	if (ys2<y1 || ys2>y2) return false;
	*area = (ys2-y1)*g + (ys1-ys2)*g/2 + slice(x1,ys1,x2,ys2,rad);
	assert(*area>=0);
	return true;
}

bool checkSlice4(double x1, double y1, double x2, double y2, double rad, double g, double *area)
{
	if (rad<y1 || rad<x1) return false;
	double xs = sqrt(rad*rad-y1*y1);
	if (xs<x1 || xs>x2) return false;
	double ys = sqrt(rad*rad-x1*x1);
	if (ys<y1 || ys>y2) return false;
	*area = (xs-x1)*(ys-y1)/2 + slice(xs,y1,x1,ys,rad);
	assert(*area>=0);
	return true;
}

double calc(double f, double R, double t, double r, double g)
{
	double rad = R-t-f;
	g -= 2*f;
	r += f;
	if (g<=0) return 1;

	double step = g+2*r;
	int size = (int)(R / step + 0.5) + 1;
	
	double sum = 0;
	for (int i=0; i<size; ++i)
		for (int j=0; j<size; ++j)
		{
			double x1 = r + step*i;
			double y1 = r + step*j;
			double x2 = x1 + g;
			double y2 = y1 + g;
			double area = g*g;
			if (sqrt(x1*x1+y1*y1) >= rad) area = 0;
			else
				if (!checkSlice1(x1,y1,x2,y2,rad,g,&area))
					if (!checkSlice2(x1,y1,x2,y2,rad,g,&area))
						if (!checkSlice3(x1,y1,x2,y2,rad,g,&area))
							checkSlice4(x1,y1,x2,y2,rad,g,&area);
			sum += area;
		}

	sum = 1 - sum / (R*R*pi)*4;
	if (sum<0) sum = 0;
	return sum;
}

int main(int argc, char *argv[])
{
	if (argc<2)
	{
		cout << "Filename needed\n";
		return -1;
	}
	fstream fin(argv[1]);
	int numcases;
	fin >> numcases;
	for (int i=0; i<numcases; ++i)
	{
		double f,R,t,r,g;
		fin >> f >> R >> t >> r >> g;
		cout.precision(6);
		cout << "Case #" << i+1 << ": " << fixed << calc(f,R,t,r,g) << endl;
	}
	fin.close();
	return 0;
}