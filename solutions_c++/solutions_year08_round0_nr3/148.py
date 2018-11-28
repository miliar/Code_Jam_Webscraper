#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int N;
	cin >> N;
	
	for(int n = 1; n <= N; ++n) {
		cout << "Case #" << n << ": ";
		
		double f, R, t, r, g;
		cin >> f >> R >> t >> r >> g;
				
		t += f;
		r += f;
		g -= 2*f;
		double R0 = R-t;
		double R0_2 = R0*R0;
		
		double P = 1.0;
		if(g > 0) {
			P = 0.0;
			for(double x = r; x < R0; x += g+2*r) {
				for(double y = r; x*x + y*y < R0_2; y += g+2*r) {
					double x2 = x+g;
					double x2_other = sqrt(R0_2 - y*y);
					if(x2_other < x2) x2 = x2_other;
					double y2 = y+g;
					double x3_2 = R0_2 - y2*y2;
					double x3 = (x3_2 < 0) ? x : sqrt(x3_2);
					if(x3 < x) x3 = x;
					if(x3 > x2) x3 = x2;
					
					if(x3 > x) {
						P += g * (x3 - x);
					}
					if(x3 < x2) {
						double s3 = sqrt(R0_2 - x3*x3);
						if(!(s3 > 0)) s3 = 0.0;
						double s2 = sqrt(R0_2 - x2*x2);
						if(!(s2 > 0)) s2 = 0.0;
						P += 0.5*(s2*x2 - s3*x3 + R0_2*(atan(x2/s2)-atan(x3/s3)))
							- y * (x2 - x3);
					}
				}
			}
			P = 1.0 - (P / (M_PI*R*R/4));
		}
		cout << P << endl;
	}
}
