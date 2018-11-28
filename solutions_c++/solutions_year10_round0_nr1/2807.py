#include<stdio.h>

int main()
{
	int i,j,t,n;
	long k,l;
	freopen("a.in", "r",stdin);
	freopen("a.out", "w", stdout);
	scanf("%lld", &t);
	for(i=0; i<t; i++)
	{
		scanf("%d%lld", &n,&k);
		
		l=((long long)1<<(n))-1;
		k&=l;
		if(k!=l || k==0)
			j=0;
		else
			j=1;
		printf("Case #%d: %s\n", i+1, j?"ON":"OFF");
	}
	return 0;
}