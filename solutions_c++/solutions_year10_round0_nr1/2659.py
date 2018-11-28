#include<stdio.h>


int main()
{
	int t,T;
	scanf("%d",&T);
	for(t= 1;t<= T;t++)
	{
		long long n,k;
		scanf("%lld%lld",&n,&k);

		int twoPow= 1 << n;
		if( (k % twoPow)== (twoPow -1) )
			printf("Case #%d: ON\n",t);
		else
			printf("Case #%d: OFF\n",t);
	}
}
