/************************/
/*	GCJ 2008		     */
/*	Matthew D Sandy       */
/************************/

#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>

using namespace std;


#define xlow (threadDist*xnum+threadR)
#define xhigh (threadDist*(xnum+1.0)-threadR)
#define ylow (threadDist*ynum+threadR)
#define yhigh (threadDist*(ynum+1.0)-threadR)
#define SQR(_x) (_x*_x)
#define PI 3.14159265358979323846

long double squareArea(long double x1, long double x2, long double y_base, long double y_max, long double circleRin);
long double heightUnder(long double x, long double threadR, long double threadDist, long double circleRin);

int main(int argc, char **argv)
{
	ifstream inFile;
	inFile.open(argv[1]);
	if(inFile.is_open()) cout<<"Opened \""<<argv[1]<<"\" for read...\n";
	else {cout<<"Error opening \""<<argv[1]<<"\" for read...\n"; return 1;}
	ofstream outFile;
	outFile.open(argv[2]);
	if(inFile.is_open()) cout<<"Opened \""<<argv[2]<<"\" for write...\n";
	else {cout<<"Error opening \""<<argv[2]<<"\" for write...\n"; return 1;}
	
	//////////////////////BEGIN CODE//////////////////////
	/*Fly Swatter
	First, feather all shapes a distance of f, and assume the fly is a point of size zero.
	This will make conceptualizing it easier, while maintaining problem equivalency.
	Define the following post-feathering values:
	threadR = r+f
	circleRout = R
	circleRin = R-t-f
	threadDist = g
	Next, set up a grid in the top-right quadrant of the raquet (which will be representative of
	the entire raquet) that represents each square.
	For each square, integrate over x = x1 to x2, where x1 and x2 represent the potential left/right
	bounds from the string.  Eg. the first square will be bound by x1 = threadR and x2 = g-threadR, and the second square
	will be bound by x1 = g+threadR, x2 = 2g-threadR.
	y_base will be set for each row of the squares and represent the minimum empty height.  Eg. the first square will have
	y_base = threadR
	For each x, if the distance from the origin to the point {x,y_base} is greater than circleRin, then set the y-value to zero,
	otherwise... set the y-value to the minimum of the following two values: g-2*threadR, sqrt(circleRin^2 - x^2) - y_base
	Note that while the second value can be less than zero, the prior restriction forces it to zero, and also provides
	safety against square-rooting a negative number.
	Iterate through the grid, starting at 0,0, and working right until sqrt(x1^2+y_base^2) >= circleRin
	then go up one and repeat, until y_base >= circleRin
	Add each area to a total area, initialized to zero.  Once the previous loop exits, divide this area by
	PI*circleRout^2 / 4 to get the final probability.
	
	Some useful math notes:
	instead of calculating the integral in real-time, the integral of (sqrt(circleRin^2-x^2) - y_base)
	can be calculated beforehand (see http://integrals.wolfram.com/)
*/
	
	int numCases;
	inFile >> numCases;
	
	for(int i=1;i<=numCases;i++)
	{	//for each test case...
		cout<<"Now processing case #"<<i<<"\n";
		long double f,R,t,r,g;
		inFile >> f;
		inFile >> R;
		inFile >> t;
		inFile >> r;
		inFile >> g;
		long double threadR = r+f;
		long double circleRout = R;
		long double circleRin = R-t-f;
		long double threadDist = g+2*r;
		int xnum=0;
		int ynum=0;
		long double area = 0;
//		cout<<"threadR\tcircleRout\tcircleRin\tthreadDist\n";
//		cout<<threadR<<"\t"<<circleRout<<"\t\t"<<circleRin<<"\t\t"<<threadDist<<"\n";
		while(ylow<circleRin)
		{	//while our y_base is still inside the inner circle...
			while(xlow*xlow+ylow*ylow<circleRin*circleRin)
			{	//while the bottom-left corner of the square is still inside the circle...
//				cout<<"Adding area from cell <"<<xnum<<","<<ynum<<">\n";
//				cout<<"xlow: "<<xlow<<"  xhigh: "<<xhigh<<"  ylow: "<<ylow<<"  yhigh: "<<yhigh<<endl;
				area += squareArea(xlow,xhigh,ylow,yhigh,circleRin);
				xnum++;
			}
			ynum++;
			xnum = 0;
		}
/*		#define res 1000000.0
		long double dx = circleRin/res;
		for(long double x = 0; x < circleRin; x += dx)
		{
			area += dx*heightUnder(x,threadR,threadDist,circleRin);
		}*/

		//write to output file
		long double probability = 1.0 - (area*4)/(PI*circleRout*circleRout);
		outFile.precision(6);
		outFile<<fixed;
		outFile<<"Case #"<<i<<": "<<probability<<"\n";
	}

	//////////////////////END CODE//////////////////////
		
	inFile.close();
	outFile.close();
}

