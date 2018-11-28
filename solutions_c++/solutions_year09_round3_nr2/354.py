#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cmath>
using namespace std;

inline double kw(double x)
{
	return x*x;
}

int main() {
	int case_nr, T;
	cin >> T;

	for (case_nr=1; case_nr<=T; case_nr++) {
		int N;
		cin >> N;
		
		int xsum=0, ysum=0, zsum=0; // sumy
		int vxsum=0, vysum=0, vzsum=0;
		int x, y, z, vx, vy, vz;
		for (int i=0; i<N; i++)
		{
			cin >> x >> y >> z >> vx >> vy >> vz;
			xsum += x;
			ysum += y;
			zsum += z;
			vxsum += vx;
			vysum += vy;
			vzsum += vz;
		}

		double xsr = (double)xsum / (double)N;
		double ysr = (double)ysum / (double)N;
		double zsr = (double)zsum / (double)N;
		double vxsr = (double)vxsum / (double)N;
		double vysr = (double)vysum / (double)N;
		double vzsr = (double)vzsum / (double)N;

		/*double s1 = vxsr+vysr+vzsr;
		double s2 = vxsr*vxsr+vysr*vysr+vzsr*vzsr;
		double s3 = xsr+ysr+zsr;
		double s4 = vxsr*xsr+vysr*ysr+vzsr*zsr;*/

		double t=0;
		//double t = (3*s4-s1*s3)/(3*s2-s1*s1);
		if (kw(vxsr)+kw(vysr)+kw(vzsr) != 0)
		{	
			t = -(xsr*vxsr+ysr*vysr+zsr*vzsr)/(kw(vxsr)+kw(vysr)+kw(vzsr));
			if (t <= 0)
				t = 0;
		}

		double d = sqrt(kw(xsr+t*vxsr) + kw(ysr+t*vysr) + kw(zsr+t*vzsr));

		printf("Case #%d: %.8lf %.8lf\n", case_nr, d, t);
	}
}
