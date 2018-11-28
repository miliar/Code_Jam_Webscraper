#include <iostream>
#include <cmath>

using namespace std;

int main (void) {

	int nc;
	cin >> nc;

	for (int c = 1; c <= nc; c++) {

		int n;
		cin >> n;

		double sumX = 0.0, sumVX = 0.0;
		double sumY = 0.0, sumVY = 0.0;
		double sumZ = 0.0, sumVZ = 0.0;

		for (int i = 0; i < n; i++) {
			double x,y,z,vx,vy,vz;
			cin >> x >> y >> z >> vx >> vy >> vz;
			sumX+=x;
			sumY+=y;
			sumZ+=z;
			sumVX+=vx;
			sumVY+=vy;
			sumVZ+=vz;
		}

		double divisor = (2.0*sumVX*sumVX+2.0*sumVY*sumVY+2.0*sumVZ*sumVZ);
		double t;
		if (fabs(divisor) < 1e-9) {
			t = 1e-9;
		} else {
			t = -1.0*(2.0*sumX*sumVX+2.0*sumY*sumVY+2.0*sumZ*sumVZ)/divisor;
			if (t<1e-10) t = 1e-9;
		}
		double d = sqrt((sumX+t*sumVX)*(sumX+t*sumVX)/(1.0*n*n) + (sumY+t*sumVY)*(sumY+t*sumVY)/(1.0*n*n) + (sumZ+t*sumVZ)*(sumZ+t*sumVZ)/(1.0*n*n));

		printf("Case #%d: %.8lf %.8lf\n",c,d,t);

	}
}