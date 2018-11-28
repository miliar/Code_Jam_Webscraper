#include <iostream>
#include <math.h>

using namespace std;

const double pi = 3.1415926535897932384626433832795;


double val(double x,double r){
	return sqrt(r*r-x*x);
}

double integr(double x1,double x2,double r){	
	const double eps = 1e-6;
	double sum = 0;
	for (double x = x1; x+eps <= x2; x += eps)
		sum += (val(x,r)+val(x+eps,r)) * eps * 0.5;
	return sum;
}

double f(double x,double r){
	return (x * sqrt(r*r-x*x) + r*r * asin(x/r))/2;
}

double integr1(double x1,double x2,double r){
	return (f(x2,r) - f(x1,r));
}

bool bel(double x,double y,double R){
	return x * x + y * y <= R*R;
}

double solve(double f,double R,double t,double r,double g){
	g -= 2*f;
	r += f;
	t += f;

	if (g <= 0) return 1;

	double RR = R - t;

	if (RR <= 0) return 1;

	double sum = 0;

	for (double x = r; x < RR; x += g + 2*r)
		for (double y = r; y < RR; y += g + 2*r){
			double x1 = x;
			double x2 = x + g;

			if (!bel(x,y,RR)) continue;
			if (!bel(x2,y,RR))
				x2 = sqrt(RR*RR - y * y);

			if (sqrt(RR*RR - x2*x2) >= y + g)
				sum += g * g;
			else {
				if (sqrt(RR*RR-x1*x1) >= y + g){
					double x3 = sqrt(RR*RR - (y+g)*(y+g));

					sum += integr1(x3,x2,RR) - (x2-x3) * y + (x3-x1) * g;
				}
				else
					sum += integr1(x1,x2,RR) - (x2-x1) * y;			
			}
		}

	return 1-(sum / (pi * R * R / 4));
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	cin >> n;
	for (int i = 1;i <= n; ++i){
		double f,R,t,r,g;
		cin >> f >> R >> t >> r >> g;
		printf("Case #%i: %.9lf\n",i,solve(f,R,t,r,g));
	}	

	return 0;
}