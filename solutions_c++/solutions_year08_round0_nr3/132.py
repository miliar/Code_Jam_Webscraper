//Compiler - Microsoft Visual C++
#include<assert.h>
#include<stdio.h>
#include<math.h>

#define EPS		1e-12

#define _abs(x)	(((x)>0)?(x):-(x))

#define E(x,y)	(_abs((x)-(y)) < EPS)
#define Z(x)	(_abs(x) < EPS)
#define ZN(x)	(x < 0 || Z(x))
#define ZP(x)	(x > 0 || Z(x))
#define S(x)	((x)*(x))

#define INSIDE 0
#define CUT 1

double f,R,t,r,g;
double rgr,inR,inR2;

/*
	E	equals
	Z	isZero
	ZN	isZeroOrNegative
	ZP	isZeroOrPositive
	S	squareOf
*/

//0 <= x1 <= x2 <= inR
double superSlice(double x1,double x2){		// area bounded by y=0, x=x1, x=x2, y = sqrt(inR*inR - x*x)
	double a,t1,t2;

	assert( ZP(x1) );
	assert( ZP(x2-x1) );
	assert( ZP(inR-x2) );

	t2 = acos(x2/inR);
	t1 = acos(x1/inR);
	a  = 0.5*( inR2*(t1-t2) + inR*(x2*sin(t2) - x1*sin(t1)) );

	assert( ZP(a) );

	return a;
}

double boxSlice(double x1,double x2,double y1,double y2,int &flag){		//box must be in the FIRST quadrant
	double x3,x4,a1,d11,d12,d21,d22;

	assert( ZP(x1));
	assert( ZP(y1));
	assert( ZP(x2-x1) );
	assert( ZP(y2-y1) );

	d11 = S(x1)+S(y1) - inR2; 
	d12 = S(x1)+S(y2) - inR2; 
	d21 = S(x2)+S(y1) - inR2; 
	d22 = S(x2)+S(y2) - inR2;

	assert( ZN(d11) );

	flag = CUT;

	if( ZN(d22) ){
		a1 = (x2-x1)*(y2-y1);
		flag = INSIDE;
	}
	else if( ZN(d12) && ZN(d21) ){
		x3 = sqrt(inR2 - S(y2));
//		printf("%.15lf %.15lf %.15lf %.15lf %.15lf\n",x1,x3,x2,y1,y2);
		assert(ZP(x2-x3));
//		printf("!\n");
		a1 = (x3-x1)*(y2-y1) + superSlice(x3,x2) - (x2-x3)*y1;
	}
	else if( ZN(d12) ){
		x3 = sqrt(inR2 - S(y2));	
		x4 = sqrt(inR2 - S(y1));	
		assert(ZP(x4-x3));
//		printf("!!\n");
		a1 = (x3-x1)*(y2-y1) + superSlice(x3,x4) - (x4-x3)*y1;
	}
	else if( ZN(d21) ){
//		printf("!!!\n");
		a1 = superSlice(x1,x2) - (x2-x1)*y1;
	}
	else{
		x3 = sqrt(inR2 - S(y1));
		assert(ZP(x3-x1));
//		printf("!!!!\n");
		a1 = superSlice(x1,x3) - (x3-x1)*y1;
	}

	assert( ZP(a1) );
	assert( ZP( (x2-x1)*(y2-y1) - a1) );

//	printf("%.15lf %.15lf %.15lf   %.15lf %.15lf\n",x2-x1,y2-y1,g, (x2-x1)*(y2-y1) , g*g);
//	assert( ZP( g*g - a1) );

	return a1;
}

int main(){

	int T,N,flag;
	scanf("%d",&T);

	int nx,ny;
	double a,A;
	double x1,x2,y1,y2,ymax;
	double pi = 2.*acos(0.);

	for(N=1;N<=T;N++){
		
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);

		g-=2*f;
		t+=f;
		r+=f;

		rgr = r+g+r;

		inR = R-t;
		inR2 = S(inR);

		assert( ZP(R-inR) );

		if( ZN(g) || ZN(inR) ){
			printf("Case #%d: 1.000000\n",N);
			continue;
		}

		a = 0;

//		printf(">>> %lf %lf %lf %lf\n",inR,t,r,g);

		for(nx=1;;nx++){
			
			x1 = (nx-1)*rgr + r;
			x2 = nx*rgr - r;

			if( ZP(x1-inR) )
				break;

			ymax = sqrt(inR2 - S(x1));

//			printf(">>> %lf %lf %lf\n",x1,x2,ymax);

			ny = (int)floor( (ymax - r) / rgr ) + 1;

			assert(ny>=1);

			y1 = (ny-1)*rgr + r;
			if( E(y1,ymax) )
				ny--;

			while(ny>=1){
				y1 = (ny-1)*rgr + r;
				y2 = ny*rgr - r;
				a += boxSlice(x1,x2,y1,y2,flag);
				if(flag==INSIDE)
					break;
				ny--;
			}

			assert(ny>=0);
//			printf("%d %d\n",nx,ny);
			if(ny >= 1)
				a += (ny-1)*g*g;
		}

		a*=4;
		A = pi*S(R);

		assert( ZP(a) );
		assert( ZP(A) );
		assert( ZP(A-a) );

//		printf("\n>>>> %.15lf %.15lf\n",a,A);

		printf("Case #%d: %.6lf\n",N, 1. - a / A);
	}
	return 0;
}