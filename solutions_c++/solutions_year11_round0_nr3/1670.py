// poj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>

int main()
{
	int t,n;
	int c[1001];
	int d,s,m,i,j,k;
	freopen("C-large.in.txt","r",stdin);
	freopen("C-large.out.txt","w",stdout);
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		scanf("%d",&n);
		d=0;
		s=0;
		m=1000001;
		for(j=0;j<n;j++)
		{
			scanf("%d",&c[j]);
			d=d^c[j];
			s=s+c[j];
			if(c[j]<m)
				m=c[j];
		}
		printf("Case #%d: ",i+1);
		if(d==0)
		{
			printf("%d\n",s-m);
		}
		else
		{
			printf("NO\n");
		}
	}
	
	return 0;
}

