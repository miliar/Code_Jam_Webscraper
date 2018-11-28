#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int T,N,cas=1;
double X[505],Y[505],Z[505];
double Vx[505],Vy[505],Vz[505];
double sumX,sumY,sumZ;
double sumVx,sumVy,sumVz;

int fcmp(double a,double b)
{
	if(fabs(a-b)<1E-12) return 0;
	if(a>b) return 1;
	return -1;
}

double cal(double t)
{
	double x=sumX+t*sumVx,y=sumY+t*sumVy,z=sumZ+t*sumVz;
	return (x*x+y*y+z*z)/(double) (N*N);
}

int main()
{
	freopen("d://B-large.in","r",stdin);
	freopen("d://1.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&N);
		sumX=sumY=sumZ=0;
		sumVx=sumVy=sumVz=0;
		for(int i=0;i<N;i++)
		{
			cin>>X[i]>>Y[i]>>Z[i];
			cin>>Vx[i]>>Vy[i]>>Vz[i];
			sumX+=X[i];sumY+=Y[i];sumZ+=Z[i];
			sumVx+=Vx[i],sumVy+=Vy[i],sumVz+=Vz[i];
		}
		double t;
		if(fcmp((sumVx*sumVx+sumVy*sumVy+sumVz*sumVz),0.0)==0)
			printf("Case #%d: %.8f %.8f\n",cas++,sqrt((sumX*sumX+sumY*sumY+sumZ*sumZ)/(double) (N*N)),0);
		else
		{
			t=-(sumVx*sumX+sumVy*sumY+sumVz*sumZ)/(sumVx*sumVx+sumVy*sumVy+sumVz*sumVz);
			if(fcmp(t,0.0)<=0) t=0.0;
			double res=cal(t);
			printf("Case #%d: %.8f %.8f\n",cas++,sqrt(res),t);
		}
	}
	return 0;
}