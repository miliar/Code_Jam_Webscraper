#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

#define eps 1e-9

int n;
int main()
{
	freopen("f.in","r",stdin);
	freopen("f.out","w",stdout);
	int i,j;
	int T;
	scanf("%d",&T);
	int x,y,z,vx,vy,vz;
	int case_cnt=1;
	while(T--)
	{
		int sum_x=0,sum_y=0,sum_z=0,sum_vx=0,sum_vy=0,sum_vz=0;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d%d%d%d%d%d",&x,&y,&z,&vx,&vy,&vz);
			sum_x+=x,sum_y+=y,sum_z+=z,sum_vx+=vx,sum_vy+=vy,sum_vz+=vz;
		}
		double x0,y0,z0,vx0,vy0,vz0;
		x0=(double)sum_x/(double)n,y0=(double)sum_y/(double)n,z0=(double)sum_z/(double)n;
		vx0=(double)sum_vx/(double)n,vy0=(double)sum_vy/(double)n,vz0=(double)sum_vz/(double)n;
		double a=vx0*vx0+vy0*vy0+vz0*vz0;
		double b=2*(x0*vx0+y0*vy0+z0*vz0);
		double c=x0*x0+y0*y0+z0*z0;
		printf("Case #%d: ",case_cnt++);
		if(a!=0)
		{
			double delta=b*b-4*a*c;
			double xx=-b/(2*a);
			double yy=(4*a*c-b*b)/(4*a);
			
			if(xx<0||fabs(xx)<eps)
			{
				double res_t=0,res=sqrt(c);
				printf("%.8f %.8f\n",res,res_t);
			}
			else
			{
				double res=yy;
				if(delta<0||fabs(delta)<eps)
					printf("%.8f %.8f\n",sqrt(yy),xx);
				else
				{
					double res_x;
					double res_x1=(-b-sqrt(delta))/(2*a);
					double res_x2=(-b+sqrt(delta))/(2*a);
					if(res_x1<res_x2&&res_x1>0)
						res_x=res_x1;
					else
						res_x=res_x2;
					printf("%.8f %.8f\n",0.0,res_x);
				}
			}
		}
		else
		{
			if(b>0)
			{
				printf("%.8f %.8f\n",sqrt(c),0.0);
			}
			else
			{
				if(b!=0)
					printf("%.8f %.8f\n",0.0,c/b);
				else
					printf("%.8f %.8f\n",sqrt(c),0.0);
			}
		}
	}
}