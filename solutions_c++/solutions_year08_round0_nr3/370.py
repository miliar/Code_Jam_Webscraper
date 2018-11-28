#include<stdio.h>
#include<math.h>
#include<assert.h>

double x[5000][3],PI;

struct POINT
{
	double x,y;
}P1,P2;

double CALC(double R,double x1,double x2,double y1,double y2)
{
	int in1,in2,in3,in4;
	double extra,angle,area;

	in1=(x1*x1+y1*y1<=R*R);
	in2=(x1*x1+y2*y2<=R*R);
	in3=(x2*x2+y2*y2<=R*R);
	in4=(x2*x2+y1*y1<=R*R);

	if(in3) return (x2-x1)*(y2-y1);
	if(!in1) return 0;

	if(in2 && in4)
	{
		P1.y=y2;
		P1.x=sqrt(R*R-y2*y2);
		P2.x=x2;
		P2.y=sqrt(R*R-x2*x2);
	}
	else if(in2)
	{
		P1.y=y2;
		P1.x=sqrt(R*R-y2*y2);
		P2.y=y1;
		P2.x=sqrt(R*R-y1*y1);
	}
	else if(in4)
	{
		P1.x=x1;
		P1.y=sqrt(R*R-x1*x1);
		P2.x=x2;
		P2.y=sqrt(R*R-x2*x2);
	}
	else
	{
		P1.x=x1;
		P1.y=sqrt(R*R-x1*x1);
		P2.y=y1;
		P2.x=sqrt(R*R-y1*y1);
	}

	extra=(P1.x-x1)*(P1.y-y1)+(P2.x-P1.x)*(P2.y-y1);

	angle=-atan2(P2.y,P2.x)+atan2(P1.y,P1.x);

	area=R*R/2.*angle - .5*fabs(P1.x*P1.y-P2.y*P1.x) - .5*fabs(P1.x*P2.y-P2.y*P2.x);

	return area+extra;
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	PI=acos(-1.);
	double R,t,r,g,f;
	int i,cnt,ks,Q,j;
	double start,thick,total,blank;
	
	scanf("%d",&Q);
	for(ks=1;ks<=Q;ks++)
	{
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		total=PI*R*R;

		R-=f+t;
		start=r+f;
		thick=g-2*f;
		cnt=0;
		while(start<R)
		{
			x[cnt][0]=start;
			x[cnt][1]=start+thick;
			cnt++;
			start+=thick+2*r+2*f;
		}

		blank=0;
		for(i=0;i<cnt;i++)
			for(j=0;j<cnt;j++)
			{
				if(i==9)
					i=9;
				blank+=CALC(R,x[i][0],x[i][1],x[j][0],x[j][1]);
			}
		blank*=4;

		printf("Case #%d: %.6lf\n",ks,1.-blank/total);
	}

	return 0;
}