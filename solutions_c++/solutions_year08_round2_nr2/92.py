#include <stdio.h>

long long xx[2000000];
long long pp[2000000];
long long N;

long long pr(long long x)
{
	long long i;
	for (i=2;i*i<=x;++i) if ((x%i)==0) return 0;
	return 1;
}

long long h(long long x)
{
	long long i,j;
	i=0;
	while (xx[x]!=x) 
	{
		pp[i]=x;
		x=xx[x];
		++i;
	}
	for (j=0;j<i;++j) xx[pp[j]]=x;
	return x;
}

long long m(long long a,long long b)
{
	xx[h(a)]=h(b);
}

int main()
{
	long long i,k,j,ii,n,a,b,p;
	scanf("%lld",&n);
	for (ii=0;ii<n;++ii)
	{
		scanf("%lld %lld %lld",&a,&b,&p);
		N=b-a+1;
		for (i=0;i<N;++i) xx[i]=i;
		for (i=p;i<=N;++i) if (pr(i))
		{
			j=i-(a%i);
			if (j==i) j=0;
			for (k=1;(j+i*k)<N;++k) m(j,j+i*k);
		}
		j=0;
		for (i=0;i<N;++i) if (xx[i]==i) ++j;
		printf("Case #%lld: %lld\n",ii+1,j);
	}
	return 0;
}
