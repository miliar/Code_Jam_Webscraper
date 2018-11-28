#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

double x[6000];
double y[6000];
double z[6000];
double vx[6000];
double vy[6000];
double vz[6000];

int main() {
	int k;
	scanf("%d",&k);

	for(int i=0;i<k;i++){

		int n;
		scanf("%d",&n);
		double num=0.0,den=0.0;
		double x0=0.0,y0=0.0,z0=0.0,a=0.0,b=0.0,c=0.0;
		for(int j=0;j<n;j++){
			scanf("%lf%lf%lf%lf%lf%lf",&x[j],&y[j],&z[j],&vx[j],&vy[j],&vz[j]);
			x0+=x[j];
			y0+=y[j];
			z0+=z[j];
			a+=vx[j];
			b+=vy[j];
			c+=vz[j];
		}
		num = ( a*x0 + b*y0 + c*z0);
		den = ( a*a + b*b + c*c);

		double tempo = - num / den;
		int anormal=0;
		if(fabs(den) <0.0000000000001){
			tempo = 0.0;
			anormal=1;
		}
		if(tempo < 0){
			tempo = 0.0;
			anormal=1;
		}


		double xf=0.0,yf=0.0,zf=0.0;
		for(int j=0;j<n;j++){
			xf+= (x[j] + vx[j]*tempo);
			yf+= (y[j] + vy[j]*tempo);
			zf+= (z[j] + vz[j]*tempo);
		}
		xf = xf/n;
		yf = yf/n;
		zf = zf/n;
		if(anormal){
			printf("Case #%d: %lf %lf \n",i+1,sqrt(xf*xf+yf*yf+zf*zf),0);
		}
		else{
			printf("Case #%d: %lf %lf \n",i+1,sqrt(xf*xf+yf*yf+zf*zf),-num/den);
		}




	}

}
