#include <cstdio>
int main()
{
	freopen("1.in","r",stdin);
	//Oh my god..
	freopen("1.out","w",stdout);
	
	long casen,n,k;
	scanf("%ld",&casen);
	for(long i=1;i<=casen;++i)
	{
		scanf("%ld%ld",&n,&k);
		k%=(1<<n);
		if(k==(1<<n)-1)
			printf("Case #%ld: ON\n",i);
		else
			printf("Case #%ld: OFF\n",i);
	}
	return 0;
}
