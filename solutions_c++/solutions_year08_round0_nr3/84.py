#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double event_point[20002];
double ep[20002];
int ind,ind2;

int cmp(const void *a,const void *b)
{
	if( *(double *)a > *(double *)b)
		return 1;
	return -1;
}

int main()
{
	double tmp;
	double pi = 2*acos(0.0);
	double tmpx,tmpy;
	double outer_fan,inner_fan,theta;
	double area;
	double x,y,ny;
	int asd,n;
	double total_area;
	double f,R,t,r,g;
	int i,mode;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&n);
	for(asd=0;asd<n;asd++)
	{
		scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
		g-=2.0*f;

		r+=f;
		t+=f;
		total_area = R*R*pi;
		R-=t;

		if(g<=0 || f>=R || r>=R)
		{
			printf("Case #%d: %.6lf\n",asd+1,1.0);
			continue;
		}
		
		ind=0;

		x=r;
		while(x<R)
		{
			event_point[ind++]=x;
			x+=g;
			if(x>=R)
				break;
			event_point[ind++]=x;
			x+=2*r;
		}
		y = r;
		while(y<R)
		{
			x = sqrt(R*R - y*y);
			event_point[ind++]=x;
			y+=g;
			if(y>=R)
				break;
			x = sqrt(R*R - y*y);
			event_point[ind++]=x;
			y+=2*r;
		}

		event_point[ind++] = 0;
		event_point[ind++] = R;


		qsort((void *)event_point,ind,sizeof(event_point[0]),cmp);
		
		ind2=0;
		ep[ind2++]=event_point[0];
		for(i=1;i<ind;i++)
		{
			if( fabs(event_point[i] - event_point[i-1]) >= 1e-10)
				ep[ind2++] = event_point[i];
		}
		area=0;

		for(i=1;i<ind2;i++)
		{
			x = -r;
			mode=1;
			while(x<R)
			{
				if(ep[i] >= x && ep[i] <= x+2*r && ep[i-1] >= x && ep[i-1] <= x+2*r)
				{
					mode=0;
					break;
				}
				x+=2*r;
				if(ep[i] >= x && ep[i] <= x+g && ep[i-1] >= x && ep[i-1] <= x+g)
				{
					mode=1;
					break;
				}
				x+=g;
			}
//			if(mode==-1)
//				abort();
			if(mode==0)
				continue;
			
			y = r;
			while(1)
			{

				if(y*y + ep[i]*ep[i] > R*R +1e-6)
					break;				

				ny = y + g;
				if( ny*ny + ep[i]*ep[i] > R*R + 1e-6)
				{
//					if( ny * ny + ep[i-1] * ep[i-1] <R*R - 1e-6)
//						abort();
					
					tmpx = ep[i];
					tmpy = sqrt(R*R - ep[i]*ep[i]);

					theta = atan2(tmpy,tmpx);
					outer_fan = R*R*theta/2.0 - R*R*sin(2.0*theta) / 4.0;

					tmpx = ep[i-1];
					tmpy = sqrt(R*R - ep[i-1]*ep[i-1]);

					theta = atan2(tmpy,tmpx);
					inner_fan = R*R*theta/2.0 - R*R*sin(2.0*theta) / 4.0;

					tmp = inner_fan - outer_fan - y * (ep[i] - ep[i-1]);

					area += tmp;
				}
				else
					area+=g*(ep[i] - ep[i-1]);
				y = ny + 2*r;
				if(y*y + ep[i]*ep[i] > R*R +1e-6 )
					break;
			}

		}
//		printf("%.2lf %.2lf %.2lf\n",area,R*R*pi /4.0 - 200 * 0.00002,total_area/4.0);
		printf("Case #%d: %.6lf\n",asd+1,1 - area/(total_area/4.0) + 1e-10);
	}

	return 0;
}
