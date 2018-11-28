#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>
#include <sstream>
#include <algorithm>

using namespace std;

double Area(const double &x1,const double &x2,const double &y1,const double &y2,const double &R){
	double tot = (x2-x1) * (y2-y1);
	if (x2*x2+y2*y2 <= R*R) return tot;
	if (x1*x1+y1*y1 >= R*R) return 0;
	double intx1 = sqrt(R*R - y1*y1);
	double inty1 = sqrt(R*R - x1*x1);
	double intx2 = R*R - y2*y2 >= 0 ? sqrt(R*R - y2*y2) : 0.0;
	double inty2 = R*R - x2*x2 >= 0 ? sqrt(R*R - x2*x2) : 0.0;	
	if (intx1 < x2){
		if (inty1 < y2){
			double base = 0.5 * (inty1-y1) * (intx1-x1);
			double ang = abs(atan2(x1,inty1) - atan2(intx1,y1)) / 2.0;
			return base + R * R * (ang - sin(ang)*cos(ang));
		} else {
			double base = 0.5 * (y2-y1) * (intx1-x1+intx2-x1);
			double ang = abs(atan2(intx2,y2) - atan2(intx1,y1)) / 2.0;
			return base + R * R * (ang - sin(ang)*cos(ang));
		}				
	} else {
		
		if (inty1 < y2) {
			double base = 0.5 * (x2-x1) * (inty1-y1+inty2-y1);
			double ang = abs(atan2(x1,inty1) - atan2(x2,inty2)) / 2.0;
			return base + R * R * (ang - sin(ang)*cos(ang));
		} else {
			double base = tot - 0.5 * (y2-inty2) * (x2-intx2);
			double ang = abs(atan2(intx2,y2) - atan2(x2,inty2)) / 2.0;			
			return base + R * R * (ang - sin(ang)*cos(ang));
		}
	}
	return -1.0;
}


int main(int argc,const char * argv[]){
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	int TC;
	//return 0;
	fin >> TC;
	for (int tc=1;tc<=TC;tc++){
		double f,R,t,r,g;
		fin >> f >> R >> t >> r >> g;
		double val = 0.0;
		if (R - t - f <= 0.0 || g - 2 * f <= 0.0)
			val = 1.0;
		else {
			for (double x = 0;x < R;x += 2 * r + g)
				for (double y = 0;y < R;y += 2 * r + g)
					val += Area(x+r+f,x+r+g-f,y+r+f,y+r+g-f,R-t-f);
			val *= 4.0;
			val = 1.0 - val / (3.141592654 * R * R);
		}

		fout << "Case #" << tc << ": " << val << endl;
	}

}
