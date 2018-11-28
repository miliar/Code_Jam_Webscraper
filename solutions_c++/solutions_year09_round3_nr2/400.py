#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <cstdio>

struct ff {
	int x,y,z;
	double vx,vy,vz;	
};

double cp(double x1, double y1, double z1, double x2, double y2, double z2) {
	return (x1+y1+z1)*(x2+y2+z2);
}

double veclen(double x, double y, double z) {
	return sqrt(x*x+y*y+z*z);
}

bool beg = false;
double tx, ty, tz;

double dptl(double x1, double y1, double z1, double x2, double y2, double z2) {
	double vx = x2-x1, vy = y2-y1, vz = z2-z1;
	double wx = -x1, wy = -y1, wz = -z1;

	double c1 = vx*wx + vy*wy + vz*wz;
	if(c1 <= 0) {
		beg = true;
		return sqrt(x1*x1+y1*y1+z1*z1);
	}
	double c2 = vx*vx + vy*vy + vz*vz;
	double b = c1/c2;
	double rx = b*vx + x1, ry = b*vy + y1, rz = b*vz + z1;

	tx = rx, ty = ry, tz = rz;

	return sqrt(rx*rx+ry*ry+rz*rz);
}
/*
double dptl(double x1, double y1, double z1, double x2, double y2, double z2)
{
	double vx = x2-x1, vy = y2-y1, vz = z2-z1;

    double c1 = -x1*vx - y1 * vy - z1*vz;
    double c2 = vx*vx + vy*vy + vz*vz;
    double b = c1 / c2;

	std::cout<<"dptl: "<<c1<<" "<<c2<<std::endl;

	return sqrt((b*vx)*(b*vx)+(b*vy)*(b*vy)+(b*vz)*(b*vz));
}
*/

void solve(int ind, const std::vector<ff>& ffs) {
	beg = false;
	double cx = 0, cy = 0, cz = 0, vx = 0, vy = 0, vz = 0;
	/*
	for(int i = 0; i < ffs.size(); ++i) {
		std::cout<<ffs[i].x<<" "<<ffs[i].y<<" "<<ffs[i].z<<std::endl;
	}
	*/
	for(int i = 0; i < ffs.size(); ++i) {
		cx += ffs[i].x;	
		cy += ffs[i].y;	
		cz += ffs[i].z;	
		vx += ffs[i].vx;	
		vy += ffs[i].vy;	
		vz += ffs[i].vz;	
	}

	cx /= ffs.size();	
	cy /= ffs.size();	
	cz /= ffs.size();	
	vx /= ffs.size();	
	vy /= ffs.size();	
	vz /= ffs.size();	

	double x2 = cx + 10*vx, y2 = cy + 10*vy, z2 = cz + 10*vz;

	double dis = dptl(cx,cy,cz,x2,y2,z2);

	double tim = -1.0;

	if(vx) {
		double l = (tx-cx)/vx;
		if(l > tim) tim = l;
	}
	if(vy) {
		double l = (ty-cy)/vy;
		if(l > tim) tim = l;
	}
	if(vz) {
		double l = (tz-cz)/vz;
		if(l > tim) tim = l;
	}

	if(tim == -1) tim = 0;

	if(beg) tim = 0;

	printf("Case #%d: %.7f %.7f\n",ind,dis,tim);
	//std::cout<<"Case #"<<ind<<": "<<dis<<" "<<tim<<std::endl;

	//std::cout<<"Distance: "<<dptl(cx,cy,cz,x2,y2,z2)<<std::endl;
	//std::cout<<"Distance: "<<sqrt(pow(veclen(cx,cy,cz),2)*pow(veclen(x2-cx,y2-cy,z2-cz),2)-
	//std::cout<<"Distance: "<<sqrt((cx*cx*(x2-cx)*(x2-cx)-(cx*(x2-cx))*(cx*(x2-cx)))/(x2-cx)/(x2-cx))<<std::endl;
}

int main() {
	int cases;
	std::cin>>cases;
	std::cout<<std::setprecision(9);

	for(int i = 0; i < cases; ++i) {
		int ffc;
		std::cin>>ffc;
		std::vector<ff> ffs(ffc);
		for(int j = 0; j < ffc; ++j) {
			std::cin>>ffs[j].x>>ffs[j].y>>ffs[j].z>>ffs[j].vx>>ffs[j].vy>>ffs[j].vz;
		}
		solve(i+1,ffs);	
	}

	return 0;
}
