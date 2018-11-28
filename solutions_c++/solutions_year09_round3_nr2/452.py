#include <iostream>
#include <cmath>

using namespace std;

void dist (double x,double y, double z, double vx, double vy, double vz) 
{
	double t;

	//cout << x << " " << y << " " << z << vx << vy << vz<<  endl;
	if(!vx && !vy && !vz) {
		t =  0.0;
	} else {
		 t  = ((double)( x*vx + y*vy + z*vz ))  / (double)((vx*vx) + (vy*vy) + (vz*vz)) ;
		t *= -1;
		if ( t <= 0 ) {
			t = 0;
		}
	}

	//cout << t;

	printf("%.8f ", sqrt ((x+vx*t)*(x+vx*t) +(y+vy*t)*(y+vy*t)+(z+vz*t)*(z+vz*t) )) ;

	printf("%.8f\n", t);

	//return ( sqrt ( (px*px) + (py*py) + (pz*pz) ) );	
}

int main()
{
	int T;

	int x,y,z,vx,vy,vz;
	//int X[11],Y[11],Z[11],VX[11],VY[11],VZ[11];
	int PX[11], PY[11], PZ[11];
	int cx, cy;

	cin >> T;
	int n;

	double tx, ty, tz, tvx, tvy, tvz;

	for (int i=0; i < T; i++ ) {
		cin >> n;
		tx = ty = tz = tvx = tvy = tvz = 0.0;

		for (int j = 0; j < n; j++ ) {
			cin >> x >> y >> z>>vx >> vy >>vz;
			tx += x;
			ty += y;
			tz += z;
			tvx += vx;
			tvy += vy;
			tvz += vz;
		
		}
		
		cout << "Case #" << i+1 << ": ";
		dist (tx/n, ty/n, tz/n, tvx/n, tvy/n, tvz/n); 
	}

		

	return 0;
}
