#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>
#include<vector>
#include<algorithm>
#include<iostream>
using namespace std;
#define eps 1e-8
struct Point
{
	double x,y;
	Point(){}
	Point(double x0,double y0):x(x0),y(y0){}
	void in()
	{
		scanf("%lf %lf",&x,&y);
	}
	void out()
	{
		printf(" %.2f %.2f",x,y);
	}
}p[1010];
double r[1010];
double w,l;
double dis(Point a,Point b)
{
	return (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y);
}
bool judge(double x,double y,int id)
{
	Point q=Point(x,y);
	for(int i=0;i<id;i++)
	{
		if(dis(p[i],q)-(1e-4) < (r[i]+r[id])*(r[i]+r[id]))
			return false;
	}
	return true;
}
bool can(double x,double y)
{
	if(0 <= x && x <= w && 0 <= y && y <= l)
		return true;
	else
		return false;
}
void change(double &x)
{
	long long f=x*100;
	x=1.0*f/100;
	x+=0.01;
}
int main()
{
	freopen("r","r",stdin);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int n;
		scanf("%d %lf %lf",&n,&w,&l);
		for(int i=0;i<n;i++)
			scanf("%lf",&r[i]);
		while(1)
		{
			bool flag=true;
			p[0]=Point(0,0);
			double x,y;
			double xx,yy;
			for(int i=1;i<n && flag;i++)
			{
				x=w;
				y=l;
				double step=min(w,l)/2;
				while(step > eps)
				{
//					printf("%.4f %.4f\n",x,y);
					step=step*0.98;
					if(rand()&1)
					{
						xx=x;
						yy=y-step;
//						printf("%.4f %.4f\n",xx,yy);
						if(can(xx,yy) && judge(xx,yy,i))
						{
							x=xx;
							y=yy;
							continue;
						}
						xx=x-step;
						yy=y;
						if(can(xx,yy) && judge(xx,yy,i))
						{
							x=xx;
							y=yy;
							continue;
						}
					}
					else
					{
						xx=x-step;
						yy=y;
						if(can(xx,yy) && judge(xx,yy,i))
						{
							x=xx;
							y=yy;
							continue;
						}
						xx=x;
						yy=y-step;
						if(can(xx,yy) && judge(xx,yy,i))
						{
							x=xx;
							y=yy;
							continue;
						}
					}
				}
				change(x);
				change(y);
				p[i]=Point(x,y);
				if(!judge(x,y,i) || !can(x,y))
					flag=false;
			}
//			for(int i=0;i<n;i++)
//				p[i].out();
//			printf("\n");
			if(flag)
				break;
		}
//		for(int i=0;i<n;i++)
//			for(int j=i+1;j<n;j++)
//				if(dis(p[i],p[j])-(1e-4) < (r[i]+r[j])*(r[i]+r[j]))
//					printf("fuck!\n");
		printf("Case #%d:",cc);
		for(int i=0;i<n;i++)
			p[i].out();
		printf("\n");
	}
	return 0;
}
/*
123
10 10000 10000
1 1 1 1 1 1 1 1 1 1




1
3 320 2
4 2 3



1
10 6817034 71890
57504 77875 12516 54881 51785 76658 67820 28944 13214 67000

 *
 */

