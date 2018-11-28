#include <iostream>
#include <cstdio>
#include <cmath>
#define sqr(x) ((x)*(x))
using namespace std;
int main()
{
	int ks,i,t,n,ax,ay,az,bx,by,bz,fx,fy,fz,vx,vy,vz;
	double cx,cy,cz,dx,dy,dz,time,dist;
	cin >> ks;
for (t=1;t<=ks;t++)
{
	cin >> n;
	ax=ay=az=bx=by=bz=0;
	for (i=0;i<n;i++)
	{
		cin >> fx >> fy >> fz >> vx >> vy >> vz;
		ax+=fx;
		ay+=fy;
		az+=fz;
		bx+=vx;
		by+=vy;
		bz+=vz;
	}
	cx=double(ax)/n;
	cy=double(ay)/n;
	cz=double(az)/n;
	dx=double(bx)/n;
	dy=double(by)/n;
	dz=double(bz)/n;
	if ((sqr(dx)+sqr(dy)+sqr(dz))<1e-9)
		time=0;
	else		
		time=-(cx*dx+cy*dy+cz*dz)/(dx*dx+dy*dy+dz*dz);
	if (time<0)
		time=0;
	dist=sqrt(sqr(cx+dx*time)+sqr(cy+dy*time)+sqr(cz+dz*time));
	printf("Case #%d: %0.9f %0.9f\n",t,dist,time);
}
}

