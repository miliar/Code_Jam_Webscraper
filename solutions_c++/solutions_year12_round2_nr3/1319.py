// equal sums.cpp : main project file.

//#include "stdafx.h"
#include<iostream>
#include<stdio.h>
#include<cstring>
#include<map>
using namespace std;

	int arr[20];
int main()
{
	/*freopen("test.txt","r",stdin);
	freopen("op.txt","w",stdout);*/
	int tests;
	scanf("%d",&tests);
	for(int l=1;l<=tests;l++)
	{
		int num;
		scanf("%d",&num);
		map <int,int> mp;
		int i,j,k;
		for(i=0;i<num;i++)
			scanf("%d",&arr[i]);
		int limit=(1<<num);
		int a,b;
		bool flag=false;
		for(i=1;i<limit;i++)
		{
			int temp=i,sum=0;
			j=0;
			while(temp>0)
			{
				if(temp&1)
					sum+=arr[j];
				j++;
				temp>>=1;
			}
			if(mp[sum]>0)
			{
				 a=mp[sum];
				b=i;
				int c=(a&b);
				a-=c;
				b-=c;
				flag=true;
				break;
			}
			mp[sum]=i;
			
			
		}
		printf("Case #%d:\n",l);
		if(!flag)
		{
			printf("Impossible\n");
			continue;
		}
		j=0;
		while(a>0)
		{
			if(a&1)
				printf("%d ",arr[j]);
			j++;
			a>>=1;
		}
		printf("\n");
		j=0;
		while(b>0)
		{
			if(b&1)
				printf("%d ",arr[j]);
			j++;
			b>>=1;
		}
		printf("\n");
	}
    return 0;
}
