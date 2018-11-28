// codejam3.cpp : main project file.

//#include "stdafx.h"
#include<iostream>
#include<stdio.h>
#include<cmath>
using namespace std;
long long count;
int a,b;
void funct()
{
	int i,j,k;
	for(i=a;i<=b;i++)
	{
		int temp=i,digits=0;
		while(temp>0)
		{
			digits++;
			temp/=10;
		}
		temp=i;
		for(j=0;j<digits-1;j++)
		{
			int d=temp%10;
			temp/=10;
			if(d==0)
				continue;
			temp+=d*(int)pow(10,(double)digits-1);
				if(temp<i&&temp<=b&&temp>=a)
					count++;
			
		}
	}
}
int main()
{
	int tests;
	scanf("%d",&tests);
	for(int l=1;l<=tests;l++)
	{
		count=0;
		
		scanf("%d%d",&a,&b);
		funct();
		printf("Case #%d: %lld\n",l,count);
	}
    return 0;
}
