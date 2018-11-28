#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

const double eps=1e-8;
int T;
int D,C;
int cnt,x,y;
int a[1000005];
double b[1000005];

bool check(double x)
{
	b[0]=a[0]-x;
	for(int i=1;i<cnt;i++)
	{
		if(a[i]>b[i-1]+D)
			b[i]=max(b[i-1]+D,a[i]-x);
		else
			if(a[i]+x<b[i-1]+D)
				return false;
			else
				b[i]=b[i-1]+D;
	}
	return true;
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		cnt=0;
		scanf("%d%d",&C,&D);
		for(int i=0;i<C;i++)
		{
			scanf("%d%d",&x,&y);
			for(int j=0;j<y;j++)
				a[cnt++]=x;
		}
		double l=0,r=1e12;
		while(l+eps<r)
		{
			double mid=(l+r)/2;
			if(check(mid))
				r=mid;
			else
				l=mid;
		}
		printf("Case #%d: %f\n",test,l);
	}
	return 0;
}

