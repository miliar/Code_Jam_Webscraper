// qA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "algorithm"
#include "cstdio"

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	int t;

	scanf("%d",&t);
	for (int zz = 1; zz <= t; zz++)
	{
		printf("Case #%d: ",zz);

		int cnt = 0;
		int n,k;
		
		scanf("%d%d",&n,&k);
		
		for (int i = 0; i < n; i++)
		{
			if (k & (1 << i))
				cnt++;
		}

		if (cnt == n)
			printf("ON\n");
		else
			printf("OFF\n");
	}	

	return 0;
}

