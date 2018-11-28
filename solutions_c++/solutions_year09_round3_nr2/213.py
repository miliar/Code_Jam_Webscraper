#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

ifstream fin("infile.in");
ofstream fout("outfile.out");

int main()
{
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		int N; fin>>N;
		double x0=0.0, y0=0.0, z0=0.0;
		double vx=0.0, vy=0.0, vz=0.0;
		for(int f=0; f<N; f++) {
			double x00, y00, z00;
			double vxx, vyy, vzz;
			fin>>x00>>y00>>z00>>vxx>>vyy>>vzz;
			x0+=x00; y0+=y00; z0+=z00;
			vx+=vxx; vy+=vyy; vz+=vzz;
		}
		x0/=N; y0/=N; z0/=N; vx/=N; vy/=N; vz/=N;

		double tmin;
		if(vx==0.0 && vy==0.0 && vz==0.0) {
			tmin=0.0;
		}
		else {
			tmin = - (vx*x0 + vy*y0 + vz*z0)/(vx*vx + vy*vy + vz*vz);
			if(tmin<=0.0) tmin=0.0;
		}

/*		double dmin =
			vx*vx*tmin*tmin + 2*vx*x0*tmin + x0*x0 +
			vy*vy*tmin*tmin + 2*vy*y0*tmin + y0*y0 +
			vz*vz*tmin*tmin + 2*vz*z0*tmin + z0*z0;
		dmin = sqrt(dmin);*/

		double x,y,z;
		x=x0+vx*tmin; y=y0+vy*tmin; z=z0+vz*tmin;
		double dmin = sqrt(x*x+y*y+z*z);

		fout<<"Case #"<<t<<": "<<fixed<<setprecision(8)<<dmin<<" "<<tmin<<endl;
	}
	
	return 0;
}