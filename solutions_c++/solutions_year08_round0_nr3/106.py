#include <iostream>
#include <fstream>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <cassert>
#include <cmath>

using namespace std;

/*

Yuck. I tried doing a Monte Carlo first, didn't converge fast enough. This solution is dedicated to Kristian.

Desert winds and a perverse desire to win
History buried in shame.

 */

const double PI = 3.1415926535898;

double area_one_corner(double radius, double px, double py)
{
	double topy = sqrt(radius*radius-px*px);
	double rightx = sqrt(radius*radius-py*py);
	double costheta = (px*rightx+py*topy)/(radius*radius);
	double sintheta = sqrt(1-costheta*costheta);
	double theta = acos(costheta);
	double sectorarea = radius*radius*theta/2.0;
	double triarea = radius*radius*sintheta/2.0;
	double rightarea = (topy-py)*(rightx-px)/2.0;
	return sectorarea-triarea+rightarea;
}

double area_bottom_corners(double radius, double p1x, double p1y, double p2x)
{
	double top2y = sqrt(radius*radius-p2x*p2x);
	return area_one_corner(radius,p1x, top2y)+ (top2y-p1y)*(p2x-p1x);
}

double area_left_corners(double radius, double p1x, double p1y, double p2y)
{
	double right2x = sqrt(radius*radius-p2y*p2y);
	return area_one_corner(radius,right2x, p1y)+(right2x-p1x)*(p2y-p1y);
}

double area_three_corners(double radius, double p1x, double p1y, double p2y, double p3x)
{
	double topy = sqrt(radius*radius-p3x*p3x);
	double rightx = sqrt(radius*radius-p2y*p2y);
	return area_one_corner(radius, rightx, topy) + (rightx-p1x)*(p2y-p1y) + (p3x-rightx)*(topy-p1y);
}

bool intri(double radius, double x, double y)
{
	return x*x+y*y <= radius*radius;
}

int main(int argc, char *argv[])
{
	assert(argc > 1);
	ifstream ifile(argv[1]);
	
	int cases=0;
	ifile >> cases;
	for(int caseno=1; caseno<=cases; caseno++)
	{
		double f, R, t, r, g;
		ifile >> f >> R >> t >> r >> g;
		
		double area=0;
		if(f < g/2)
		{
			for(double squarex = 0; squarex < R-t; squarex += g+2*r)
			{
				for(double squarey = 0; squarey < R-t; squarey += g+2*r)
				{	
					double x1 = squarex+r+f;
					double x2 = squarex+g+r-f;
					double y1 = squarey+r+f;
					double y2 = squarey+g+r-f;

					if(intri(R-t-f, x1, y1))
					{
						if(intri(R-t-f, x2, y2) )
						{
							area += (x2-x1)*(y2-y1);
						}
						else if(intri(R-t-f, x2, y1) )
						{
							if(intri(R-t-f, x1, y2) )
							{
								area += area_three_corners(R-t-f, x1, y1, y2, x2);
							}
							else
							{
								area += area_bottom_corners(R-t-f, x1, y1, x2);
							}
						}
						else if(intri(R-t-f, x1, y2))
						{
							area += area_left_corners(R-t-f, x1, y1, y2);
						}
						else
						{
							area += area_one_corner(R-t-f, x1, y1);
						}
					}
				}
			}
		}
		double totarea = PI/4.0 * R*R;
		cout << "Case #" << caseno << ": " << (totarea-area)/totarea << endl;
	}
}
