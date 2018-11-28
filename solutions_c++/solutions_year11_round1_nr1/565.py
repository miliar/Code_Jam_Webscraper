#include<iostream>
#include<stdio.h>
using namespace std;



int main()
{
	int t,p;
	scanf("%d",&t);
	for(p=1;p<=t;p++)
	{	
		long long int n;
		int pg,pd;
		scanf("%lld%d%d",&n,&pd,&pg);
		printf("Case #%d: ",p);
		if((pg==100&&pd<100)||(pg==0&&pd>0))
		{
			printf("Broken\n");
		}
		else if(n>=100)
		{
			printf("Possible\n");
		}
		else
		{
			long long int possible=100;
			if(pd%4==0)
				possible=25;
			else if(pd%2==0)
				possible=50;
			if(pd%25==0)
				possible/=25;
			else if(pd%5==0)
				possible/=5;
			if(possible<=n)
				printf("Possible\n");
			else
				printf("Broken\n");
		}
	}
	return 0;
}