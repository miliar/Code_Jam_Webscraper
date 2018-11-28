/*
 * =====================================================================================
 *
 *       Filename:  FlySwatter.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  07/17/08 12:21:12
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Kapil Bhudhia, kapilbhudhia@gmail.com
 *
 * =====================================================================================
 */


#include <iostream>
#include <map>

struct Point;
struct Square;
static const double PI = 3.14159265;
static const double EPSILON = 1e-08;
static const double EPSILONSQ = 1e-16;

double calculateFlyArea(double f, double R, double t, double r, double g);
using namespace std;

struct Point
{
	double x, y;
	bool valid;
	Point():valid(false) {}

	bool isValid()
	{
		return valid;
	}

	Point(double _x, double _y)
		: x(_x), y(_y), valid(true)
	{}
	
	double distsq(Point pt)
	{
		return (x-pt.x)*(x-pt.x) + (y-pt.y)*(y-pt.y);
	}

	double dist(Point pt)
	{
		return sqrt((x-pt.x)*(x-pt.x) + (y-pt.y)*(y-pt.y));
	}

	void set(double _x, double _y)
	{
		valid = true;
		x = _x;
		y = _y;
	}
};

struct Square
{
	double xmin, xmax, ymin, ymax;
	double R, r, g, f;
	Point centre;

	enum AXIS {YPAR=0, XPAR=1};

	Square(int i, int j, double _R, double _r, double _g, double _f)
		:xmin(-1), ymin(-1), xmax(-1), ymax(-1), R(_R), r(_r), g(_g), f(_f)
	{
		centre.set((r + g/2) + (i - 1)*(2*r+g), (r + g/2) + (j - 1)*(2*r+g));

		xmin = centre.x - g/2 + f;
		xmax = centre.x + g/2 - f;
		ymin = centre.y - g/2 + f;
		ymax = centre.y + g/2 - f;

		//cout << xmin << " " << xmax << " " << ymin << " " << ymax << endl;
	}

	bool isValid()
	{
		//cout << "isVALID : " <<R - Point(xmin, ymin).dist(Point(0,0)) <<endl;
		return ((xmax - xmin ) > EPSILON) && ((ymax - ymin) > EPSILON)
			&& ((R - Point(xmin, ymin).dist(Point(0,0))) > EPSILON);
	}

	double calculateArea()
	{
		Point  xminX, yminX, xmaxX, ymaxX;
		xminX = getIntersectionPoint(xmin, ymin, ymax, XPAR);
		yminX = getIntersectionPoint(ymin, xmin, xmax, YPAR);
		//cout << "xminX = " << xminX.x << ", " << xminX.y << endl;
		//cout << "yminX = " << yminX.x << ", " << yminX.y <<  endl;

		if(xminX.isValid() && yminX.isValid()) 
			return getArea(xminX, Point(xmin, ymin), yminX);

		if(xminX.isValid() && yminX.isValid() == false)
		{
			xmaxX = getIntersectionPoint(xmax, ymin, ymax, XPAR);
			if(xmaxX.isValid())
				return getArea(xminX, Point(xmin, ymin), Point(xmax, ymin), xmaxX, XPAR);
			else {cout << "Error Condt\n"; return 0;}
		}

		if(xminX.isValid() == false && yminX.isValid())
		{
			ymaxX = getIntersectionPoint(ymax, xmin, xmax, YPAR);
			if(ymaxX.isValid())
				return getArea(ymaxX, Point(xmin, ymax), Point(xmin, ymin), yminX, YPAR);
			else {cout << "Error Condt\n"; return 0;}
		}

		if(xminX.isValid() == false && yminX.isValid() == false)
		{
			xmaxX = getIntersectionPoint(xmax, ymin, ymax, XPAR);
			ymaxX = getIntersectionPoint(ymax, xmin, xmax, YPAR);

			if(xmaxX.isValid() && ymaxX.isValid())
				return getArea(ymaxX, Point(xmin, ymax), Point(xmin, ymin), Point(xmax, ymin), xmaxX);
			else
				return getSquareArea();
		}

	}

	Point getIntersectionPoint(double point, double lim1, double lim2, AXIS par)
	{
		Point Xpoint;
		double coord = -1;
		if(point - R > EPSILON) return Xpoint;
		coord = sqrt(R*R - point*point);
		if(((lim1 - coord) > EPSILON) || ((coord - lim2) > EPSILON)) return Xpoint; 
		if(par == XPAR)
		{
			Xpoint.set(point, coord);
		}
		else
		{
			Xpoint.set(coord, point);
		}

		return Xpoint;
	}

	double getArea(Point x1, Point x2, Point x3)
	{
		return getArcArea(x1, x3) + getTriangleArea(x1, x2, x3);
	}

	double getArea(Point x1, Point x2, Point x3, Point x4, AXIS par)
	{
		return getArcArea(x1, x4) + getTrapeziumArea(x1, x2, x3, x4, par);
	}
	double getArea(Point x1, Point x2, Point x3, Point x4, Point x5)
	{
		return getArcArea(x1, x5) + getSquareArea() - 
			getTriangleArea(x1, Point(xmax, ymax), x5);
	}

	double getArcArea(Point x1, Point x2)
	{
		double d = x1.dist(x2);
		double theta = asin(d/(2*R));
		return (theta*R*R - R*d*cos(theta)*0.5); 
	}

	double getTriangleArea(Point x1, Point x2, Point x3)
	{
		return 0.5 * x2.dist(x1) * x2.dist(x3); 
	}

	double getTrapeziumArea(Point x1, Point x2, Point x3, Point x4, AXIS par)
	{
		if(par == XPAR)
			return 0.5 * (xmax - xmin) * (x1.dist(x2) + x3.dist(x4));
		else
			return 0.5 * (ymax - ymin) * (x1.dist(x2) + x3.dist(x4));
	}

	double getSquareArea()
	{
		return (xmax - xmin)*(ymax - ymin);
	}
};


int main()
{
	int N;
	double f, R, t, r, g;

	cin >> N;
	
	for(int i = 0; i < N; i++)
	{
		cin >> f >> R >> t >> r >> g;
		//cout<<"f = " << f << " R = " << R << " t = " << t << " r = " << r << " g = " << g <<  endl;
		
		cout << "Case #" << i+1 << ": " << 1 - 4*calculateFlyArea(f, R, t, r, g)/(PI*R*R) << endl;
	}

	return 0;
}

double calculateFlyArea(double f, double R, double t, double r, double g)
{
	double flyArea = 0.0;
	R = R - t - f;
	for(int i = 1; ; i++)
	{
		double squareArea = 0.0;
		for(int j = 1; j <= i; j++)
		{
			Square square(i, j, R, r, g, f);
			if(square.isValid() == false)
			{
				break;
			}
			squareArea += (i == j) ? square.calculateArea()/2 : square.calculateArea();
		}
		if(squareArea < EPSILON)
			break;
		else
			flyArea += squareArea;
	}
	return 2*flyArea;
}

