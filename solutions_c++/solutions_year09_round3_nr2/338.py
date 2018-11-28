#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;



int main()
{
	int tt,pp;
	cin>>tt;
	pp=tt;
	while(tt--)
	{
		int n;
		cin>>n;
		double x[500],vx[500],y[500],z[500],vy[500],vz[500];
		double ax=0,bx=0,ay=0,az=0,bz=0,by=0,a,b,ab,t;
		double d;
		for(int i=0;i<n;i++)
		{
			cin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
			ax+=x[i];
			bx+=vx[i];
			ay+=y[i];
			by+=vy[i];
			az+=z[i];
			bz+=vz[i];
		}		
		ax/=n;bx/=n;
		by/=n;ay/=n;az/=n;bz/=n;
		a=ax*ax+ay*ay+az*az;
		b=bx*bx+by*by+bz*bz;
		ab=ax*bx+ay*by+az*bz;
		if(b!=0)
			t=(ab/b)*(-1);
		else
			t=0;
		if(t<0)
		{
			t=0;
		}
		d=pow((ax+bx*t),2.0)+pow((ay+by*t),2.0)+pow((az+bz*t),2.0);
		if(d<0)
			cout<<"Dsda";
			
		d=sqrt(d);
		printf("Case #%d: %0.8lf %0.8lf\n",pp-tt,d,t);
//		cout<<d<<" "<<t;	
		}	
    return 0;
}
