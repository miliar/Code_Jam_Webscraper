#include<stdio.h>
#include<math.h>
int n;

void solve()
{
	scanf("%d",&n);
	double x=0,y=0,z=0;
	double tx,ty,tz;
	double vx=0,vy=0,vz=0;
	for(int i=0;i<n;++i)
	{
		scanf("%lf%lf%lf",&tx,&ty,&tz);
		x+=tx/n;
		y+=ty/n;
		z+=tz/n;
		scanf("%lf%lf%lf",&tx,&ty,&tz);
		vx+=tx/n;
		vy+=ty/n;
		vz+=tz/n;
	}
	double a=vx*vx+vy*vy+vz*vz,b=2*(x*vx+y*vy+z*vz),c=x*x+y*y+z*z;
	double ans;
	if(a<1e-10||-b/(2*a)<1e-12)
		ans=0;
	else ans=-b/(a*2);
	if(a*ans*ans+b*ans+c<1e-10)
		printf("%.10lf %.10lf\n",0.0,ans);
	else
		printf("%.10lf %.10lf\n",sqrt(a*ans*ans+b*ans+c),ans);
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
	{
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}

