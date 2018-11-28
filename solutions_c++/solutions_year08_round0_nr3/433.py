#include <stdio.h>
#include <math.h>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

double f = 0.00001;
double R = 10000;
double t = 0.00001;
double r = 0.00001;
double g = 1000;
/*
double f = 1;
double R = 100;
double t = 1;
double r = 1;
double g = 10;
//double g_sq = 0;
*/
/*
double f = 0.25;
double R = 1.0;
double t = 0.1;
double r = 0.01;
double g = 0.9;
//double g_sq = 0;
*/
/*
double f = 0.4;
double R = 10000;
double t = 0.00001;
double r = 0.00001;
double g = 700;
//double g_sq = 0;
*/
int inside = 0, outside = 0, case1 = 0, case2 = 0, case3 = 0, case4 = 0;

class Rect {
private:
	double X, Y;	// coordinates of inner corner
	double distLL, distLR, distUL, distUR;	// L = Lower/Left, U = Upper, R = Right

public:
	Rect(double x_left, double y_bottom){
		X = x_left; 
		Y = y_bottom;

		distLL = getDistLowerLeft();
		distLR = getDistLowerRight();
		distUL = getDistUpperLeft();
		distUR = getDistUpperRight();
	};
	inline double getX1(){return X;};
	inline double getY1(){return Y;};
	inline double getX2(){return X+g;};
	inline double getY2(){return Y+g;};

	static double getDist(double x, double y){
		return sqrt(x*x + y*y);
	};
	static double getAngle(double x, double y){
		return atan(y/x);	// problem specification indicates there is no case that angle is 90 degrees.
	};

	double getDistLowerLeft() {return Rect::getDist( getX1(), getY1() ); };
	double getDistLowerRight(){return Rect::getDist( getX2(), getY1() ); };
	double getDistUpperLeft() {return Rect::getDist( getX1(), getY2() ); };
	double getDistUpperRight(){return Rect::getDist( getX2(), getY2() ); };
	
	bool isInside(){
		return ( distUR <= R );
	};
	bool isOutside(){
		return ( distLL >= R );
	};
	bool isMiddle(){
		return ( !isInside() && !isOutside() );
	};

	double getArea(){
		if (isInside()){
			inside++;
			return g*g;
		}else if (isOutside()){
			outside++;
			return 0.0;
		}

		double poly_area;
		double ang_low, ang_high;

		if ( distUL >= R && distLR >= R ){	// case 1
			case1++;
			ang_low  = asin( getY1() / R );
			ang_high = acos( getX1() / R );

			double dx = R * cos(ang_low) - getX1();
			double dy = R * sin(ang_high) - getY1();

			poly_area = dx * dy / 2; 	// triangular area

		}else if ( distUL < R && distLR >= R ){	// case 2
			case2++;
			ang_low  = asin( getY1() / R );
			ang_high = asin( getY2() / R );

			double dx_low  = R * cos(ang_low) - getX1();
			double dx_high = R * cos(ang_high) - getX1();

			poly_area = (dx_low + dx_high) * g / 2;	// trapezoidal area

		}else if ( distUL >= R && distLR < R ){	// case 3
			case3++;
			ang_low  = acos( getX2() / R );
			ang_high = acos( getX1() / R );

			double dy_right = R * sin(ang_low) - getY1();
			double dy_left  = R * sin(ang_high) - getY1();

			poly_area = (dy_right + dy_left) * g / 2;	// trapezoidal area

		}else{	// case 4
			case4++;
			ang_low  = acos( getX2() / R );
			ang_high = asin( getY2() / R );

			double dx = R * cos(ang_high) - getX1();
			double dy = R * sin(ang_low) - getY1();

			poly_area = g * g - (g - dx)*(g - dy)/2;	// square - triangle
		}
		
		return poly_area + Rect::getArcSectionArea(ang_high - ang_low);
	};
	
	static double getArcSectionArea(double angle){
		double arc_area = M_PI*R*R * angle / (2*M_PI);
		double triangle_area = R*cos(angle/2) * R*sin(angle/2);
		
		return arc_area - triangle_area;
	}
		
};

int main(){
	int N = 0;

	ifstream fi;
	ofstream fo;
	fi.open("input.txt");
	fo.open("output.txt");

	fi >> N;
	
	for(int i=0; i<N; i++){
		fi >> f >> R >> t >> r >> g;

		g = g - 2*f;
		R = R - t - f;

		double area_survival = 0.0;
		double area_racquet = M_PI * (R+t+f)*(R+t+f);

		double x1 = r + f;
		while(x1 < R){
			double y1 = r + f;
			printf("computing for (x1, y1) = (%f, %f)\n", x1, y1);
			while(y1 < R){
				Rect rect(x1, y1);
				area_survival += rect.getArea();
				y1 += (f+g+f) + 2*r;
			}
			x1 += (f+g+f) + 2*r;
		}
		area_survival *= 4;	// for 4 quadrants
		double prob = (area_racquet - area_survival) / area_racquet;
		
		printf("Area of racquet  = %10.10lf\n", area_racquet );
		printf("Area of survival = %10.10lf\n", area_survival );
		printf("Probability of hitting = %8.6lf\n", prob);
		
		char buf[10];
		sprintf(buf, "%8.6lf", prob);
		fo << "Case #" << i+1 << ": " << buf << endl;
	}

	fi.close();
	fo.close();
}

