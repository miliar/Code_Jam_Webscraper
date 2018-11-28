#include <cmath>
#include <string>
#include <cstdio>
using namespace std;

const double eps=1.e-10,pi=acos(-1.);

double r,rr;

inline double f(double x) {  //圆弧下面积积分公式 
	return (sqrt(rr-x*x)*x+rr*asin(x/r))/2.;
}


double go(double x1,double x2,double y) { 
double ret,sign,ll,t,yy;

	if (fabs(y)<eps) {
		return 0.;
	}
	if (x1+eps<=-r) {
		x1=-r;
	}
	if (x2>=r+eps) {
		x2=r;
	}
	if (x1+eps>x2) {
		return 0.;
	}
	if (y<=-eps) {
		sign=-1.;
		y=-y;
	}
	else {
		sign=1.;
	}
	if (y+eps>r) {
		return (f(x2)-f(x1))*sign;
	}

	yy=rr-y*y;
	t=sqrt(yy);
	if ((x1+eps>t) || (x2<-t+eps)) {
		return (f(x2)-f(x1))*sign;
	}
	if (x1+eps<=-t)  { //x1<-sqrt(rr-y*y)
		ret=f(-t)-f(x1);
		ll=-t;
	}
	else {
		ret=0.;
		ll=x1;
	}
	if (x2<t+eps)  { //x2<=sqrt(rr-y*y)
		ret+=(x2-ll)*y;
	}
	else {
		ret+=(t-ll)*y+f(x2)-f(t);
	}
	return ret*sign;
}
	

double gao(double x1,double y1,double x2,double y2,double pr) {
double x=0,y=0; 
	r=pr;
	x1-=x;
	x2-=x;
	y1-=y;
	y2-=y;
	if (x1>=x2+eps) {
		x=x1;
		x1=x2;
		x2=x;
	}
	rr=r*r;
	return fabs(go(x1,x2,y1)-go(x1,x2,y2));
	
}



int main() {
    
  
    
    int     T,test_case;
    double  f,  R,  t,  r,  g;
    double  x,x1, y1, x2, y2;
    double  side,   radius, step;
    double  nom;
    
    scanf("%d",&T);
    for ( test_case = 1; test_case <= T; ++test_case ) {
        
       
        scanf( "%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g );
        printf( "Case #%d: ", test_case );
        
        if( ( side = g - f - f ) <eps) {
           puts("1.000000");
            continue;
        }
        
        radius = R - t - f;
        step = g + r + r;
		nom=0.;
        for (x=r+f;x+side+eps>-radius;x-=step)
		;
        for( x1=x; x1+eps<= radius; x1 += step ) {
			x2=x1+side;
            for( y1 = x; y1 +eps <= radius; y1 += step ) {
                y2 = y1 + side;
                nom += gao( x1, y1, x2, y2, radius );
            }
        }
        
        printf( "%.6lf\n", 1.-nom / pi/R/R);
        
    }
    
    //system( "pause" );
	return 0;
    
}
