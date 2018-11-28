#include <stdio.h>

int main()
{
	long long t,n,k,num,i,a;
	scanf("%lld",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%lld%lld",&n,&k);
		num = 1<<n;
		if(((num-1)&k) == (num-1))
		  printf("Case #%lld: ON\n",i);
		else
		  printf("Case #%lld: OFF\n",i);
	}
}
