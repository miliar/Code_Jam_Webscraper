
#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
using namespace std;

struct Point{
	double x;
	double y;
	double z;
	double vx;
	double vy;
	double vz;
	Point(): x(0),y(0),z(0),vx(0),vy(0),vz(0) {}
};

int main(){
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	int T;
	int num;
	int x, y, z;
	int vx, vy, vz;
	fin>>T;
	for(int t=1;t<=T;t++){
		Point mc;
		fin>>num;
		for(int i=0;i<num;i++){
			fin>>x>>y>>z>>vx>>vy>>vz;
			mc.x += x;
			mc.y += y;
			mc.z += z;
			mc.vx += vx;
			mc.vy += vy;
			mc.vz += vz;
		}
		mc.x /= num;
		mc.y /= num;
		mc.z /= num;
		mc.vx /= num;
		mc.vy /= num;
		mc.vz /= num;
		//cout<<mc.x<<" "<<mc.y<<" "<<mc.z<<endl;
		//cout<<mc.vx<<" "<<mc.vy<<" "<<mc.vz<<endl;
		double v2 = mc.vx*mc.vx + mc.vy*mc.vy + mc.vz*mc.vz;
		double c2 = mc.x*mc.x + mc.y*mc.y + mc.z*mc.z;
		double vc = mc.vx*mc.x + mc.vy*mc.y + mc.vz*mc.z;
		double tmin;
		double dmin;
		if(vc > 0 || abs(v2) < 0.000000001 || abs(c2) < 0.000000001){
			tmin = 0;
			dmin = c2;
		}
		else{
			tmin = -vc/v2;
			dmin = v2*tmin*tmin + 2*vc*tmin + c2;
			if(abs(dmin) < 0.000000001)
				dmin = 0;
		}
		fout<<"Case #"<<t<<": ";
		fout<<setprecision(8)<< setiosflags(ios::fixed)
			<<sqrt(dmin)<<" "<<tmin<<endl;

	}
	return 0;
}