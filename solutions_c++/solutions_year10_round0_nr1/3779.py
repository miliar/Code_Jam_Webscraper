// cj1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		int r,k;
		scanf("%d%d",&r,&k);
		while(k>(1<<r))k-=(1<<r);
		if(k==(1<<r)-1)printf("Case #%d: ON\n",i+1);
		else printf("Case #%d: OFF\n",i+1);
	}
	return 0;
}