long double squareArea(long double x1, long double x2, long double y_base, long double y_max, long double circleRin)
{
	//cout<<"squareArea("<<x1<<","<<x2<<","<<y_base<<","<<y_max<<","<<circleRin<<")\n";
	//returns the non-negative area inside the space bound by the curves
	//{x = x1, x = x2, y = y_base, y = y_max, y = sqrt(circleRin^2-x^2)}
	if(x1>=x2 || y_base>=y_max) return 0.0;	//return 0 if no area possible
	long double area = 0;
	//calculate the x-coordinate at which the circle crosses over the top string.  if undefined (never intersects), define as x1 
	long double xtop = y_max>circleRin?x1:sqrt(circleRin*circleRin-y_max*y_max);
	//calculate the x-coordinate at which the circle crosses over the bottom string.  never need to worry about y_base>circleRin bc of loop condition
	long double xbottom = sqrt(circleRin*circleRin-y_base*y_base);
	//clamp xtop, xbottom between x1 and x2
	if(xtop<x1) xtop = x1;
	if(xtop>x2) xtop = x2;
	if(xbottom<x1) xbottom = x1;
	if(xbottom>x2) xbottom = x2;
	//each square's area consists of a rectangular area from x1 to xtop with height y_max-y_base...
	//cout<<"\txtop: "<<xtop<<"  xbottom: "<<xbottom<<endl;
	area += (xtop-x1)*(y_max-y_base);
	//and sometimes an integrated area over xtop to xbottom
	if(xtop<xbottom && circleRin > 0)
	{
		area += 0.5*(atan(xbottom/sqrt(circleRin*circleRin-xbottom*xbottom))*circleRin*circleRin+xbottom*sqrt(circleRin*circleRin-xbottom*xbottom));
		area -= 0.5*(atan(xtop/sqrt(circleRin*circleRin-xtop*xtop))*circleRin*circleRin+xtop*sqrt(circleRin*circleRin-xtop*xtop));
		area -= (xbottom-xtop)*y_base;
	}
	//cout<<"\tadded area: "<<area<<endl;
	return area;
}

long double heightUnder(long double x, long double threadR, long double threadDist, long double circleRin)
{
	//returns the length of 'empty line' underneath the circle at x
	if(fmod(x,threadDist)<threadR || fmod(x,threadDist)>threadDist-threadR) return 0.0;
	long double max_height = sqrt(SQR(circleRin)-SQR(x));
	long double height = max_height;	//start with the maximum height
	height -= threadR;	//always reduce by the base string
	int i = 1;
	while(i*threadDist+threadR<max_height)
	{	//while there are un-intersected threads, subtract their height
		height -= 2*threadR;
		i++;
	}
	long double last_height = max_height - (i*threadDist-threadR);	//this is the potentially intersected distance
	if(last_height>0) height -= last_height;	//only subtract it if it actually needs to be
	return height;
}

