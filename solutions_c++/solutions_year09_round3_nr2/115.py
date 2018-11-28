#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

const int N = 1100;

int n;
double x[N],y[N],z[N],vx[N],vy[N],vz[N],
		sx,sy,sz,svx,svy,svz;

double f(double t)
{
	double xc =(sx+t*svx)/n, 
		yc=(sy+t*svy)/n,
		zc=(sz+t*svz)/n;
	double ret = sqrt(xc*xc+yc*yc+zc*zc);
	return ret;
}
int main()
{
	
	int i,j,k,test,len;

	int ca;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d", &ca);
	for(test=1;test<=ca;++test)
	{
		
		scanf("%d", &n);
		sx=sy=sz=svx=svy=svz=0;
		for(i=0;i<n;++i)
		{
			scanf("%lf%lf%lf%lf%lf%lf",
				x+i,y+i,z+i,vx+i,vy+i,vz+i);
			sx += x[i];
			sy += y[i];
			sz += z[i];
			svx += vx[i];
			svy += vy[i];
			svz += vz[i];
		}

		double x1 = -(sx*svx+sy*svy+sz*svz), x2=svx*svx+svy*svy+svz*svz;
		if(x2==0) x2 += 1e-8;
		double t = x1/x2, ans1, ans2;
		if(t<0) t=0.0;
		double ans;
		ans1 = f(0);
		ans2 = f(t);
		if(ans1 < ans2) 
		{
			ans = ans1;
			t = 0;
		}
		else ans = ans2;
		printf("Case #%d: %.8lf %.8lf\n", test, ans, t);
		

	}
	return 0;
}