#include "iostream"
#include "sstream"
#include "fstream"
#include "vector"
#include "algorithm"
#include "ios"
#include "math.h"
#include "limits"

using namespace std;

ifstream in("C-small-attempt1.in");
ofstream out("out.txt");

struct Object{
	Object(double left, double bottom, double square): Left(left), Bottom(bottom), Square(square) {}
	double Square;
	double Left;
	double Bottom;
};

double GetSquare(double x1, double y1, double x2, double y2, double R){
	if(R*R <= x1*x1 + y1*y1)
		return 0;
	double a = 0, b = 0, c = 0, d = 0;
	if(R*R <= x1*x1 + y2*y2) a = sqrt(R*R - x1*x1) - y1;
	else{
		a = y2 - y1;
		if(R*R <= x2*x2 + y2*y2) c = sqrt(R*R - y2*y2) - x1;
		else c = x2 - x1;
	}
	if(R*R <= x2*x2 + y1*y1) b = sqrt(R*R - y1*y1) - x1;
	else{
		b = x2 - x1;
		if(R*R <= x2*x2 + y2*y2) d = sqrt(R*R - x2*x2) - y1;
		else d = y2 - y1;
	}

	double result = 0;
	double chord = 0;
	result = c*a + d*b - c*d;
	chord = sqrt((b-c)*(b-c) + (a-d)*(a-d));
	//Correct result
	result += (b-c)*(a-d)*0.5;
	//More precision
	double phi = asin(chord*0.5/R);
	result += R*(phi*R - 0.5*chord*cos(phi));	//pi*R^2 * phi/2pi - Str
	return result;
}

int main(){
	int N = 0;
	in >> N;
	for(int i = 0; i < N; i++){
		double result = 0;
		double f = 0, R = 0, t = 0, r = 0, g = 0;
		in >> f >> R >> t >> r >> g;

		//Processing
		if(g > 2*f || R-f-t > 1.41421*(r+f)){	//For optimize
			//P != 1
			double Pr = R-f-t;	//Possible radius
			double Isr = 2*(r+f);	//Impossible string radius 
			double d = g - 2*f;	//Distance between impossible strings
			for(double x = Isr/2; x < Pr; x+=Isr+d){
				for(double y = Isr/2; y < Pr; y+=Isr+d){
					result += GetSquare(x, y, x+d, y+d, Pr);
				}
			}
			result *= 4;
			result /= 3.14159265358979323846*R*R;
			result = 1 - result;
		}else{
			result = 1.0;
		}

		//Output
		out.precision(6);
		out << "Case #" << i+1 << ": " << fixed << result << endl;
	}
}