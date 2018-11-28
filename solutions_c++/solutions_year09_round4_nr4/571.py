#include<stdio.h>
#include<math.h>
#include<iostream>
using namespace std;

struct point{
	double x,y;
}p[3];
double r[3];

double sqr(double a){
	return a*a;
}

double dist(point a,point b){
	return sqrt(sqr(a.x-b.x)+sqr(a.y-b.y));
}

int main(){
	int T;
	scanf("%d",&T);
	for(int TT=1;TT<=T;TT++){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			cin>>p[i].x>>p[i].y>>r[i];
		}
		double ret=1e100;
		if(n==1){
			ret=r[0];
		}else if(n==2){
			ret=max(r[0],r[1]);
		}else{
			double r1=max((dist(p[0],p[1])+r[0]+r[1])/2,r[2]);
			double r2=max((dist(p[2],p[1])+r[2]+r[1])/2,r[0]);
			double r3=max((dist(p[0],p[2])+r[0]+r[2])/2,r[1]);
			ret=min(min(r1,r2),r3);
		}
		printf("Case #%d: %.7lf\n",TT,ret);
	}
}