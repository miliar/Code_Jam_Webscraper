#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <math.h>
#include <iomanip>

using namespace std;

void main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int x[512];
		int y[512];
		int z[512];
		int vx[512];
		int vy[512];
		int vz[512];

		int N;
		cin >> N;

		for (int n = 0; n < N; n++)
			cin >> x[n] >> y[n] >> z[n] >> vx[n] >> vy[n] >> vz[n];

		double xc;
		double yc;
		double zc;
		double vxc;
		double vyc;
		double vzc;

		double sumX = 0;
		double sumY = 0;
		double sumZ = 0;		
		double sumVX = 0;
		double sumVY = 0;
		double sumVZ = 0;
		for (int j = 0; j < N; j++)
		{
			sumX += x[j];
			sumY += y[j];
			sumZ += z[j];
			sumVX += vx[j];
			sumVY += vy[j];
			sumVZ += vz[j];
		}


		xc = sumX / (double)N;
		yc = sumY / (double)N;
		zc = sumZ / (double)N;
		vxc = sumVX / (double)N;
		vyc = sumVY / (double)N;
		vzc = sumVZ / (double)N;

		double minT;
		double minD;

		if (vxc*vxc + vyc*vyc + vzc*vzc < 1e-5)
		{
			minT = 0;
			minD = sqrt(xc*xc + yc*yc + zc*zc);
		}
		else
		{
			minT = - (xc * vxc + yc * vyc + zc * vzc) / (vxc*vxc + vyc*vyc + vzc*vzc);
			minD = sqrt((xc + minT*vxc)*(xc + minT*vxc) + (yc + minT*vyc)*(yc + minT*vyc) + (zc + minT*vzc)*(zc + minT*vzc));
		}

		if (minT < 0)
		{
			minT = 0;
			minD = sqrt(xc*xc + yc*yc + zc*zc);
		}

		printf("Case #%d: %.8f %.8f\n", t+1, minD, minT);
		//cout << setprecision(8) << "Case #" << t + 1 <<": " << minD << " " << minT << endl;
	}

}
