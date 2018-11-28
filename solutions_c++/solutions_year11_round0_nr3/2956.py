#include<iostream>
#include<stdio.h>
using namespace std;
int bin(int a,int b)
{
	//int i,j=__builtin_popcount(max(a,b)),c=0;
	int i,j=32,c=0;
	for(i=0;i<j;i++)
		//if(((a>>i)+(b>>i))&1)
		if((((a>>i)&1)+((b>>i)&1))&1)
			c|=(1<<i);
	return c;
}
int main()
{
	int t,i,j,k,sum,mn,asum=0,n;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d",&n);
		sum=asum=0;
		mn=10000000;
		for(i=0;i<n;i++)
		{
			scanf("%d",&j);
			sum+=j;
			mn=min(mn,j);
			asum=bin(asum,j);
		}
		printf("Case #%d: ",k);
		if(asum)
			printf("NO\n");
		else
			printf("%d\n",sum-mn);
	}
	return 0;
}
/*
2
5
1 2 3 4 5
3
3 5 6
*/
