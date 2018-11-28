#include "stdafx.h"
#include <vector>
#include <math.h>
#include <string>
#include <set>
#include <iostream>
#include <map>
#include <algorithm>
#include <sstream>
using namespace std;

const double eps=0.0000001;

int main(){

	freopen("A.in","rt",stdin);
	freopen("A.out","wt",stdout);

	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int N;
		cin>>N;
		vector<int> x(N),y(N),z(N),vx(N),vy(N),vz(N);
		double T,xc=0,x0=0,yc=0,y0=0,z0=0,zc=0;
		for(int i=0;i<N;i++)
		{
			cin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
		}
		for(int i=0;i<N;i++)
		{
			xc+=vx[i];
			yc+=vy[i];
			zc+=vz[i];
			x0+=x[i];
			y0+=y[i];
			z0+=z[i];
		}

		
		if ( (abs(xc)<eps) && (abs(yc)<eps) && (abs(zc)<eps) )
		{
			x0/=N*1.0;
			y0/=N*1.0;
			z0/=N*1.0;
			printf("Case #%d: %.10lf %.10lf\n",i+1,sqrt(x0*x0+y0*y0+z0*z0),0.0);
			continue;
		}

		T=-(xc*x0+yc*y0+zc*z0)/(xc*xc+yc*yc+zc*zc);
		if (T<0)
		{
			x0/=N*1.0;
			y0/=N*1.0;
			z0/=N*1.0;
			printf("Case #%d: %.10lf %.10lf\n",i+1,sqrt(x0*x0+y0*y0+z0*z0),0.0);
			continue;			
		}
		
		double X=0,Y=0,Z=0;
		for(int j=0;j<N;j++)
		{
			X+=x[j]+T*vx[j];
			Y+=y[j]+T*vy[j];
			Z+=z[j]+T*vz[j];
		}
		X/=N*1.0;
		Y/=N*1.0;
		Z/=N*1.0;
		double d=sqrt(X*X+Y*Y+Z*Z);
		printf("Case #%d: %.10lf %.10lf\n",i+1,d,T);

	}
	
	return 0;
}