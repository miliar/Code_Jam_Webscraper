#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;
 
typedef long long LL;
typedef vector<int> vi;
typedef vector< pair<int, int> > vii;
#define MP(x,y) make_pair(x, y)

double ux[1005], uy[1005];
double lx[1005], ly[1005];
int nl, nu;

inline int findx(double *L, double *R, double &x) {
	return (upper_bound(L, R, x) - L) - 1;
}
inline double height(double x, double dy, double dx, double y) {
	return x * dy/dx + y;
}
double ABS(double x) {
	return x<0?-x:x;
}
double cutpoints(double x) {
	int idL = findx(lx, lx+nl, x);
	int idU = findx(ux, ux+nu, x);
	
	double hL = height(x-lx[idL], ly[idL+1]-ly[idL], lx[idL+1]-lx[idL], ly[idL]);
	double hU = height(x-ux[idU], uy[idU+1]-uy[idU], ux[idU+1]-ux[idU], uy[idU]);
//	printf("idL=%d, idU=%d hL %lf hU %lf\n", idL, idU, hL, hU);
	double area = 0.0;
	int i;
	for(i=0;i<idL;i++)
		area += lx[i] * ly[i+1] - lx[i+1] * ly[i];
	area += ux[0] * ly[0] - uy[0] * lx[0];
	area += lx[idL] * hL - x * ly[idL];
	area += x * hU - x * hL;
	area += x * uy[idU] - hU * ux[idU];
	for(i=idU; i>0; --i)
		area += ux[i] * uy[i-1] - ux[i-1] * uy[i];
	return ABS(area);
}
	double W;
double go(double target) {
	double ll = 0, rr = W;
	for(int u=0;u<100;u++){
		double mm = (ll+rr)/2.0;
		double darea = cutpoints(mm);
	//	printf("cut at %lf darea=%lf\n", mm, darea);
		if(darea < target) ll = mm;
		else rr = mm;
	}
	fprintf(stderr, "%lf %lf\n", ll, rr);
	return (ll+rr)/2.0;
}

int main(void) {
    int T, cs;
    scanf("%d", &T);
    for(cs=1;cs<=T;cs++) {
        
	
		int G;
		scanf("%lf%d%d%d", &W, &nl, &nu, &G);
		int i;
		for(i=0;i<nl;i++)
			scanf("%lf%lf", &lx[i], &ly[i]);
		for(i=0;i<nu;i++)
			scanf("%lf%lf", &ux[i], &uy[i]);
		double aa = 0.0;
		for(i=0;i<nl-1;i++)
			aa += lx[i] * ly[i+1] - lx[i+1] * ly[i];
		for(i=nu-1;i>0;--i)
			aa += ux[i] * uy[i-1] - ux[i-1] * uy[i];
		//for(i=0;i<nu-1;i++)
		//	aa -= ux[i] * uy[i+1] - ux[i+1] * uy[i];
		aa += W * uy[nu-1] - W * ly[nl-1];
		aa = ABS(aa);
		//printf("aa=%lf\n", aa);
		double bb = 0.0;
		printf("Case #%d:\n", cs);
		fprintf(stderr, "Case #%d:\n", cs);
		for (i = 1; i < G; i++) {
			bb = aa * i / (double)G;
			double v = go(bb);
			printf("%.8lf\n", v);
			fprintf(stderr, "%.8lf\n", v);
		}
    }
    return 0;
}

