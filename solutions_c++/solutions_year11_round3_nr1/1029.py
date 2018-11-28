// poj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>

int main()
{
	int t,r,c;
	char a[51][51];
	int i,j,k,l;
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d%d",&r,&c);
		for(j=0;j<r;j++)
		{
			scanf("%s",a[j]);
		}
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				if(a[j][k]=='#'&&j+1<r&&k+1<c)
				{
					if(a[j+1][k]=='#'&&a[j][k+1]=='#'&&a[j+1][k+1]=='#')
					{
						a[j][k]=a[j+1][k+1]='/';
						a[j+1][k]=a[j][k+1]='\\';
					}
				}
			}
		}
		bool flag=true;
		for(j=0;j<r;j++)
		{
			for(k=0;k<c;k++)
			{
				if(a[j][k]=='#')
					flag=false;
			}
		}
		printf("Case #%d:\n",i+1);
		if(flag)
		{
			for(j=0;j<r;j++)
				printf("%s\n",a[j]);
		}
		else
			printf("Impossible\n");
	}
}

