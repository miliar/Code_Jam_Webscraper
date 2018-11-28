// cj1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int _tmain(int argc, _TCHAR* argv[])
{
	int c;
	scanf("%d", &c);
	for (int cc = 1; cc <= c; cc++)
	{
		unsigned n, k;
		scanf("%u %u", &n, &k);
		k %= (1<<n);
		if (k == (1<<n)-1)
			printf("Case #%d: ON\n", cc);
		else
			printf("Case #%d: OFF\n", cc);
	}
	return 0;
}

