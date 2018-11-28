#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define PI 3.141592653589793238

int N;

double partA(double h,double R) {
	return acos(h/R)*R*R - h*sqrt(R*R-h*h);
}

double partB(double h1, double h2, double R) {
	return partA(h1,R)-partA(h2,R);
}

double min(double a, double b) {
	return a<b?a:b;
}

double dist(double x, double y) {
	return sqrt(x*x+y*y);
}

double f, R, t, r, g, h, E, E2, d, sR;

int main() {
	int i,j,n,X;
	double x,y;
	freopen("cpp1.in","r",stdin);
	freopen("cpp1.out","w",stdout);
	scanf("%d",&N);
	for(n=1;n<=N;n++) {
		scanf("%lf %lf %lf %lf %lf",&f, &R, &t, &r, &g);
		t += f;
		g -= 2*f;
		r += f;
		sR = R-t;
		if(t>R || g<0 || sR<r) {
			printf("Case #%d: %.6lf\n",n,1.0);
			continue;
		}
		d = 2*r+g;
		E = partB(0,r,sR);
		h = d;
		X = 1;
		while(h<sR) {
			E+=partB(h-r,min(h+r,sR),sR);
			h+=d;
			X++;
		}
		
		E *= 4;
		E += PI*R*R - PI*sR*sR;
		
		E2 = 0;

		for(i=1;i<X;i++) {
			for(j=1;j<X;j++) {
				x = i*d;
				y = j*d;
				bool dl = dist(x-r,y-r)<sR;
				bool ul = dist(x+r,y-r)<sR;
				bool ur = dist(x+r,y+r)<sR;
				bool dr = dist(x-r,y+r)<sR;

				if(!dl) continue;
				if(ur) {
					E2 += (2*r)*(2*r);
					continue;
				}
				y = j*d-r;
				h = min(x+r,sqrt(sR*sR-y*y));
				E2 += partB(x-r,h,sR)/2 - y*(h-x+r);
				if(dr) {
					y=j*d+r;
					h = min(x+r,sqrt(sR*sR-y*y));
					E2 -= partB(x-r,h,sR)/2 - y*(h-x+r);
				}
			}
		}
		j = 0;
		y = 0;
		for(i=1;i<X;i++) {
				x = i*d;
				bool dl = dist(x-r,y-r)<sR;
				bool ul = dist(x+r,y-r)<sR;
				bool ur = dist(x+r,y+r)<sR;
				bool dr = dist(x-r,y+r)<sR;

				if(!dl) continue;
				if(ur) {
					E2 += (2*r)*(2*r);
					continue;
				}
				h = min(x+r,sR);
				E2 += partB(x-r,h,sR);
				if(dr) {
					y = r;
					h = min(x+r,sqrt(sR*sR-y*y));
					E2 -= partB(x-r,h,sR) - 2*y*(h-x+r);
				}
		}
		if(dist(r,r)<sR) E2 += r*r;
		else {
			E2 += (PI*sR*sR)/4 - partB(r,sR,sR);
		}
		E2 *= 4;

		printf("Case #%d: %.6lf\n",n,(E-E2)/(PI*R*R));
	}
	return 0;
}