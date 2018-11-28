#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <assert.h>
using namespace std;

#define PI 3.14159265358979323

double Fall(int run) {
		double f,R,t,r,g;
		cin >> f >> R >> t >> r >> g;
		double Area = PI*R*R/4;
		R -= t+f;
		g-=2*f; r+=f;
		if (g<=0) return 1;
		double esc = 0;
		int full = 0;
		double step = 2*r + g;
		for (double x = r; x < R; x+=step) {
			double RRxx = R*R-x*x;
			for (double y = r; y*y < RRxx; y+=step) {
				double xx[10], yy[10];
				int np=0; int arcat = -1;
				xx[np]=x; yy[np++]=y;
				xx[np]=x+g; yy[np++]=y;
				xx[np]=x+g; yy[np++]=y+g;
				xx[np]=x+g; yy[np++]=y+g;
				xx[np]=x; yy[np++]=y+g;
				xx[np]=x; yy[np++]=y;
				int k1 = 0, k2 = np-1;
				while (k1<=k2 && xx[k1]*xx[k1]+yy[k1]*yy[k1]<R*R) ++k1; // first bad
				while (k1<=k2 && xx[k2]*xx[k2]+yy[k2]*yy[k2]<R*R) --k2; // last bad
				if (k1<=k2) {
					//cerr <<k1 <<" " << k2 << " " << np << "! ";
					assert(k1<k2);
					assert(xx[k1-1]*xx[k1-1]+yy[k1-1]*yy[k1-1]<R*R);
					if (xx[k1]==xx[k1-1])
						yy[k1] = sqrt(R*R-xx[k1]*xx[k1]);
					else
						xx[k1] = sqrt(R*R-yy[k1]*yy[k1]);
					//cerr << " new k1 " << xx[k1] << "," << yy[k1];
					if (xx[k2]==xx[k2+1])
						yy[k2] = sqrt(R*R-xx[k2]*xx[k2]);
					else
						xx[k2] = sqrt(R*R-yy[k2]*yy[k2]);
					//cerr <<  " new k2 " << xx[k2] << "," << yy[k2] << endl;
					double ac = 0;
					for (int t=1; t<np; ++t) {
						ac += yy[t]*xx[t-1]-yy[t-1]*xx[t];
						if (t==k1) t=k2;
					}
					double a0 = atan(xx[k2]/yy[k2]);
					double a1 = atan(xx[k1]/yy[k1]);
					double sec = R*R*(a1-a0);
					double tri = yy[k2]*xx[k1]-yy[k1]*xx[k2];
					//cerr << xx[k2]<<"/"<<yy[k2]<<", "<<xx[k1]<<"/"<<yy[k1]<<"; ac=" << ac << " sec=" << sec << " tri=" << tri << endl;
					esc += 0.5 * (ac+sec);
				} else ++full;
			}
		}
		cerr << "full = " << full << ", rand = " << esc << ", A = " << Area << endl;

		return 1-(esc+full*g*g)/Area;
}

int main() {
	int N;
	
	
	cin >> N;
	for (int run=1; run<=N; ++run) {
		cout << "Case #" << run << ": " << Fall(run) << endl;
	}
}
