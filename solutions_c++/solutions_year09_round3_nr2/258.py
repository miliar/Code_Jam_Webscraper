#include<iostream>
#include<sstream>
#include<string>
#include<cmath>
using namespace std;

double sx=0.0,sy=0.0,sz=0.0,svx=0.0,svy=0.0,svz=0.0;

double Calc(double time)
{
	double tx=sx+svx*time;
	double ty=sy+svy*time;
	double tz=sz+svz*time;
	return sqrt(tx*tx+ty*ty+tz*tz);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int cas=1;
	int t,i,j,k,n;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",cas);
		cas++;
		double x=0.0,y=0.0,z=0.0,vx=0.0,vy=0.0,vz=0.0;
		sx=0.0,sy=0.0,sz=0.0,svx=0.0,svy=0.0,svz=0.0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%lf%lf%lf%lf%lf%lf",&x,&y,&z,&vx,&vy,&vz);
			sx+=x;sy+=y;sz+=z;
			svx+=vx;svy+=vy;svz+=vz;
		}
		sx/=n;sy/=n;sz/=n;
		svx/=n;svy/=n;svz/=n;
		if((fabs(svx)<0.0000000001)&&(fabs(svy)<0.0000000001)&&(fabs(svy)<0.0000000001))
		{
			printf("%.8lf %.8lf\n",Calc(0.0),0.0);
			continue;
		}
	double Left, Right;
    double mid, midmid;
    double mid_value, midmid_value;
    Left = 0; Right = 100000000000;
	double EPS=0.000000001;
    while (Left + EPS < Right)
    {
        mid = (Left + Right) / 2;
        midmid = (mid + Right) / 2;
        mid_value = Calc(mid);
        midmid_value = Calc(midmid);
        if (mid_value >= midmid_value) Left = mid;
        else Right = midmid;
    }
	mid = (Left + Right) / 2;
	printf("%.8lf %.8lf\n",Calc(mid),mid);
	}
	return 0;
}
