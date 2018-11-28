#include <stdio.h>
#include <math.h>
#include <string.h>
#include <assert.h>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)

double radius(int x1, int y1, int r1, int x2, int y2, int r2){
	double dx = x1-x2, dy = y1-y2;
	return (sqrt(dx*dx + dy*dy) + r1 + r2) / 2.0;
}

int T,N,X[50],Y[50],R[50];

double calc(int i, int j){
	return radius(X[i],Y[i],R[i], X[j],Y[j],R[j]);
}

int main(){
	scanf("%d",&T);	
	REP(TC,T){
		scanf("%d",&N);
		assert(N<=3);
		REP(i,N) scanf("%d %d %d",&X[i],&Y[i],&R[i]);

		double res = 1e100;
		if (N==1){
			res = R[0];
		} else if (N==2){
			res = max(R[0],R[1]);
		} else {
			res = min(res, max(1.0*R[0], calc(1,2)));
			res = min(res, max(1.0*R[1], calc(0,2)));
			res = min(res, max(1.0*R[2], calc(0,1)));
		}
		printf("Case #%d: %.6lf\n",TC+1,res);
	}
}
