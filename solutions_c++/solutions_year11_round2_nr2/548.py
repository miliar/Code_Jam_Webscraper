#include <cstdio>
#include <algorithm>
using namespace std;
#define eps 1e-8
#define max(a,b) (a>b?a:b)
const int maxn=1000005;
int n,D,C,P,V,test;
double a[maxn],b[maxn],l,r,mid;

bool Check(double t)
{
	for (int i=1;i<=n;i++)
	{
		b[i]=a[i];
		if (i==1) b[i]-=t; else
		if (b[i]-b[i-1]>=D) b[i]=max(b[i]-t,b[i-1]+D); else
		{
			if (b[i]+t-b[i-1]<D) return 0;
			b[i]=b[i-1]+D;
		}
	}
	return 1;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d",&test);
	for (int kase=1;kase<=test;kase++)
	{
		scanf("%d%d",&C,&D);
		n=0;
		for (int i=1;i<=C;i++)
		{
			scanf("%d%d",&P,&V);
			for (int j=1;j<=V;j++)
				a[++n]=P;
		}
		sort(a+1,a+n+1);
		for (l=0.0,r=1000000000.0;l+eps<r;)
		{
			mid=(l+r)/2;
			if (Check(mid)) r=mid; else l=mid;
		}
		printf("Case #%d: %.6lf\n",kase,r);
	}
	
	return 0;
}
