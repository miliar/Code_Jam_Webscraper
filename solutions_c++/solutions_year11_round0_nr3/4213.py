// hj.cpp : Defines the entry point for the console application.
//

#include "StdAfx.h"
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int compare(const void *a,const void *b)
{
    return *(int*)a - *(int*)b; //if return *(int*b) - *(int*a) ,then the array will be sortted in decreasing order
}

int main(int argc, char* argv[])
{
	freopen("111.in","r",stdin);
	freopen("111.out","w",stdout);
	int i,j,n;
	int a[1000];
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		int m,b=0,c=0;
		scanf("%d",&m);
		for(j=0;j<m;j++)
		{
			scanf("%d",&a[j]);
		}
		for(j=0;j<m;j++)
		{
			b=b^a[j];	
		}
		if(0!=b)
		{
			printf("Case #%d: NO\n",i+1);	
		}
		else
		{
			qsort(a,m,sizeof(int),compare);
			for(j=1;j<m;j++)
			{
				c=c+a[j];
			}
			printf("Case #%d: %d\n",i+1,c);
		}

	}
	return 0;
}
