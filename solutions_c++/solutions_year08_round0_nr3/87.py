#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>

#include <stdio.h>
#include <string.h>

using namespace std;

double f, R, t, r, g;
double prob;
double inner_R;
double box_w;

#define rad(x, y) sqrt(x*x+y*y)

#define integral(_x, _r) (0.5*(atan(_x/(sqrt(_r*_r-_x*_x)))*_r*_r+_x*sqrt(_r*_r-_x*_x)))
#define area_under(_x1, _x2, _y1, _r) (integral(_x2, _r) - integral(_x1, _r) - (_x2-_x1)*_y1)

double box_area(double x1, double y1)
{
	bool corner1, corner2, corner3, corner4;
	/* 3 4
	 * 1 2
	 */

       	corner1 = (rad(x1,y1)<inner_R);
	if (!corner1) return 0;

	double x2 = x1+box_w;
	double y2 = y1+box_w;

	corner4 = (rad(x2,y2)<inner_R);
	if (corner4) return (box_w*box_w);

	corner3 = (rad(x1,y2)<inner_R);
	corner2 = (rad(x2,y1)<inner_R);

	if (!corner2 && !corner3)
	{
		double x3 = sqrt(inner_R*inner_R-y1*y1);
		return area_under(x1, x3, y1, inner_R);
	}

	if (corner2 && corner3)
	{
		double x3 = sqrt(inner_R*inner_R-y2*y2);
		return ( (x3-x1)*box_w +  area_under(x3, x2, y1, inner_R));
	}

	if (corner2)
	{
		return area_under(x1, x2, y1, inner_R);
	}
	else
	{
		double x3a = sqrt(inner_R*inner_R-y2*y2);
		double x3b = sqrt(inner_R*inner_R-y1*y1);
		return ( (x3a-x1)*box_w + area_under(x3a, x3b, y1, inner_R) );
	}
	return 0; // should not get here...
}


int main()
{
	int num;
	ifstream in("in");
	string line;

	in >> num;
	getline(in, line);

	for (int n=0; n<num; n++)
	{
		in >> f >> R >> t >> r >> g;

		inner_R = R-t-f;
		box_w = g-2*f;

		if (2*f>=g) prob = 1.0;
		else
		{
			double x, y, y_max;
			double area=0.0;

			for (x=f+r; x<inner_R; x+=2*r+g)
			{
				y_max = sqrt(inner_R*inner_R-x*x);
				for (y=f+r; y<inner_R; y+=2*r+g)
				{
					area += box_area(x, y);
				}
			}
			double total_area = R*R*M_PI/4.0;
			prob = 1-(area/total_area);
		}

		printf("Case #%d: %8.6f\n", n+1, prob);
	}

	in.close();

	return 0;
}

