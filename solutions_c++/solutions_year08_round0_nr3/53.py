#include<iostream>
#include<algorithm>
#include<cmath>
#include<cassert>

using namespace std;

#define M 1440
#define N 256
#define INF 1000000000

double f, R, t, r , g;
const double  PI=acos(-1.0);
double dis(double x,double y){ return x*x+y*y;}
bool in_r(double x,double a,double b){
	return x>=a&&x<=b;
}
double cal(double a,double x){
	return x/2*(sqrt(a*a-x*x)) + a*a/2*asin(x/a);
}
double cal(double a,double x1,double x2){
	return cal(a,x2)-cal(a,x1);
}
double are(double R,double x,double y1,double y2){
	return cal(R,y1,y2)-x*(y2-y1);
}
int main()
{	

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++){
		printf("Case #%d: ",ii);
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		if(f*2>=g) {
			printf("%.6lf\n",1.0);
			continue;
		}
		double tot=PI*R*R/4 , sum=0;
		R=R-t-f;
		double x,y, de=g/2-f;
		for(y=r+g/2;;y+=2*r+g){			
			if( dis(r+g/2-de,y-de) >= R*R ) break;
			for(x=r+g/2;;x+=2*r+g){
				if( dis(x-de,y-de) >= R*R ) break;
				if( dis(x+de,y+de) <= R*R ){
					sum+=4*de*de;
				}else{
					double x1=sqrt( R*R-(y+de)*(y+de) );
					double x2=sqrt( R*R-(y-de)*(y-de) );
					if( in_r(x1,x-de,x+de ) && in_r(x2,x-de,x+de) ){
						double y1=y-de,y2=y+de;
						sum+=are(R,x-de,y1,y2);
					}else if( in_r(x1,x-de,x+de ) ){
						double y1=sqrt( R*R-(x+de)*(x+de) );
						double y2=y+de;
						sum+=are(R,x-de,y1,y2)+2*de*(y1-(y-de));
					}else if( in_r(x2,x-de,x+de ) ){
						double y1=y-de ;
						double y2=sqrt( R*R-(x-de)*(x-de) );
						sum+=are(R,x-de,y1,y2);						
					}else{
						double y1=sqrt( R*R-(x+de)*(x+de) );
						double y2=sqrt( R*R-(x-de)*(x-de) );
						sum+=are(R,x-de,y1,y2)+2*de*(y1-(y-de));		
					}
				}
			}

		}
		printf("%.6lf\n",1-(sum/tot));
	}
	return 0;
}