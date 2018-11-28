#include <stdio.h>
int power(int a, int b)
{
	int r=1;
	for (int i=0;i<b;i++)
	{
		r*=a;
	}
	return r;
}
int main()
{
	int T,N,K;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		scanf("%d%d",&N,&K);
		int c=power(2,N);
		K=K%c;
		printf("Case #%d: ",i);
		if (K==c-1)
		{
			printf("ON\n");
		}
		else
		{
			printf("OFF\n");
		}
	}
}