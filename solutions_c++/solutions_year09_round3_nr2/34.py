#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt,ii,n,i;
	double mx,my,mz,dx,dy,dz,x,y,z,t,x0,y0,z0,d;
	cin>>tt;
	for(ii=1;ii<=tt;ii++)
	{
		cin>>n;
		mx=my=mz=0;
		dx=dy=dz=0;
		for(i=0;i<n;i++)
		{
			cin>>x>>y>>z;
			mx+=x;
			my+=y;
			mz+=z;
			cin>>x>>y>>z;
			dx+=x;
			dy+=y;
			dz+=z;
		}
		mx/=n;
		my/=n;
		mz/=n;
		dx/=n;
		dy/=n;
		dz/=n;
		
		x=mx; y=my; z=mz;
		if(dx==0 && dy==0 && dz==0) t=0;
		else t=-(x*dx+y*dy+z*dz)/(dx*dx+dy*dy+dz*dz);
		if(t<0) t=0;
		x0=x+t*dx;
		y0=y+t*dy;
		z0=z+t*dz;
		d=sqrt(x0*x0+y0*y0+z0*z0);
		cout.precision(8);
		cout.setf(ios::fixed);
		cout<<"Case #"<<ii<<": "<<d<<' '<<t<<endl;
	}
	return 0;
}

