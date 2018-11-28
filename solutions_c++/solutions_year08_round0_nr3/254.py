#include <stdio.h>
#include <math.h>


int N ;
double f, R, t, r, g ;

double inner ;


bool in_zone(double x, double y){
	return (x*x+y*y<=R*R) ;
}


double moon_area(double x1, double y1, double x2, double y2){
	double th1 = atan(y1/x1) ;
	double th2 = atan(y2/x2) ;
	double dth ;

	if( th1 > th2 )
		dth =  th1 - th2 ;
	else
		dth = th2 - th1 ;

	return R*R*(dth-sin(dth))/2.0 ;
}


double get_area(double x, double y){

	double sum = 0 ;
	double cx1, cy1, cx2, cy2 ;

	if( in_zone(x+g, y+g) )
		return g*g ;

	if( in_zone(x, y+g) ){
		cx1 = sqrt(R*R - (y+g)*(y+g)) ;
		sum += (cx1-x)*g ;

		if( in_zone(x+g,y) ){
			cy2 = sqrt(R*R - (x+g)*(x+g)) ;
			sum += (g+cy2-y)*(x+g-cx1)/2.0 ;
			sum += moon_area(cx1, y+g, x+g, cy2) ;
		}
		else{
			cx2 = sqrt(R*R-y*y) ;
			sum += g*(cx2-cx1)/2.0 ;
			sum += moon_area(cx1,y+g,cx2,y) ;
		}
	}

	else{
		cy1 = sqrt(R*R - x*x) ;

		if( in_zone(x+g,y) ){
			cy2 = sqrt(R*R - (x+g)*(x+g)) ;
			sum += (cy1-y+cy2-y)*g/2.0 ;
			sum += moon_area(x, cy1, x+g, cy2) ;
		}
		else{
			cx2 = sqrt(R*R-y*y) ;
			sum += (cy1-y)*(cx2-x)/2.0 ;
			sum += moon_area(x,cy1,cx2,y) ;
		}
	}

	return sum ;
}



int main(void){

	int cases;
	double x, y ;
	double area ;

	scanf("%d", &N) ;
	for( cases=1 ; cases<=N ; cases++){
		scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g) ;

		if( 2*f >= g ){
			printf("Case #%d: %.6f\n", cases, 1.0) ;
			continue ;
		}

		g -= 2*f ;
		R -= t+f ;
		r += f ;

		area = 0 ;
		for( x = r ; x<R ; x+=g+2*r){
			for( y=r ; x*x+y*y<R*R ; y+=g+2*r)
				area += get_area(x,y) ;
		}

		area *= 4 ;
		R += t+f ;
		printf("Case #%d: %.6f\n", cases, 1.0-area/(R*R*3.141592653589793)) ;
	}


	return 0 ;
}

