#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <cassert>

const double PI = 3.14159265358979323846;
const double eps = 1e-10;

using namespace std;

double INF = 1e300;

inline double lci(double y,double r){ 
    if(y>r) return INF;
    return sqrt(r*r-y*y);
}

inline bool circle_on_section(double y,double x1,double x2, double r){
    if(y>r) return false;
    double p = lci(y,r);
    return p+eps >= x1 && p-eps<= x2;
}


inline double cross(double x1,double y1,double x2,double y2){
    return x1*y2 - y1*x2;
}

double csect(double x1, double y1, double x2, double y2, double r){
    double sect = (fabs(atan(x1/y1) - atan(x2/y2)))/2/PI * PI * r*r;
    double t= .5 * fabs((cross(x1,y1,x1,y2) + cross(x1,y2,x2,y2)));
    assert(x1<=x2);
    assert(y1>=y2);
    assert(sect-t >= 0);
//    printf("r=%lf c=%lf x1=%lf y1=%lf x2=%lf y2=%lf\n",sect-t,(y2-y1)*(x1-x2),x1,y1,x2,y2);
    assert(sect-t-eps <= (y2-y1)*(x1-x2));
    return sect - t;
    
}

double calc2(double x1, double y1, double x2, double y2, double r){
    double g = y2-y1;
    bool on1 = circle_on_section(x1,y1,y2,r);
    bool on2 = circle_on_section(y2,x1,x2,r);
    bool on3 = circle_on_section(x2,y1,y2,r);
    bool on4 = circle_on_section(y1,x1,x2,r);

    double xx2=lci(y2,r), xx4=lci(y1,r);
    double yy1=lci(x1,r), yy3=lci(x2,r);

    if(on2 && on4){
	return (xx2-x1)*g + csect(xx2,y2,xx4,y1,r);
    }else if(on1 && on3){
	return (yy3-y1)*g + csect(x1,yy1,x2,yy3,r);
    }else if(on1 && on4){
	return csect(x1,yy1,xx4,y1,r);
    }else if(on2 && on3){
	return (yy3-y1)*g + (y2-yy3)*(xx2-x1) + csect(xx2,y2,x2,yy3,r);
    }else{
	printf("(%lf,%lf)-(%lf-%lf),r=%lf\n",x1,y1,x2,y2,r);
	assert(false);
    }
    
}

double calc(double f, double R, double t, double r,double g){
    double tot = PI * R * R;
    R = (R-t-f);
    r += f;
    g -= 2*f;
    
    if(g<=0) return 1;
    
    double inside = 0,RR=R*R;
    for(double y1 = r;y1<R;y1+= 2*r+g){
	for(double x1= r ; x1 < R && x1*x1 + y1*y1 < RR; x1 += 2*r+g){
	    double x2=x1+g, y2=y1+g;
	    if(x2*x2+y2*y2 <= RR){
		inside += g*g;
	    }else{
		double tmp=calc2(x1,y1,x2,y2,R);
		inside += tmp;
	    }
	}
    }
    return 1.0-inside*4/tot;
}


int main(){
    int ncases;
    cin >> ncases;
    
    for(int i=1;i<=ncases;++i){
	double f,R,t,r,g;
	cin >> f >> R >> t >> r >> g;
	printf("Case #%d: %0.9lf\n",i,calc(f,R,t,r,g));
    }
}
