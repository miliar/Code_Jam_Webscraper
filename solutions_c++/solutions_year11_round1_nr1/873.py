// poj.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <stdio.h>

int gcd(int a,int b)
{
	if(b==0)
		return a;
	else
		return gcd(b,a%b);
}
int main()
{
	long long n;
	int pd,pg;
	int md,mg;
	int t,i;
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%lld%d%d",&n,&pd,&pg);
		printf("Case #%d: ",i+1);
		if(pd>0&&pg==0)
		{
			printf("Broken\n");
			continue;
		}
		else if(pd<100&&pg==100)
		{
			printf("Broken\n");
			continue;
		}
		md=100/gcd(100,pd);
		//mg=100/gcd(100,pg);
		if(md<=n)
			printf("Possible\n");
		else
			printf("Broken\n");
	}
}

