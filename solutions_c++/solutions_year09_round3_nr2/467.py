#include <fstream>
#include <cmath>
#include <iostream>
#include <iomanip>

using namespace std;

int main () 
{

	ifstream fin ("B-large.in");
	ofstream fout ("B-large.out");
	double n, t;
	double x, y, z, vx, vy, vz;
	double cmx[2], cmy[2], cmz[2];
	double d, time, ax,ay,az, bx, by,bz;
	
	
	fin>>n;
	
	for (int i=0; i<n; i++) {
		fin>>t;
		cmx[0] = 0;
		cmy[0] = 0;
		cmz[0] = 0;
		cmx[1] = 0;
		cmy[1] = 0;
		cmz[1] = 0;
		
		for (int j=0; j<t; j++) {
			fin>>x>>y>>z>>vx>>vy>>vz;
		
			cmx[0] += x; //cout<<cmx[0]<<'\n';
			cmy[0] += y;
			cmz[0] += z;
		
			cmx[1] += x+vx;
			cmy[1] += y+vy;
			cmz[1] += z+vz;
		
		}
	
		cmx[0] /= t; //cout<<cmx[0]<<t<<'\n';
		cmy[0] /= t;
		cmz[0] /= t;
		
		cmx[1] /= t;
		cmy[1] /= t;
		cmz[1] /= t;
		
		bx= cmx[0]; 
		by= cmy[0];
		bz= cmz[0];
		
		ax= cmx[1]-bx; 
		ay= cmy[1]-by;
		az= cmz[1]-bz;
		
		if (ax*ax+ay*ay+az*az == 0) time = 0;
		else time =  (-ax*bx-ay*by-az*bz)/(ax*ax+ay*ay+az*az);
		
		if (time < 0) time = 0;
		d = ((pow(ax,2)+pow(ay,2)+pow(az,2))*time*time) + (time*2*(ax*bx+ay*by+az*bz)) + (pow(bx,2)+pow(by,2)+pow(bz,2));
		if (d<0) d=0;
		else d = sqrt(d);
		fout<< "Case #"<<i+1<<": "<<setiosflags(ios::fixed)<<setprecision(8)<<d<<" "<<time<<'\n';
				
	}

	fin.close();
	fout.close();
	return 0;

}
