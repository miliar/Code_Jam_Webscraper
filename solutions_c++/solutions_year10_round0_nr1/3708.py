#include<stdio.h>
#include<fstream.h>

int main()
{
	freopen("A-large.in",  "r", stdin);
	freopen("A-large.out", "w", stdout);
	long t;
	scanf("%d",&t);
	long i;
	int n;
	unsigned long k;
	for(i=1;i<=t;i++)
	{
		scanf("%d%ld",&n,&k);
		unsigned long s =1;
		int j;
		for(j=1;j<=n;j++)s*=2;
		k=k+1;
		if(k%s==0)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}