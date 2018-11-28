// cj02.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include<algorithm>
using namespace std;

__int64 t[1024];

__int64 gcd(__int64 a, __int64 b)
{
	while( a != 0 )
	{
		b %= a;
		__int64 c = b;
		b = a;
		a = c;
	}
	return b;
}

int _tmain(int argc, _TCHAR* argv[])
{

	int c;
	scanf("%d", &c);
	for (int cc = 1; cc <= c; cc++)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%I64d", &t[i]);

		}
		sort(t, t+n);
		int go = 0;
		__int64 T = 1;
		for (int x = 0; x < n; x++)
		{
			for (int y = x+1; y < n; y++)
			{
				__int64 d = t[y]-t[x];
				if (d == 0) continue;
				if (go == 0) 
					go = 1, T = d;
				else 
					T = gcd(T, d);
				if (T == 1) goto END;
			}
		}
END:
		if (T == 1) 
			printf("Case #%d: 0\n", cc);
		else
		{
			printf("Case #%d: %I64d\n", cc, T*((t[0]+T-1)/T)-t[0]);
		}
	}
	return 0;
}

