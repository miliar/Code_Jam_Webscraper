#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MN 100

#define inf 1e30

int X[MN],Y[MN],R[MN];

double max(double i,double j){return i>j?i:j;}
double min(double i,double j){return i<j?i:j;}

double getr(int i,int j){
	double d;
	d=hypot(X[i]-X[j],Y[i]-Y[j]);
	if (d<fabs(R[i]-R[j]*1.0)) return max(R[i],R[j]);
	else return (d+R[i]+R[j])/2;
}

double solve(){
	int i;
	double ret,tmp;
	int N;
	scanf("%d",&N);
	for (i=0;i<N;i++){
		scanf("%d%d%d",&X[i],&Y[i],&R[i]);
	}
	ret=inf;
	if (N==1) return R[0]*1.0;
	if (N==2) return R[0]>R[1]?R[0]*1.0:R[1]*1.0;
	if (N==3){
		ret=min(ret,(max(getr(0,1),R[2]*1.0)));
		ret=min(ret,(max(getr(2,1),R[0]*1.0)));
		ret=min(ret,(max(getr(2,0),R[1]*1.0)));
		return ret;
	}else return 0.0;
}

int main(){
	int C,cas;
	scanf("%d",&C);
	for (cas=1;cas<=C;cas++){
		printf("Case #%d: %.6lf\n",cas,solve());
	}
	return 0;
}

