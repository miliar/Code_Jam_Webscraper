#include <stdio.h>
#include <algorithm>
using namespace std;
struct ab
{
	int beg,end,wi;
}a[1005];
int cmp(const void *x,const void *y)
{
	ab xx=*(ab *)x;
	ab yy=*(ab *)y;
	return xx.wi-yy.wi;
}
int cmp2(const void *x,const void *y)
{
	ab xx=*(ab *)x;
	ab yy=*(ab *)y;
	return xx.end-yy.end;
}
int main ()
{
	int cas,ca;
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	double x,s,t,r,ans,tt,bs;
	int i,n;
	scanf("%d",&cas);
	for(ca=1;ca<=cas;ca++)
	{
		scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
		for(i=0;i<n;i++)
		{
			scanf("%d%d%d",&a[i].beg,&a[i].end,&a[i].wi);
		}
		ans=0;


		qsort(a,n,sizeof(a[0]),cmp2);
		bs=0;
		if(a[0].beg>0)
			bs+=a[0].beg;
		for(i=1;i<n;i++)
		{
			if(a[i].beg>a[i-1].end)
			{
				bs+=a[i].beg-a[i-1].end;
			}
		}
		if(a[n-1].end<x)
			bs+=x-a[n-1].end;
		if(t>0)
		{
			tt=bs/r;//È«³ÌÅÜ
			if(t>tt)
			{
				ans+=tt;
				t-=tt;
			}
			else
			{
				double ss=r*t;
				ans=ans+t+(bs-ss)/s;
				t=0;
			}
		}
		else
		{
			ans=ans+bs/s;
			t=0;
		}




		qsort(a,n,sizeof(a[0]),cmp);
		for(i=0;i<n;i++)
		{
			if(t>0)
			{
				tt=(a[i].end-a[i].beg)/(r+a[i].wi);
				if(t>tt)
				{
					t-=tt;
					ans+=tt;
				}
				else
				{
					double ss=(r+a[i].wi)*t;
					ans=ans+t+(a[i].end-a[i].beg-ss)/(s+a[i].wi);
					t=0;
				}
			}
			else
			{
				ans+=(a[i].end-a[i].beg)/(s+a[i].wi);
			}
		}

		printf("Case #%d: %.7lf\n",ca,ans);

	}
}