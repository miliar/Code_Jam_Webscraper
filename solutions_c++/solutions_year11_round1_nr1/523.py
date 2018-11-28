#include <stdio.h>
int gcd(int a,int b)
{
	return b? gcd(b,a%b):a; 
}
int main ()
{
	int cas,i,ca;
	int a,b;
	__int64 n;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cas);
	for(ca=1;ca<=cas;ca++)
	{
		scanf("%I64d",&n);
		scanf("%d%d",&a,&b);
		if(b==100)
		{
			if(a!=100)
			{
				printf("Case #%d: Broken\n",ca);
			}
			else
			{
				printf("Case #%d: Possible\n",ca);
			}
			continue;
		}
		if(b==0)
		{
			if(a!=0)
				printf("Case #%d: Broken\n",ca);
			else
			{
				printf("Case #%d: Possible\n",ca);
			}
			continue;
		}
		if(a==0)
		{
			printf("Case #%d: Possible\n",ca);
			continue;	
		}
		int GCD=gcd(a,100);
		if(100/GCD<=n)
		{
			printf("Case #%d: Possible\n",ca);
		}
		else
		{
			printf("Case #%d: Broken\n",ca);
		}
		

	}

}