#include<stdio.h>
#include<vector>
#include<math.h>
#include<string.h>
#define EPS 1e-6
double pi=acos(-1);
inline double sqr(double x){ return x*x; }
double chord(double R,double rad){
	double pie=pi*R*R*rad/(2*pi);
	double tri=0.5*R*R*sin(rad);
	return pie-tri;
}

int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		double f,R,t,r,g;
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		if (g-2*f<=EPS){ printf("Case #%d: 1.000000\n",tt);continue; }
		double x=r+g-f, y=r+g-f,area=0,RR=R-t-f;

		while (sqr(x-g+2*f)+sqr(y-g+2*f)<sqr(RR)+EPS){
			while (sqr(x-g+2*f)+sqr(y-g+2*f)<sqr(RR)+EPS){
				if (sqr(x)+sqr(y)<sqr(RR)+EPS) area+=sqr(g-2*f);
				else{
					double xx=x-g+2*f,yy=y-g+2*f;
					if (sqr(x)+sqr(yy)<sqr(RR)+EPS){
						if (sqr(xx)+sqr(y)<sqr(RR)+EPS){
							//biggest
							double righty=sqrt(sqr(RR)-sqr(x));
							double upx=sqrt(sqr(RR)-sqr(y));
							area+=(upx-xx)*(g-2*f) + 0.5*(g-2*f+righty-yy)*(x-upx);
							area+=chord(RR,atan2(y,upx)-atan2(righty,x));
						}else{
							double lefty=sqrt(sqr(RR)-sqr(xx));
							double righty=sqrt(sqr(RR)-sqr(x));
							area+=0.5*(g-2*f)*(lefty-yy+righty-yy);
							area+=chord(RR,atan2(lefty,xx)-atan2(righty,x));
						}
					}else{
						if (sqr(xx)+sqr(y)<sqr(RR)+EPS){
							double upx=sqrt(sqr(RR)-sqr(y));
							double lowx=sqrt(sqr(RR)-sqr(yy));
							area+=0.5*(g-2*f)*(upx-xx+lowx-xx);
							area+=chord(RR,atan2(y,upx)-atan2(yy,lowx));
						}else{
							//smallest
							double upy=sqrt(sqr(RR)-sqr(xx));
							double rightx=sqrt(sqr(RR)-sqr(yy));
							area+=0.5*(rightx-xx)*(upy-yy);
							area+=chord(RR,atan2(upy,xx)-atan2(yy,rightx));
						}
					}
				}
				y+=2*r+g;
			}
			x+=2*r+g;
			y=r+g-f;
		}
		double cir=pi*sqr(R);
		printf("Case #%d: %.6lf\n",tt,(cir-4*area)/cir+1e-8);
	}
	return 0;
}
