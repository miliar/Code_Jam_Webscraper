#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

double Sx,Sy,Sz,Svx,Svy,Svz;
int n;

double sqr(double x)
{
	return x*x;
}

double f(double t)
{
	return sqr((Sx+t*Svx)/n)+sqr((Sy+t*Svy)/n)+sqr((Sz+t*Svz)/n);
}

void run()
{
	scanf("%d",&n);
	Sx=Sy=Sz=Svx=Svy=Svz=0;
	for(int i=0; i<n; i++)
	{
		long long x,y,z,vx,vy,vz;
		scanf("%lld%lld%lld%lld%lld%lld",&x,&y,&z,&vx,&vy,&vz);
		Sx+=x;
		Sy+=y;
		Sz+=z;
		Svx+=vx;
		Svy+=vy;
		Svz+=vz;
	}
	double Tmin;
	if((Svx*Svx+Svy*Svy+Svz*Svz)==0)
	{
		Tmin = 0;
	}
	else
	{
		Tmin = -(Svx*Sx+Svy*Sy+Sz*Svz)/(Svx*Svx+Svy*Svy+Svz*Svz);
	}
	if(Tmin<0)
	{
		Tmin = 0;
	}
	double res = f(Tmin);
	printf("%.6lf %.6lf",sqrt(res),Tmin);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int testCount;
	scanf("%d",&testCount);
	for(int testNumber=1; testNumber<=testCount; testNumber++)
	{
		printf("Case #%d: ",testNumber);
		run();
		printf("\n");
	}
	return 0;
}