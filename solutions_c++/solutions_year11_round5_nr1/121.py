#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#pragma warning (disable:4996)

#define M 150

struct D{int x,y;}a[M],b[M];


int main()
{
	int t,T=0;
	int i,j,k,n,m,w,part;
	double now,t1,t2,obj,y1,y2,x1,dx,x2;

	freopen("input.txt","r",stdin);
	freopen("output2.txt","w",stdout);

	for(scanf("%d",&t);t--;)
	{
		scanf("%d%d%d%d",&w,&m,&n,&part);
		
		for(i=1;i<=m;++i) scanf("%d%d",&b[i].x,&b[i].y);
		for(i=1;i<=n;++i) scanf("%d%d",&a[i].x,&a[i].y);

		k=0;
		for(i=1;i<n;++i) k+=(a[i+1].y+a[i].y)*(a[i+1].x-a[i].x);
		for(i=1;i<m;++i) k-=(b[i+1].y+b[i].y)*(b[i+1].x-b[i].x);
		obj=k/2./part;
		k=1;

		t1=(a[2].y-a[1].y)/double(a[2].x-a[1].x);
		t2=(b[2].y-b[1].y)/double(b[2].x-b[1].x);
		i=1;
		j=1;
		now=obj;
		printf("Case #%d:\n",++T);
		x1=0;
		y1=a[1].y-b[1].y;
		while(i<n && j<m)
		{
			if(t1!=t2)
			{
				if(now*2*(t1-t2)+y1*y1>0) // at least possible
				{
					dx=(sqrt(now*2*(t1-t2)+y1*y1)-y1)/(t1-t2);
					x2=(-sqrt(now*2*(t1-t2)+y1*y1)-y1)/(t1-t2);
					if(dx<0 || (x2>0 && x2<dx)) dx=x2;
				}
				else
					dx=100000;
			}
			else dx=now/y1;

			if(x1+dx<=a[i+1].x+0.000000001 && x1+dx<=b[j+1].x+0.000000001)
			{
				x1+=dx;
				y1+=dx*(t1-t2);
				printf("%.9f\n",x1);
				if(++k==part) break;
				now=obj;

				if(fabs(x1-a[i+1].x)<0.000000001) ++i;
				if(fabs(x1-b[j+1].x)<0.000000001) ++j;
			}
			else if(a[i+1].x<b[j+1].x)
			{
				dx=a[i+1].x-x1;
				y2=y1+dx*(t1-t2);
				now-=(y1+y2)/2*dx;

				y1=y2;
				x1=a[i+1].x;

				if(++i==n) break;
				t1=(a[i+1].y-a[i].y)/double(a[i+1].x-a[i].x);
			}
			else
			{
				dx=b[j+1].x-x1;
				y2=y1+dx*(t1-t2);
				now-=(y1+y2)/2*dx;

				y1=y2;
				x1=b[j+1].x;

				if(++j==m) break;
				t2=(b[j+1].y-b[j].y)/double(b[j+1].x-b[j].x);
			}
		}
	}
	return 0;
}
