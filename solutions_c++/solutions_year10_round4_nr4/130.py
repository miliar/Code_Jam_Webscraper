#include <stdio.h>
#include <math.h>
int N,M;
double Px[100];
double Py[100];
double Qx[100];
double Qy[100];
double dist(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

double area(double r,double R,double d)
{
	printf("%1.20f,%1.20f,%1.20f\n",r,R,d);
	long double f1=r*r*acos((long double)(d*d+r*r-R*R)/(2*d*r));
	long double f2=R*R*acos((long double)(d*d+R*R-r*r)/(2*d*R));
	
	long double f3=-0.5*sqrt((long double)(R+r-d)*(d+r-R)*(d-r+R)*(d+r+R));
	
	
	printf("\nfs %lf %lf %lf\n",(double)f1,(double)f2,(double)f3);
	printf("answer is %lf\n",(double)(f1+f2+f3));
		return f1+f2+f3;
	
}
int B[100];
int main()
{
	int T;
	scanf("%d",&T);
	printf("A=[");
	for(int t=1;t<=T;t++)
	{
		scanf("%d %d",&N,&M);
		N=2;
		B[t]=M;
		for(int i=1;i<=N;i++)
			scanf("%lf %lf",&Px[i],&Py[i]);
		for(int i=1;i<=M;i++)
			scanf("%lf %lf",&Qx[i],&Qy[i]);
		//printf("Case #%d: ",t);
		for(int i=1;i<=M;i++)
		{		
			double r,R;
			

			r=dist(Px[1],Py[1],Qx[i],Qy[i]);
			R=dist(Px[2],Py[2],Qx[i],Qy[i]);
			
			double d;
			d=dist(Px[1],Py[1],Px[2],Py[2]);
			printf("%1.20f,%1.20f,%1.20f",r,R,d);
			
			//printf("%1.9f ",area(r,R,d));
			
			if(t==T && i==M)
				printf("]\n");
			else
				printf(";");
			
			

		}
		
		
	}
	printf("B=[");
	for(int t=1;t<=T;t++)
	{
		printf("%d",B[t]);
		if(t==T)
			printf("]");
		else
			printf(",");
	}
	
	
}