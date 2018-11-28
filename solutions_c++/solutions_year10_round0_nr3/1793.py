#include <cstdio>
long long a[5000];
long long next[5005],profit[5005];
int main()
{
	freopen("theme.in","r",stdin);
	freopen("theme.out","w",stdout);
	long long i,j,r,k,n,nod,rez,T,t,cap;
	scanf("%lld",&T);
	for (t=1;t<=T;t++)
	{
		scanf("%lld%lld%lld",&r,&k,&n);
		for (i=1;i<=n;i++)
		{
			scanf("%lld",&a[i]);
			a[i+n]=a[i];
		}
		for (i=1;i<=n;i++)
		{
			cap=0;
			for (j=i;cap+a[j]<=k&&j<i+n;j++)
			{
				cap+=a[j];
			}
			if (j>n)
				j-=n;
			next[i]=j;
			profit[i]=cap;
		}
		nod=1;
		rez=0;
		for (i=1;i<=r;i++)
		{
			rez+=profit[nod];
			nod=next[nod];
		}
		printf("Case #%lld: %lld\n",t,rez);
	}
	return 0;
}
