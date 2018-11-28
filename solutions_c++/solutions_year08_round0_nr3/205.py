#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;
#define PI 3.14159265358979323846

double dist2(double x, double y)
{
	return x*x+y*y;
}
double int_circle_and_line(double a, double r)
{
	return sqrt(r*r-a*a);
}
double arcS(double r, double t)
{
	return r*r/2.0*(t-sin(t));
}
double arrowS(double r, double cx, double cy, double px, double py, bool cutarc)
{
	double p1x = px;
	double p1y = int_circle_and_line(p1x, r);
	if (cy < 0.0) p1y = -p1y;

	double p2y = py;
	double p2x = int_circle_and_line(p2y, r);
	if (cx < 0.0) p2x = -p2x;

	double S = fabs(py - p1y) * fabs(px - p2x) / 2.0;

	double theta = fabs(atan2(p1y, p1x) - atan2(p2y, p2x));
	return cutarc ? S - arcS(r, theta) : S + arcS(r, theta);
}

double hatS(double r, double g, double cx, double cy, double pt1x, double pt1y, double pt2x, double pt2y, bool cutarc)
{
	double p1y = pt1y;
	double p1x = int_circle_and_line(p1y, r);
	if (cx < 0.0) p1x = -p1x;

	double p2y = pt2y;
	double p2x = int_circle_and_line(p2y, r);
	if (cx < 0.0) p2x = -p2x;

	double S = (fabs(pt1x - p1x) + fabs(pt2x - p2x))*g/2.0;

	double theta = fabs(atan2(p1y, p1x) - atan2(p2y, p2x));
	return cutarc ? S - arcS(r, theta) : S + arcS(r, theta);
}

double miss(double x, double y, double f,double R,double t,double r,double g)
{
	if (g < 2.0*f)
		return 0.0;
	double a = g-2.0*f;
	double a2 = a / 2.0;
	double RR = (R-t-f)*(R-t-f);
	double ptx[4] = {x+a2, x+a2, x-a2, x-a2};
	double pty[4] = {y+a2, y-a2, y+a2, y-a2};
	bool pt_in[4];
	for (int i =0;i<4;i++)
		pt_in[i] = (dist2(ptx[i], pty[i]) < RR);

	if (pt_in[0] && pt_in[1] && pt_in[2] && pt_in[3])
		return a*a;

	if (!pt_in[0] && pt_in[1] && pt_in[2] && pt_in[3])
		return a*a - arrowS(R-t-f, x, y, ptx[0], pty[0], true);
	if (pt_in[0] && !pt_in[1] && pt_in[2] && pt_in[3])
		return a*a - arrowS(R-t-f, x, y, ptx[1], pty[1], true);
	if (pt_in[0] && pt_in[1] && !pt_in[2] && pt_in[3])
		return a*a - arrowS(R-t-f, x, y, ptx[2], pty[2], true);
	if (pt_in[0] && pt_in[1] && pt_in[2] && !pt_in[3])
		return a*a - arrowS(R-t-f, x, y, ptx[3], pty[3], true);

	if (!pt_in[0] && !pt_in[1] && pt_in[2] && pt_in[3])
		return a*a - hatS(R-t-f, a, x, y, ptx[0], pty[0], ptx[1], pty[1], true);
	if (!pt_in[0] && pt_in[1] && !pt_in[2] && pt_in[3])
		return a*a - hatS(R-t-f, a, y, x, pty[0], ptx[0], pty[2], ptx[2], true);
	if (pt_in[0] && !pt_in[1] && pt_in[2] && !pt_in[3])
		return a*a - hatS(R-t-f, a, y, x, pty[1], ptx[1], pty[3], ptx[3], true);
	if (pt_in[0] && pt_in[1] && !pt_in[2] && !pt_in[3])
		return a*a - hatS(R-t-f, a, x, y, ptx[2], pty[2], ptx[3], pty[3], true);

	if (!pt_in[0] && !pt_in[1] && !pt_in[2] && pt_in[3])
		return arrowS(R-t-f, x, y, ptx[3], pty[3], false);
	if (!pt_in[0] && !pt_in[1] && pt_in[2] && !pt_in[3])
		return arrowS(R-t-f, x, y, ptx[2], pty[2], false);
	if (!pt_in[0] && pt_in[1] && !pt_in[2] && !pt_in[3])
		return arrowS(R-t-f, x, y, ptx[1], pty[1], false);
	if (pt_in[0] && !pt_in[1] && !pt_in[2] && !pt_in[3])
		return arrowS(R-t-f, x, y, ptx[0], pty[0], false);

	return 0.0;
}

int main()
{
	int n;
	cin>>n;
	for (int i = 0; i<n; i++)
	{
		double f,R,t,r,g;
		cin>>f>>R>>t>>r>>g;

		double p = 0.0;
		int c = 2 * (int)ceil((R-t)/(g+2.0*r));
		for (int y=0; y<c;y++)
		{
			double dy = (y - c/2) * (g+2.0*r) + r + g/2.0;
			for (int x=0; x<c;x++)
			{
				double dx = (x - c/2) * (g+2.0*r) + r + g/2.0;
				p += miss(dx,dy,f,R,t,r,g);
			}
		}

		p = p/(PI*R*R);

		printf("Case #%d: %06f\n", i+1, 1.0-p);
	}

	return 0;
}
