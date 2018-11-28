#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int T;
int n;
int a[1005];
double b[1005];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		int sum=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			sum+=a[i];
		}
		double p=sum*2;
		double r=sum*2;
		double l=0;
		for(int j=0;j<=100;j++)
		{
			double m=(l+r)/2;
			double tt=0;
			for(int i=0;i<n;i++)
				if(a[i]>m)
					tt+=a[i];
				else
					tt+=m;
			if(tt>p)
				r=m;
			else
				l=m;
		}
		p=l;
		for(int i=0;i<n;i++)
			b[i]=(double)(p)-a[i];
		printf("Case #%d:",test);
		for(int i=0;i<n;i++)
		{
			double aa=(double)b[i]/sum*100;
			printf(" %.7f",aa>0?aa:0);
		}
		puts("");
	}
	return 0;
}

