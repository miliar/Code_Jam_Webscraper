#pragma warning(disable:4786)
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <algorithm>
#include <set>
#include <cmath>
using namespace std;
double sqr(double x)
{
	return x*x;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca,i,n;
	double x,y,z,xt,yt,zt,vx,vy,vz,vxt,vyt,vzt,ans,t;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++)
	{
		scanf("%d",&n);
		x=y=z=vx=vy=vz=0;
		for (i = 0 ; i < n ; i++)
		{
			scanf("%lf%lf%lf%lf%lf%lf",&xt,&yt,&zt,&vxt,&vyt,&vzt);
			x+=xt; y+=yt; z+=zt; vx+=vxt; vy+=vyt; vz+=vzt;
		}
		if(vx*vx+vy*vy+vz*vz == 0) t = 0;
		else t = - (x*vx+y*vy+z*vz) / (vx*vx+vy*vy+vz*vz);
		if (t < 0 ) t = 0;
		ans = sqrt(sqr(x+t*vx)+sqr(y+t*vy)+sqr(z+t*vz)) / n;
		printf("Case #%d: %lf %lf\n",ca,ans,t);

	}

	return 0;
}
