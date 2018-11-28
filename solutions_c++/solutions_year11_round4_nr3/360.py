#include <stdio.h>

int p(long long x)
{
	long long i;
	if (x<2) return 0;
	if (x==2) return 1;
	if ((x&1)==0) return 0;
	for (i=3;i*i<=x;i+=2) if ((x%i)==0) return 0;
	return 1;
}

int main()
{
	int ic,nc;
	long long n,i,s,j;
	scanf("%d",&nc);
	for (ic=1;ic<=nc;++ic)
	{
		scanf("%lld",&n);
		if (n==1) s=0; else
		{
			s=1;
			for (i=2;i*i<=n;++i) if (p(i))
			{
				j=i;
				while (j*i<=n) { j*=i; ++s; }
			}
		}
		printf("Case #%d: %lld\n",ic,s);
	}
	return 0;
}
