// poj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>

int main()
{

	int t,n,l,h;
	int a[101];
	int i,j,k;
	freopen("C-small-attempt0.in.txt","r",stdin);
	freopen("C-small.out.txt","w",stdout);
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d%d%d",&n,&l,&h);
		for(j=0;j<n;j++)
			scanf("%d",&a[j]);
		bool flag=false;
		for(k=l;k<=h;k++)
		{
			bool test=true;
			for(j=0;j<n;j++)
			{
				if(k%a[j]!=0&&a[j]%k!=0)
				{
					test=false;
					break;
				}
			}
			if(test)
			{
				flag=true;
				break;
			}
		}
		printf("Case #%d: ",i+1);
		if(flag)
		{
			printf("%d\n",k);
		}
		else
		{
			printf("NO\n");
		}

	}
}

