#include<stdio.h>

long long int pow2(long long int n);

int main()
{
	long long int t,c,n,k,m;

//	freopen("A-largel.in","r",stdin);
//	freopen("outputlll.out","w",stdout);

	scanf("%lld",&t);

	for(c=1;c<=t;c++)
	{
		scanf("%lld%lld",&n,&k);

		m=pow2(n);

		k++;

		if(k%m==0)
			printf("Case #%d: ON\n",c);
		else
			printf("Case #%d: OFF\n",c);
	}
	
	return 0;
}

long long int pow2(long long int n)
{
	long long int i,s;

	for(i=1,s=1;i<=n;s*=2,i++);

	return s;
}
