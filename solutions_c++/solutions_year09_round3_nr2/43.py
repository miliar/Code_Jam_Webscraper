#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const int nmax=500;
double X,Y,Z,VX,VY,VZ;

double sqr(double a)
{
	return a*a;
}

double dis(double t)
{
	return sqrt(sqr(X+VX*t)+sqr(Y+VY*t)+sqr(Z+VZ*t));
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		int i,n,x,y,z,vx,vy,vz;
		scanf("%d",&n);
		X=Y=Z=VX=VY=VZ=0.0;
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d%d%d%d",&x,&y,&z,&vx,&vy,&vz);
			X+=x; Y+=y; Z+=z;
			VX+=vx; VY+=vy; VZ+=vz;
		}
		X/=n; Y/=n; Z/=n;
		VX/=n; VY/=n; VZ/=n;

		double tl=0.0,tr=1e9,tm,tm1,tm2;
		for(int it=0;it<200;it++)
		{
			tm=(tl+tr)/2;
			tm1=(tl+tm)/2;
			tm2=(tm+tr)/2;
			if (dis(tm1)<dis(tm)) tr=tm; else
			if (dis(tm2)<dis(tm)) tl=tm; else tr=tm2;
		}

		printf("Case #%d: %lf %lf\n",t,dis(tl),tl);
	}

	return 0;
}