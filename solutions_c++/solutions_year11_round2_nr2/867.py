#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int a[220];
int v[220];

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t,c,d,i;
	long long sum,min,max,x,left,right;
	double tt,l,r;
	bool flag;
	scanf("%d",&t);
	for (int cnt=1;cnt<=t;cnt++)
	{
		scanf("%d%d",&c,&d);
		printf("Case #%d: ",cnt);
		for (i=1;i<=c;i++)
			scanf("%d%d",&a[i],&v[i]);
		a[0]=a[1]-d-1;
		sum=0;
		for (i=1;i<=c;i++)
		{
			if (a[i]-a[i-1]<d) sum+=d-a[i]+a[i-1];
			sum+=d*(v[i]-1);
		}
		min=0;
		max=sum;
		while (min<max)
		{
			x=(min+max)/2;
			left=a[1]-x;
			right=left+d*(v[1]-1);
			if (right-a[1]>x)
			{
				min=x+1;
				continue;
			}
			flag=false;
			for (i=2;i<=c;i++)
			{
				left=right+d;
				if (a[i]-x>left) left=a[i]-x;
				right=left+d*(v[i]-1);
				if (right-a[i]>x)
				{
					min=x+1;
					flag=true;
					break;
				}
			}
			if (flag) min=x+1;
			else max=x;
		}
			tt=min-0.5;
			l=a[1]-tt;
			r=l+d*(v[1]-1);
			flag=true;
			if (r-a[1]>tt)
			{
				flag=false;
			}
			for (i=2;i<=c;i++)
			{
				l=r+d;
				if (a[i]-tt>l) l=a[i]-tt;
				r=l+d*(v[i]-1);
				if (r-a[i]>tt)
				{
					flag=false;
				}
			}
			if (flag) printf("%lf\n",tt);
			else printf("%lf\n",(double)min);
	}
	return 0;
}