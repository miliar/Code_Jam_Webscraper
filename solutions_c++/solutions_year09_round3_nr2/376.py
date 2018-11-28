#include<iostream>
#include<math.h>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int n;
		cin >> n;
		double xc, yc, zc, vxc, vyc, vzc; 
		double x, y, z, vx, vy, vz; 
		xc = 0; yc = 0; zc = 0; vxc = 0; vyc = 0; vzc = 0;
		for (int j = 0; j < n; j++)
		{
			cin >> x >> y >> z >> vx >> vy >> vz;
			xc += x; yc += y; zc += z; vxc += vx; vyc += vy; vzc += vz;
		}
		double t;
		if ((int)vxc == 0 && (int)vyc == 0 && (int)vzc == 0) t = 0;
		else 
		{
			t = (vxc * xc + vyc * yc + vzc *zc) / (vxc * vxc + vyc * vyc + vzc * vzc);
			t *= -1;
		}
		if (t < 0) t = 0;
		xc = (double) xc / n;
		yc = (double) yc / n;
		zc = (double) zc / n;
		vxc = (double) vxc / n;
		vyc = (double) vyc /n;
		vzc = (double) vzc / n;
		double dist;
		dist = sqrt((xc + vxc * t) * (xc + vxc * t) + (yc + vyc * t) * (yc + vyc * t) + (zc + vzc * t) * (zc + vzc * t));
		cout << "Case #" << i << ": ";
		printf("%.8f %.8f\n", dist, t);
	}
}
