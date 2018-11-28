#include <iostream>
#include <cmath>
using namespace std;

typedef struct  
{
	double x,y,z;
	double vx,vy,vz;
}Node;

Node key[600];

int N;
double xx,vxx,yy,vyy,zz,vzz;
double ret,ans;

inline void slove()
{
	ans=0;
	double a,b,c;

	a=vxx*vxx+vyy*vyy+vzz*vzz;
	b=2*xx*vxx+2*yy*vyy+2*zz*vzz;
	c=xx*xx+yy*yy+zz*zz;
		
	if(a==0)
	{
		ret=0;ans=c;
	}
	else
	{
		if(b/(2*a)<=0)
		{
			ret=-b/(2*a);
			ans=ret*ret*a+ret*b+c;	
		}
		else 
		{
			ret=0;
			ans=c;	
		}	
	}
		
	ans=sqrt(ans+1e-10);
}



int main()
{
	int T;

	freopen("BL.in","r",stdin);
	freopen("BL.txt","w",stdout);
	scanf("%d",&T);
	int bb=1;

	while (T--)
	{
		
		scanf("%d",&N);

		int i;

		for (i=0;i<N;++i)
		{
			scanf("%lf%lf%lf%lf%lf%lf",&key[i].x,&key[i].y,&key[i].z,&key[i].vx,&key[i].vy,&key[i].vz);
		}

		xx=vxx=yy=vyy=zz=vzz=0;

		for(i=0;i<N;++i)
		{
		    xx+=key[i].x;
			vxx+=key[i].vx;
			yy+=key[i].y;
			vyy+=key[i].vy;
			zz+=key[i].z;
			vzz+=key[i].vz;	
		}

		xx/=N;
		yy/=N;
		zz/=N;
		vxx/=N;
		vyy/=N;
		vzz/=N;
		
		slove();
		printf("Case #%d: ",bb++);
		printf("%.8lf %.8lf\n",ans,ret+1e-6);
		
	}
	return 0;
}