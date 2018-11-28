#include <stdio.h>
#include <math.h>

int main()
{
	int T;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	int w=1,n,i;
	double x,y,z,vx,vy,vz,X,Y,Z,VX,VY,VZ,a,b,ans,t;
	while(T--)
	{
		printf("Case #%d: ",w);
		w++;
		scanf("%d",&n);
		x=y=z=vx=vy=vz=0;
		for(i=0;i<n;i++)
		{			
			scanf("%lf%lf%lf%lf%lf%lf",&X,&Y,&Z,&VX,&VY,&VZ);
			x=x+X;
			y=y+Y;
			z=z+Z;
			vx=vx+VX;
			vy=vy+VY;
			vz=vz+VZ;
		}
		a=vx*vx+vy*vy+vz*vz;
		b=vx*x+vy*y+vz*z;
		if(b>0 || a==0)
			t=0;
		else
			t=-b/a;
		ans=(x+t*vx)*(x+t*vx)+(y+t*vy)*(y+t*vy)+(z+t*vz)*(z+t*vz);
		ans/=(n*n);
		printf("%.8lf %.8lf\n",sqrt(ans),t);
	}
	return 0;
}