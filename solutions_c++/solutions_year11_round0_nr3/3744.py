// candy.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int nrt;

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("candy.in","r",stdin);
	freopen("candy.out","w",stdout);
	scanf("%d\n",&nrt);

	for(int x = 0;x < nrt;++x)
	{
		int n,xor = 0,curval,minim = 100000000,sum = 0;
		scanf("%d\n",&n);
		for(int i = 1;i <= n; ++i)
		{
			scanf("%d\n",&curval);
			xor ^= curval;
			if (minim > curval) minim = curval;
			sum += curval;
		}
		printf("Case #%d: ",x +1 );
		if (xor == 0) printf("%d\n",sum - minim);
			else printf("NO\n"); 
	}

	return 0;
}

