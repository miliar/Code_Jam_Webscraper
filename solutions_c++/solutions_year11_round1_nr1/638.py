#include<iostream>
#include<stdio.h>
using namespace std;

int gcd(int a,int b)
{
	if(b==0)return a;
	return gcd(b,a%b);
}

int main()
{
	int T,dp,gp;
	__int64 n;
	freopen("A-large.in","r",stdin);
	freopen("bb.txt","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%I64d%d%d",&n,&dp,&gp);
		if(gp==100)
		{
			if(dp<100)printf("Case #%d: Broken\n",t);
			else printf("Case #%d: Possible\n",t);
		}
		else if(gp==0)
		{
			if(dp>0)printf("Case #%d: Broken\n",t);
			else printf("Case #%d: Possible\n",t);
		}
		else if(dp==0)printf("Case #%d: Possible\n",t);
		else 
		{
			int k=gcd(dp,100);

			int p=100/k;
			if(p<=n)
			{
				printf("Case #%d: Possible\n",t);
			}
			else printf("Case #%d: Broken\n",t);
		}
	}


	return 0;
}