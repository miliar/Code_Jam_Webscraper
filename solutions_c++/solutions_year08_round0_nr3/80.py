#include <iostream>
#include <cmath>

using namespace std;

const double ZERO = 1e-8;
const double PI = 3.1415926535897932;

double f, R, t, r, g;

void init()
{
	scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);	
}

double dis(double x1, double y1, double x2, double y2)
{
	return sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));	
}

double getarc(double x1, double y1, double x2, double y2)
{
	double arc;
	double c=dis(x1, y1, x2, y2), b=dis(0, 0, x1, y1), a=dis(0, 0, x2, y2);
	arc=acos((a*a+b*b-c*c)/2/a/b);
	double s=R*R*arc/2-R*R*sin(arc)/2;
	//cout << s << endl;
	return s;	
}

double calc(double x1, double x2, double y1, double y2)
{
	double xx, yy, xx0, yy0;
	
	if (dis(0, 0, x2, y2)<=R+ZERO)
		return (x2-x1)*(y2-y1);
	else
	if (dis(0, 0, x1, y1)>=R-ZERO)
		return 0.00;
	else
	if (dis(0, 0, x1, y2)<=R+ZERO && dis(0, 0, x2, y1)<=R+ZERO){
		xx=sqrt(R*R-y2*y2);
		yy=sqrt(R*R-x2*x2);
		return (xx-x1+x2-x1)*(y2-yy)/2+(x2-x1)*(yy-y1)+getarc(xx, y2, x2, yy);	
	}
	else
	if (dis(0, 0, x1, y2)<=R+ZERO){
		xx=sqrt(R*R-y2*y2);
		xx0=sqrt(R*R-y1*y1);
		return (xx-x1+xx0-x1)*(y2-y1)/2+getarc(xx, y2, xx0, y1);
	}
	else
	if (dis(0, 0, x2, y1)<=R+ZERO){
		yy=sqrt(R*R-x1*x1);
		yy0=sqrt(R*R-x2*x2);
		return (yy-y1+yy0-y1)*(x2-x1)/2+getarc(x1, yy, x2, yy0);
	}
	else
	{
		xx=sqrt(R*R-y1*y1);
		yy=sqrt(R*R-x1*x1);
		return (xx-x1)*(yy-y1)/2+getarc(x1, yy, xx, y1);
	}

}

void work()
{
	double s, x, y, x1, y1, x2, y2;
	
	if (2*f>=g-ZERO){
		printf("1.000000\n");
		return;
	}
	t+=f;
	g-=2*f;
	r+=f;
//	printf("t=%.6lf\n", t);
//	printf("g=%.6lf\n", g);
//	printf("r=%.6lf\n", r);
	x=0;
	s=0;
	while (x<R-t-ZERO){
		x1=x+r;
		x2=x1+g;
		y=0;
		while (y<R-t-ZERO){
			y1=y+r;
			y2=y1+g;
			R-=t;
		//	printf("%lf %lf %lf %lf\n", x1, y1, x2, y2);
			s+=calc(x1, x2, y1, y2);
			R+=t;
			y=y2+r;
		}
		x=x2+r;	
	}		
	s=s*4;
	printf("%.6lf\n", 1.0-(s/(PI*R*R)));
}

int main()
{
	int cas=0, t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	while (t--){
		cas++;
		printf("Case #%d: ", cas);
		init();
		work();
	}
		
	return 0;
}
