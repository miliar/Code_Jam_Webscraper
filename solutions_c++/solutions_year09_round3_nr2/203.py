#include <iostream>
#include <cmath>
#include <vector>
#include <cstdio>


using namespace std;


int main()
{
	int TestCase;
	cin  >> TestCase;
	for(int ti=0;ti<TestCase;ti++)
	{
		int n;
		cin >> n;

		double x=0,y=0,z=0,vx=0,vy=0,vz=0;

		for(int i=0;i<n;i++)
		{
			double p[3];
			double v[3];
			for(int j=0;j<3;j++) cin >> p[j];
			for(int j=0;j<3;j++) cin >> v[j];

			x += p[0]; y+=p[1]; z+=p[2];
			vx += v[0]; vy+=v[1]; vz+=v[2];
		}

		x/=(double)n;
		y/=(double)n;
		z/=(double)n;
		vx/=(double)n;
		vy/=(double)n;
		vz/=(double)n;

		double t;
		if(vx*vx+vy*vy+vz*vz==0.0)
			t=0;
		else

			t=-(x*vx+y*vy+z*vz)/(vx*vx+vy*vy+vz*vz);

		if(t<0) t=0;

		double nx=x+t*vx, ny=y+t*vy, nz=z+t*vz;

		cout << "Case #" << ti+1 << ": " ;
		printf("%.10lf %.10lf\n",sqrt(nx*nx+ny*ny+nz*nz) ,t );
	}
	return 0;
}
