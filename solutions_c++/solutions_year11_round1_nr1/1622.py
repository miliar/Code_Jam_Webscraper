#include <cstdio>
#include <cstdlib>
/*
n*Pd==100*x<=Pg*Total
for some 0<=n<=N
x is integer

*/
int main()
{
	freopen("A-small-attempt3.in","r",stdin);
	freopen("A-small-attempt3.out","w",stdout);
	int nT,t=0;
	scanf("%d",&nT);
	while(nT--)
	{
		int n,pg,pd;
		scanf("%d%d%d",&n,&pd,&pg);
		if((pd!=100 && pg==100) || (pd>0 && pg==0))
		{
			printf("Case #%d: Broken\n",++t);
			continue;
		}
		int today=100;
		if(pd!=0)
		{
			while((pd % 2==0) && (today % 2 ==0))
			{
				pd/=2;
				today/=2;
			}
			while((pd % 5==0) && (today % 5==0))
			{
				pd/=5;
				today/=5;
			}
		}
		else
		{
			today=1;
		}
		if(today>n)
		{
			printf("Case #%d: Broken\n",++t);
		}
		else
		{
			printf("Case #%d: Possible\n",++t);
		}
	}
}
