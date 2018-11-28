#include <stdio.h>

long long r,k,n,g[2000],t=0,s,i,to[2000],p[2000],j,b[2000],ss[2000],c;

int main()
{
	scanf("%lld",&n);
	while (scanf("%lld %lld %lld",&r,&k,&n)==3)
	{
		for (i=0;i<n;++i) scanf("%lld",g+i);
		for (i=0;i<n;++i)
		{
			s=g[i];
			for (j=(i+1)%n;j!=i;j=(j+1)%n)
			{
				if (s+g[j]>k) break; else s+=g[j];
			}
			to[i]=j;
			p[i]=s;
		}
		for (i=0;i<n;++i) b[i]=-1;
		i=j=s=0;
		while (i<r)
		{
			if (b[j]==-1 || 2*i>b[j]+r)
			{
				b[j]=i;
				ss[j]=s;
				s+=p[j];
				j=to[j];
				++i;
			} else
			{
				c=(r-i)/(i-b[j]);
				s+=c*(s-ss[j]);
				i+=c*(i-b[j]);
			}
		}
		printf("Case #%lld: %lld\n",++t,s);
	}
	return 0;
}