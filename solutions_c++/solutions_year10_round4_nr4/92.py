#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define BIT(X,B) (((X)>>(B))&1)
#define SET(X,B) ((X)|(1<<(B)))
#define CLR(X,B) ((X)&(~(1<<(B))))
#define REV(X,B) ((X)^(1<<(B)))

const double pi=acos(double(-1));
inline double sqr(double x){return x*x;}
inline double dis2(double x1,double y1,double x2,double y2){
	return sqr(x1-x2)+sqr(y1-y2);
}
/*
double inter_ccl(double x1,double y1,double r1,
				 double x2,double y2,double r2){
	double d=dis(x1,y1,x2,y2);
	if(r1+r2<=d) return 0.;
	if(r2-r1>=d) return pi*r1*r1;
	if(r1-r2>=d) return pi*r2*r2;

	double a1=acos((r1*r1+d*d-r2*r2)/(2.*r1*d));
	double a2=acos((r2*r2+d*d-r1*r1)/(2.*r2*d));
	
	return (a1-sin(a1))*r1*r1-(a2-sin(a2))*r2*r2;
}
*/
const int Max=10000;
double px[Max],py[Max],qx[Max],qy[Max];

int main(){
	int TT;
	scanf("%d",&TT);
	for(int cas=1;cas<=TT;++cas){
		int N,M;
		scanf("%d %d",&N,&M);
		for(int i=0;i<N;++i) scanf("%lf %lf",px+i,py+i);
		for(int i=0;i<M;++i) scanf("%lf %lf",qx+i,qy+i);
		printf("Case #%d:",cas);
		for(int i=0;i<M;++i){
			double r2=dis2(px[0],py[0],qx[i],qy[i]);
			double R2=dis2(px[1],py[1],qx[i],qy[i]);
			double d2=dis2(px[0],py[0],px[1],py[1]);
			double r=sqrt(r2),R=sqrt(R2),d=sqrt(d2);
			
			if(R-r>=d){
				printf(" %.8f",r2*pi);
				continue;
			}
			if(r-R>=d){
				printf(" %.8f",R2*pi);
				continue;
			}
			
			double cosR=(R2+d2-r2)/(2*R*d);
			double cosr=(r2+d2-R2)/(2*r*d);
			
			if(cosr>1.) cosr=1.;if(cosr<-1.) cosr=-1.;
			if(cosR>1.) cosR=1.;if(cosR<-1.) cosR=-1.;
			
			double ar=2*acos(cosr);
			double aR=2*acos(cosR);
			
			double sr=(ar-sin(ar))*r2/2.;
			double sR=(aR-sin(aR))*R2/2.;
			printf(" %.8f",sr+sR);
		}
		puts("");
	}
	return 0;
}
