#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <iostream>
using namespace std;
double x[2],y[2],tx,ty;
double r[2];
int m,n;

void init(){
	scanf("%d%d",&n,&m);
	scanf("%lf%lf%lf%lf",&x[0],&y[0],&x[1],&y[1]);
	return;
}

double sqr(double k){
	return k*k;
}

double dist(double x1,double y1,double x2,double y2){
	return sqrt(sqr(x1-x2)+sqr(y1-y2));
}

double myacos(double k){
	if (k<=-1){
		return acos(-1);
	}
	if (k>=1){
		return acos(1);
	}
	return acos(k);
}

double getans(double l,double l1,double l2){
	double p=myacos((sqr(l)+sqr(l1)-sqr(l2))/(2*l*l1))*2.0;
	double q=myacos((sqr(l)+sqr(l2)-sqr(l1))/(2*l*l2))*2.0;
	return (sqr(l1)*(p-sin(p))+sqr(l2)*(q-sin(q)))*0.5;
}

void process(){
	for (int i=1;i<=m;i++){
		scanf("%lf%lf",&tx,&ty);
		r[0]=dist(x[0],y[0],tx,ty);
		r[1]=dist(x[1],y[1],tx,ty);
		printf(" %.6lf",getans(dist(x[0],y[0],x[1],y[1]),r[0],r[1]));
	}
	return;
}

int main(){
	int cse;
	scanf("%d",&cse);
	for (int k=1;k<=cse;k++){
		init();
		printf("Case #%d:",k);
		process();
		puts("");
	}
	return 0;
}
