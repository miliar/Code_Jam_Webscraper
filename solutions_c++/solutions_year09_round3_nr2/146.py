#include<cstdio>
#include<cmath>

#define y0 __y0

long long vx,vy,vz,x0,y0,z0;//2500000
int n;

double ansD,ansT;
void work()
{
	long long A = vx*vx + vy*vy + vz*vz;
	long long B = 2*( x0*vx+y0*vy+z0*vz );
	long long C = x0*x0 + y0*y0 + z0*z0;

	if( A==0 )
	{
		ansD = C;
		ansT = 0;
	}else
	{
		// -b/2a

		if( B>0 )
		{
			// opt is naga
			ansT = 0;
			ansD = C;
		}else
		{
			ansT = -0.5*B/A;
			ansD = (A*ansT+B)*ansT+C;
		}
	}
}
int main()
{
	int xx,yy,zz,vxx,vyy,vzz;
	int T;
	scanf("%d",&T);
	for( int TT=1;TT<=T;TT++ )
	{
		scanf("%d",&n);
		vx = vy = vz = x0 = y0 = z0 = 0;
		for(int i=0;i<n;i++)
		{
			scanf("%d%d%d%d%d%d",&xx,&yy,&zz,&vxx,&vyy,&vzz);
			vx+=vxx;
			vy+=vyy;
			vz+=vzz;
			x0+=xx;
			y0+=yy;
			z0+=zz;
		}

		work();
		printf("Case #%d: %.9lf %.9lf\n",TT,sqrt(ansD)/n,ansT);
	}
	return 0;
}
