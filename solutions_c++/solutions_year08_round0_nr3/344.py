#include <iostream>
#include <cmath>
using namespace std;

double pi = 3.141592535;
//Returns Integral(Sqrt(1-x^2),{x,0,t})
double Integral(double t){
	return (pi / 4) - ((asin(t)+t*sqrt(1-t*t))/2);
}

//For x,y>=0 calculate how much of the unit square has X>=x and Y>=y
//Works since the above integral is the area with X>=t Y>=0
//The area is 	(the area with X>=x Y>=0) 
//                   + (the area with Y>=y X>=0)
//                   + (the area with 0<=X<=x 0<=Y<=y)
//                   - (the aree with 0<=X 0<=Y)
double AreaOfCircleAboveXY(double x, double y){
	return (x*x + y*y >= 1) ? 0 : (Integral(x)+Integral(y)+(x*y)-(pi / 4));
}

// For 0<=x1<=x2 and 0<=y1<=y2 return the area of the intersection of the unit circle with
// [x1,x2] x [y1,y2]
// Works by the same kind of double counting as the previous function
double AreaOfCircleInRectangle(double x1, double y1, double x2, double y2){
	return AreaOfCircleAboveXY(x1,y1)+AreaOfCircleAboveXY(x2,y2)-
		(AreaOfCircleAboveXY(x1,y2)+AreaOfCircleAboveXY(x2,y1));
}

// Solves the anti-problem for flyRadius=0, outerRadius=1, thickness = 0
// Here the answer is the total area of the space missed by the strings / pi
// We add all the holes in the positive quadrant and divide by (pi/4)
double Miss(double stringRadius,double gap){
	double delta = (2*stringRadius+gap);
	double totalArea = 0;
	for (double x0 = stringRadius; x0 < 1; x0 += delta){
		for (double y0 = stringRadius; x0*x0 + y0*y0 < 1; y0 += delta){
			totalArea+=AreaOfCircleInRectangle(x0,y0,x0+gap,y0+gap);
		}
	}
	return (totalArea * 4) / pi;
}

// Solves the actual problem for flyRadius=0, outerRadius=1, thickness = 0
double Hit(double stringRadius, double gap){
	return 1-Miss(stringRadius,gap);
}

// Solves the actual problem for flyRadius=0, thickness = (outerRadius - 1), outerRadius > 1
// Counts the prob of being hit by the boundary + the prob of being hit by the strings
// Since flyRadius = 0, both are impossible
double Hit(double outerRadius, double stringRadius, double gap){
	double wholeArea = pi * outerRadius * outerRadius;
	double areaOfBoundary = wholeArea - pi;
	return (areaOfBoundary + Hit(stringRadius,gap) * pi) / wholeArea;
}

// Solves the actual problem for flyRadius=0
// This probability is homegenous:
// Hit(oR,t,sR,g)=Hit(k oR,k t,k sR,k g)
double Hit(double outerRadius, double thickness, double stringRadius, double gap){
	double innerRadius = outerRadius - thickness;
	return (thickness >= outerRadius) ? 1 :
		Hit(outerRadius / innerRadius, stringRadius / innerRadius, gap/innerRadius);
}

// Solves the actual problem
// The problem does not change if you reduce the flyRadius by k,
// increase the thickness and the stringRadius by k and decrease the gap by 2*k
double Hit(double flyRadius, double outerRadius, double thickness, double stringRadius, double gap){
	return (2 * flyRadius >= gap) ? 1 :
		Hit(outerRadius, thickness + flyRadius, stringRadius + flyRadius, gap - 2*flyRadius);
}

int main(){
	double flyRadius, outerRadius, thickness, stringRadius, gap;
	int N;
	cin >> N;
	for (int i = 0; i < N; ++i){
		cin >> flyRadius >> outerRadius >> thickness >> stringRadius >> gap;
		double answer=Hit(flyRadius, outerRadius, thickness, stringRadius, gap);
		printf("Case #%d: %.6f\n",i+1,answer);
	}
	return 1;
}
