#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;
const int V=1200;
double X,Y,r[V],x[V],y[V],d,dx,dy,tr;
int _,ca,i,n;
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&_);
	for(ca=1;ca<=_;ca++)
	{
		scanf("%d%lf%lf",&n,&X,&Y);
		d=sqrt(X*X+Y*Y);dx=X;dy=Y;
		for(i=0;i<n;i++)scanf("%lf",&r[i]);
		x[0]=0.0;y[0]=0.0;
		for(i=1;i<n;i++)
		{
			tr=r[i-1]+r[i];
			x[i]=x[i-1]+tr/d*dx+0.00000001;
			y[i]=y[i-1]+tr/d*dy+0.00000001;
		}
		printf("Case #%d:",ca);
		for(i=0;i<n;i++)printf(" %.9f %.9f",x[i],y[i]);puts("");
	}
}
