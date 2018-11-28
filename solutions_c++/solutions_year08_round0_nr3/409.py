#include <iostream>
#include <cmath>
#include <utility>
#include <iomanip>
using namespace std;
#define PI 3.14159265359
typedef pair<double,double> Coord;
double distance(Coord p1,Coord p2)
{
	double d1 = p2.second - p1.second;
	double d2 = p2.first - p1.first;
	return sqrt(d1*d1+d2*d2);
}
double arcArea(double R,Coord c,double r)
{
	Coord origin(0,0);
	const double x = c.first, y = c.second;
	const double left = x-r,right = x+r,top = y+r,bottom = y-r;
	Coord leftBottom (left,bottom),rightTop(right,top),leftTop(left,top),rightBottom(right,bottom);
	if(distance(origin,leftBottom) >= R)
		return 0;
	if(distance(origin,rightTop) <= R)
		return 4*r*r;
	const double RSquare = R*R;
	Coord lp,rp;
	lp.first = left;
	lp.second = sqrt(RSquare-left*left);
	if(lp.second > top)
	{
		lp.second = top;
		lp.first = sqrt(RSquare-top*top);
	}
	rp.first = right;
	rp.second = sqrt(RSquare-right*right);
	if (rp.second < bottom)
	{
		rp.second = bottom;
		rp.first = sqrt(RSquare-bottom*bottom);
	}
	double area = ((rp.first*sqrt(RSquare-rp.first*rp.first)-lp.first*sqrt(RSquare-lp.first*lp.first)) 
					+ RSquare*(asin(rp.first/R)-asin(lp.first/R)))/2 - (rp.first - lp.first)*bottom;
	area += (lp.first-left)*(top-bottom);
	return area;
}
double GapArea(double R,double g,double r)
{
	if(R<=0 || g <= 0)
		return 0;
	double area = 0;
	Coord origin(0,0),leftBottom,rectCenter;
	int i=0;

	leftBottom.first = r;
	leftBottom.second = r;
	while (distance(origin,leftBottom) < R)
	{
		int j = 0;
		
		rectCenter.second = leftBottom.second+g/2;
		while(distance(origin,leftBottom) < R)
		{
			rectCenter.first = leftBottom.first+g/2;
			area += arcArea(R,rectCenter,g/2);
			j ++;
			leftBottom.first += 2*r+g;
		}
		i ++;
		leftBottom.first = r;
		leftBottom.second += 2*r+g;
	}
	return area;
}
int main()
{
	int i,testCases;
	double f,R,t,r,g;
	double totalArea,gapArea;
	double probability;
	cin >> testCases;
	for (i = 0; i < testCases; i ++)
	{
		cin >> f >> R >> t >> r >> g;
		totalArea = PI*R*R/4;
		gapArea = GapArea(R-t-f,g-2*f,r+f);
		probability = 1-gapArea/totalArea;
		cout << "Case #" << i+1 << ": " << fixed << setw(6) << probability << "\n";
	}
	
	return 0;
}