#include <stdio.h>

int gcd(int a,int b)
{
	int r;
	while(b)
	{
		r = a%b;
		a = b;
		b = r;
	}
	return a;
}

int main ()
{
	int cas,i,k,d,g;
	__int64 n;
	freopen("A-large(1).in","r",stdin);
	freopen("A-large(1).out","w",stdout);
	scanf("%d",&cas);
	for(k = 1; k <= cas; k++)
	{
		scanf("%I64d",&n);
		scanf("%d%d",&d,&g);
		if(g==100)
		{
			if(d!=100)
			{
				printf("Case #%d: Broken\n",k);
			}
			else
			{
				printf("Case #%d: Possible\n",k);
			}
			continue;
		}
		if(g==0)
		{
			if(d!=0)
				printf("Case #%d: Broken\n",k);
			else
			{
				printf("Case #%d: Possible\n",k);
			}
			continue;
		}
		int tmp=gcd(d,100);
		if(100/tmp <= n)
		{
			printf("Case #%d: Possible\n",k);
		}
		else
		{
			printf("Case #%d: Broken\n",k);
		}
		

	}

}

        