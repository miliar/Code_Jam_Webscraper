#include <fstream>
#include <math.h>
#include <iostream>
#include <stdio.h>
using namespace std;

ifstream fin("b-small.in");
FILE * fout=fopen("b-small.out","w");

int main() {
	int ncase;
	fin>>ncase;
	for (int curcase=1; curcase<=ncase; curcase++) {
		int n;
		fin>>n;
		double x=0,y=0,z=0,a=0,b=0,c=0;
		
		for (int i = 0; i <n; i++) {
			int tx,ty,tz,ta,tb,tc;
			fin>>tx>>ty>>tz>>ta>>tb>>tc;
			x+=tx;
			y+=ty;
			z+=tz;
			a+=ta;
			b+=tb;
			c+=tc;
		}
		x/=n;y/=n;z/=n;a/=n,b/=n,c/=n;
		double A=a*a+b*b+c*c;
		double B=2*(a*x+b*y+c*z);
		double C=x*x+y*y+z*z;
		double ans = 0;
		double X=0;
		if (-B/(2*A)>0) 
			X=-B/(2*A);
		ans = A*X*X+B*X+C;
		if (ans<0) ans=0;
		ans = sqrt(ans);	
		fprintf(fout,"Case #%d: %0.8f %0.8f\n",curcase,ans,X);
//		fout<<"Case #"<<curcase<<": "<<ans<<" "<<X<<endl;
	}
	return 0;
}
			
		 
