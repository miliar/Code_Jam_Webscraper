#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

const double pi = 3.14159265358979323846;

inline double distance(double x, double y)	//	distance of a point from the origin
{
	return sqrt( x*x + y*y );
}

inline double rds(double u, double v)		//	root of difference of squares
{
	return sqrt( u*u - v*v );
}

struct Point
{
	double x, y;
};

struct Gap
{
	Point left_bottom;

	double max_right;
	double max_width;

	double max_top;
	double max_height;
};

inline double area_sector(double x, double y, double x2, double y2, double r)
{
	return ( r*r*(atan2(x2,y)-atan2(x,y2)) - x2*y - x*y2 + 2*x*y ) / 2;
}

int main()
{
	int N;
	cin >> N;

	for(int n=1; n <= N; ++n)
	{
		double f, R, t, r, g;
		cin >> f >> R >> t >> r >> g;

		double fly_area = 0.0;

		Gap gap;

	  //  ----  Only loop for a single quadrant since the layout is symmetric  ----  //

		//	Outer loop iterates up-wards through rows of gaps  //

		for( gap.left_bottom.y = r; distance(r+f, gap.left_bottom.y+f) + f <= (R - t); gap.left_bottom.y += g + 2*r )
		{
			// Inner loop iterates right-wards through columns of gaps  //

			for( gap.left_bottom.x = r; distance(gap.left_bottom.x+f, gap.left_bottom.y+f) + f <= (R - t); gap.left_bottom.x += g + 2*r )
			{
				if( distance(gap.left_bottom.x + g, gap.left_bottom.y) <= (R - t) )
				{
					gap.max_right = gap.left_bottom.x + g;
					gap.max_width = g;
				}
				else
				{
					gap.max_right = rds(R - t, gap.left_bottom.y);
					gap.max_width = gap.max_right - gap.left_bottom.x;
				}

				//	----  //

				if( distance(gap.left_bottom.x, gap.left_bottom.y + g) <= (R - t) )
				{
					gap.max_top = gap.left_bottom.y + g;
					gap.max_height = g;
				}
				else
				{
					gap.max_top = rds(R - t, gap.left_bottom.x);
					gap.max_height = gap.max_top - gap.left_bottom.y;
				}

				//	----  //

				double x, y, x2, y2, x3, y3, Rtf;

				x = gap.left_bottom.x + f;
				y = gap.left_bottom.y + f;

				Rtf = R - t - f;

				if( gap.max_height < g  &&  gap.max_width < g )
				{
					x2 = rds(Rtf, y);
					y2 = rds(Rtf, x);

					fly_area += area_sector(x, y, x2, y2, Rtf);
				}

				else if( gap.max_height < g )
				{
					x2 = gap.max_right - f;
					y2 = rds(Rtf, x);

					y3 = rds(Rtf, x2);

					fly_area += area_sector(x, y3, x2, y2, Rtf) + (x2-x)*(y3-y);
				}

				else if( gap.max_width < g )
				{
					x2 = rds(Rtf, y);
					y2 = gap.max_top - f;

					x3 = rds(Rtf, y2);

					fly_area += area_sector(x3, y, x2, y2, Rtf) + (x3-x)*(y2-y);
				}

				else if( distance(gap.max_right, gap.max_top) > (R - t) )
				{
					x2 = gap.max_right - f;
					y2 = gap.max_top - f;

					x3 = rds(Rtf, y2);
					y3 = rds(Rtf, x2);

					fly_area += area_sector(x3, y3, x2, y2, Rtf) + (x2-x)*(y3-y) + (x3-x)*(y2-y3);
				}

				else
					fly_area += (g - 2*f) * (g - 2*f);
			}
		}

		float P = float(1 - 4 * fly_area / (pi * R*R ));

		printf("Case #%d: %.6f\n", n, P);
	}

	return 0;
}