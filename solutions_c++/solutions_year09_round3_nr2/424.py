#include <stdio.h>
#include <math.h>
const double eps=1e-9;
int main()
{
	int t,i,j,k,t1;
	double x,y,z,zx,zy,zz,t2,x1,y1,z1,d;
    freopen("B-small-attempt0.in","r",stdin);
   freopen("out1.txt","w",stdout);
    scanf("%d",&t);
    t1=1;
    while(t--)
    {
        int n;
		x=0,y=0,z=0,zx=0,zy=0,zz=0;
        scanf("%d",&n);   
        for(int i=0;i<n;i++)
        {
            double rx,ry,rz,ra,rb,rc;
            scanf("%lf%lf%lf%lf%lf%lf",&rx,&ry,&rz,&ra,&rb,&rc);
        x+=rx;
        y+=ry;
        z+=rz;
        zx+=ra;
        zy+=rb;
       zz+=rc;
        }
		x/=n;
		y/=n;
		z/=n;
		zx/=n;
		zy/=n;
		zz/=n;
        
		if((zx*zx+zy*zy+zz*zz)<eps)
		{
			t2=0;
		}
		else
			t2=-(zx*x+zy*y+zz*z)/(zx*zx+zy*zy+zz*zz);
        if(t2<0)t2=0;
        x1=x+zx*t2;
        y1=y+zy*t2;
        z1=z+zz*t2;
        d=sqrt((x1)*(x1)+(z1)*(z1)+(y1)*(y1));
        printf("Case #%d: %.8lf %.8lf\n",t1,d,t2);
		t1++;
    }
} 