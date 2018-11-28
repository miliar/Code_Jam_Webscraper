#include <stdio.h>
#include <math.h>

typedef struct Circle
{
	double x,y,r;
}Circle;

Circle C[41];
int N;
bool adj[41][41];
int Cmp(double a,double b)
{
	if (fabs(a-b)<1e-9) return 0;
	else if (a>b) return 1;
	else return -1;
}

double Dis(double x,double y,double xx,double yy)
{return sqrt((x-xx)*(x-xx)+(y-yy)*(y-yy));}

bool Cross(Circle &A,Circle &B)
{return Cmp(Dis(A.x,A.y,B.x,B.y),(A.r+B.r)) <=0 ;}

bool Check(Circle A,Circle B,Circle X,double R)
{
	A.r = R - A.r;
	B.r = R - B.r;
	return Cross(A,B);
}
bool Check(double R)
{
	Circle A,B;
	bool ret = 	  Check(C[0],C[1],C[2],R)
				||Check(C[1],C[2],C[0],R)
				||Check(C[2],C[0],C[1],R);
	return ret;
}
int main()
{
	freopen("D-Small.txt","w",stdout);
	double low,up,mid,minr;
	int t,st,i;
	scanf("%d",&st);
	for (t=0;t<st;++t)
	{
		scanf("%d",&N);
		minr = -1;
		for (i=0;i<N;++i)
		{
			scanf("%lf %lf %lf",&C[i].x,&C[i].y,&C[i].r);
			if (minr <0 || minr<C[i].r) minr = C[i].r;
		}
		if (N<3)
		{
			printf("Case #%d: %.6lf\n",t+1,minr);
			continue;
		}
		low = minr;up =2000;
		for (i=0; fabs(up-low)>=1e-8 && low<up;++i)
		{
			mid = (up+low)/2;
			if (Check(mid)) up = mid;
			else low = mid;
		}
		printf("Case #%d: %.6lf\n",t+1,mid);
	}
	return 0;
}


