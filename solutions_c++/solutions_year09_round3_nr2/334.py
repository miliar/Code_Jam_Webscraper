#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <deque>
#include <math.h>

using namespace std;

FILE* in = fopen("B.in","r");
FILE* out = fopen("B.out","w");

int main(){
	int testnum = 0;
	
	fscanf(in,"%d", &testnum);
	double x[501], y[501], z[501], vx[501], vy[501], vz[501], tx[501], ty[501], tz[501];
	for(int test = 1; test <= testnum; ++test){
		int numfly = 0;
		double dist, time, curDist, curTime;
		double Xc,Yc,Zc, curXc, curYc, curZc;
		double Xcv,Ycv,Zcv;
		fscanf(in,"%d\n", &numfly);
		for(int i = 0; i< numfly; ++i){
			fscanf(in,"%lf %lf %lf %lf %lf %lf\n", &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
		}
		Xc = Yc = Zc = Xcv = Ycv = Zcv = 0;
		//X0
		for(int i = 0; i< numfly; ++i){
			Xc += x[i];
			Yc += y[i];
			Zc += z[i];
			Xcv += vx[i];
			Ycv += vy[i];
			Zcv += vz[i];
		}
		Xc = Xc/numfly;
		Yc = Yc/numfly;
		Zc = Zc/numfly;
		Xcv = Xcv/numfly;
		Ycv = Ycv/numfly;
		Zcv = Zcv/numfly;
		//Xt
		double minTime= 0, maxTime = 1e10;
		double DistMaxTime, DistMinTime = Xc*Xc + Yc*Yc + Zc*Zc;
		
		time = maxTime;
		curXc = Xc + time*Xcv;
		curYc = Yc + time*Ycv;
		curZc = Zc + time*Zcv;
		DistMaxTime = curXc*curXc + curYc*curYc + curZc*curZc;
		double eps = 0.000000001;
		while((maxTime - minTime) > eps || abs((double)DistMaxTime - DistMinTime)> eps){
				
			time = (maxTime+ minTime)/2.0;
			curXc = Xc + time*Xcv;
			curYc = Yc + time*Ycv;
			curZc = Zc + time*Zcv;
			curDist = curXc*curXc + curYc*curYc + curZc*curZc;
			if(DistMaxTime<DistMinTime){
				DistMinTime = curDist;
				minTime = time;
			}else{
				DistMaxTime = curDist;
				maxTime = time;
			}
		}
		time = (maxTime+ minTime)/2.0;
		dist = sqrt(curDist);
		fprintf(out,"Case #%d: %.10lf %.10lf\n", test, dist, time);
	}
	fprintf(out, "\n");
	return 0;
}