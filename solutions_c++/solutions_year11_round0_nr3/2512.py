#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
	int n,t,p,i,min,sum,xorred,num;
	
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d",&n);
		xorred=sum=0;
		min=1000000;
		for(p=0;p<n;p++)
		{
			scanf("%d",&num);
			xorred^=num;
			sum+=num;
			min=min>num?num:min;
		}
		printf("Case #%d: ",i+1);
		if(xorred==0)
		{
			printf("%d\n",sum-min);
		}
		else
			printf("NO\n");
	}
	return 0;
}