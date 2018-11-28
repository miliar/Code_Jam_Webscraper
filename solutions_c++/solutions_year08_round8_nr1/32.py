#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <assert.h>
#include <memory.h>

using namespace std;

namespace {

const double PI = 3.14159265358;

double x1, y1, x2, y2, x3, y3;
double xx1, yy1, xx2, yy2, xx3, yy3;

double square(double x1, double y1, double x2, double y2, double x3, double y3)
{
	return abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1))/2.0;
}

double len(double x, double y)
{
	return sqrt(x*x + y*y);
}

void angle(double x1, double y1, double x2, double y2, double& c, double& s)
{
	double l1 = len(x1, y1);
	double l2 = len(x2, y2);
	c = (x1*x2 + y1*y2)/(l1*l2);
	s = (x1*y2-y1*x2)/(l1*l2);
}

bool null(double v)
{
	return abs(v) < 1E-9;
}

void solve()
{
	cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
	cin >> xx1 >> yy1 >> xx2 >> yy2 >> xx3 >> yy3;
	
	x2 -= x1; x3 -= x1;
	xx1 -= x1; xx2 -= x1; xx3 -= x1;

	y2 -= y1; y3 -= y1;
	yy1 -= y1; yy2 -= y1; yy3 -= y1;

	double xxx1 = -x1;
	double yyy1 = -y1;
	x1 = y1 = 0;

	double s1 = square(xx1, yy1, xx2, yy2, xx3, yy3);
	double s2 = square(x1, y1, x2, y2, x3, y3);

	double sf    = sqrt(s1/s2);
	double ca, sa;
		
	angle(x2, y2,xx2-xx1, yy2-yy1, ca, sa);

	double A = sf*ca - 1;
	double B = -sf*sa;
	double C = sf*sa;
	double D = sf*ca -1;
	double dx = xx1;
	double dy = yy1;

	bool sw = false;
	bool found = false;
	double rx, ry;

	try
	{
		if (null(A))
		{
			if (null(B))
			{
				if (null(dx))
				{
					if (null(C))
					{
						if (null(D))
						{
							if (null(dy))
							{
								rx = ry = 0;
								rx -= xxx1; ry -= yyy1;
								found = true;
							}
							else
								throw false;
						}
						else
						{
							found = true;
							rx = 0 - xxx1;
							ry = -dy/D - yyy1;
						}
					}
					else
					{
						found = true;
						ry = 1 - xxx1;
						rx = (-dy-D*ry)/C - yyy1;
					}
				}
				else
					throw false;
			}
			else
			{
				sw = true;
				swap(A, B);
				swap(C, D);
			}
		}

		double Y = (A*D - C*B);
		double Q = (C*dx -A*dy);
		if (null(Y))
		{
			if (null(Q))
				ry = 0;
			else
				throw false;
		}
		ry = Q/Y;
		rx = (-B*ry-dx)/A;

		if (sw)
			swap(ry, rx);

		rx -= xxx1;
		ry -= yyy1;

		cout << fixed << setprecision(8) << rx << " " << ry;

	}
	catch (bool)
	{
		cout << "No Solution";
		return;
	}

}

}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int tt=1; tt <= T; tt++)
	{

		cout << "Case #" << tt << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
