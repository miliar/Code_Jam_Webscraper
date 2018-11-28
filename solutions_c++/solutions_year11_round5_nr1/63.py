#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#define eps 1E-12

using namespace std;

struct T
{
	double x,y;
}a[200],b[200],low,high;
int n,m,k,nn,mm,kk,i,T,ts;
double w,l,r,c,s,ans[200];

double sq()
{
	int i;
	double s=0;
	for(i=0;i<m-1;i++)
		s+=b[i].x*b[i+1].y-b[i].y*b[i+1].x;
	s+=b[m-1].x*a[n-1].y-a[n-1].x*b[m-1].y;
	for(i=0;i<n-1;i++)
		s+=a[i+1].x*a[i].y-a[i].x*a[i+1].y;
	s+=a[0].x*b[0].y-a[0].y*b[0].x;
	if(s<0)
		s=-s;
	return s;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%lf%d%d%d",&w,&n,&m,&k);
		for(i=0;i<n;i++)
			scanf("%lf%lf",&a[i].x,&a[i].y);
		for(i=0;i<m;i++)
			scanf("%lf%lf",&b[i].x,&b[i].y);
		s=sq()/k;
		kk=k;
		while(k--)
		{
			if(!k)
				break;
			l=0;
			r=w;
			while(r-l>eps)
			{
				c=(l+r)/2;
				for(i=0;i<n;i++)
					if(a[i].x>=c)
						break;
				if(i==n)
					i--;
				low=a[i];
				a[i].y=(c-a[i-1].x)/(a[i].x-a[i-1].x)*(a[i].y-a[i-1].y)+a[i-1].y;
				a[i].x=c;
				nn=n;
				n=i+1;
				for(i=0;i<m;i++)
					if(b[i].x>=c)
						break;
				if(i==m)
					i--;
				high=b[i];
				b[i].y=(c-b[i-1].x)/(b[i].x-b[i-1].x)*(b[i].y-b[i-1].y)+b[i-1].y;
				b[i].x=c;
				mm=m;
				m=i+1;
				if(sq()>s*k)
					r=c;
				else
					l=c;
				a[n-1]=low;
				b[m-1]=high;
				n=nn;
				m=mm;
			}
			ans[k-1]=l;
			c=l;
			w=c;
			for(i=0;i<n;i++)
				if(a[i].x>=c)
					break;
			if(i==n)
				i--;
			a[i].y=(c-a[i-1].x)/(a[i].x-a[i-1].x)*(a[i].y-a[i-1].y)+a[i-1].y;
			a[i].x=c;
			n=i+1;
			for(i=0;i<m;i++)
				if(b[i].x>=c)
					break;
			if(i==m)
				i--;
			b[i].y=(c-b[i-1].x)/(b[i].x-b[i-1].x)*(b[i].y-b[i-1].y)+b[i-1].y;
			b[i].x=c;
			m=i+1;
		}
		printf("Case #%d:\n",++ts);
		for(i=0;i<kk-1;i++)
			printf("%.12lf\n",ans[i]);
	}
	return 0;
}