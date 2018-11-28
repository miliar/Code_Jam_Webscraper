#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <complex>
using namespace std;

typedef complex<double> point;

ifstream fin("d.in");
ofstream fout("d.out");

point p[10];
point q[100];
double ret[100];
int n,m;

double solve(point p0, double r0, point p1, double r1) {
	double c = abs(p1-p0);
	double cosCBA = (r1*r1 + c*c - r0*r0)/(2.0*r1*c);
	double cosCAB = (r0*r0 + c*c - r1*r1)/(2.0*r0*c);
	double CBA = acos(cosCBA);
	double CAB = acos(cosCAB);
	double CBD = 2.0*CBA;
	double CAD = 2.0*CAB;
	return 0.5*CBD*r1*r1 - 0.5*r1*r1*sin(CBD) + 0.5*CAD*r0*r0 - 0.5*r0*r0*sin(CAD);
}

int main() {
	int T,testNum;
	fin>>T;
	int i;
	double x,y;
	for(testNum=1;testNum<=T;++testNum) {
		fin>>n>>m;
		for(i=0;i<n;++i) {
			fin>>x>>y;
			p[i] = point(x,y);
		}
		for(i=0;i<m;++i) {
			fin>>x>>y;
			q[i] = point(x,y);
			ret[i] = solve(p[0],abs(q[i]-p[0]),p[1],abs(q[i]-p[1]));
		}
		fout<<"Case #"<<testNum<<":";
		for(i=0;i<m;++i) {
			fout.setf(ios::fixed);
			fout.precision(8);
			fout<<" "<<ret[i];
		}
		fout<<"\n";
	}
	return 0;
}
