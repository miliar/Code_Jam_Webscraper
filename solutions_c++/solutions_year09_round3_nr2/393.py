#include<iostream>
#include<cmath>

using namespace std;

void main()
{
	int testcase;
	cin >> testcase;
	for(int t=0; t < testcase; t++) {
		int total;
		cin >> total;
		long double xc=0, yc=0, zc=0, vx=0, vy=0, vz=0;
		long double ixc=0, iyc=0, izc=0, ivx=0, ivy=0, ivz=0;

		for(int i=0;i<total;i++) {
			cin >> ixc >> iyc >> izc >> ivx >> ivy >> ivz ;
			xc+=ixc;
			yc+=iyc;
			zc+=izc;
			vx+=ivx;
			vy+=ivy;
			vz+=ivz;
		}
		xc = xc/total;
		yc = yc/total;
		zc = zc/total;
		vx = vx/total;
		vy = vy/total;
		vz = vz/total;

		long double anst = -(xc*vx + yc*vy + zc*vz )/ ( vx*vx + vy*vy + vz*vz );

		if ( anst < 0.0 || (( vx*vx + vy*vy + vz*vz ) < 0.00000001 && ( vx*vx + vy*vy + vz*vz ) > -0.00000001))
			anst = 0;
		long double ansd = (vx*vx + vy*vy + vz*vz)*anst*anst + 2*(xc*vx + yc*vy +zc*vz)*anst + xc*xc + yc*yc + zc*zc;

		double ot = anst;
		double od ;
		if ( ansd < 0.0000001 && ansd > -0.00000001)
			od = 0;
		else
			od = sqrt(ansd);
		printf("Case #%d: %.8f %.8f\n",t+1, od, ot);

	}
}