// cj3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int _tmain(int argc, _TCHAR* argv[])
{
	int c;
	scanf("%d", &c);
	for (int cc = 1; cc <= c; cc++)
	{
		int result = 0;
		int q[32], k, r, n, acc[32];
		scanf("%d %d %d", &r, &k, &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &q[i]);
		memset(acc, 0, sizeof(acc));
		int qstart = 0, rr = 0;
		while(rr < r)
		{
			int sp = 0;
			for (int i = 0; i < n; i++)
			{
				if (sp+q[qstart] > k)
					break;
				sp += q[qstart];
				result += q[qstart];
				acc[qstart]++;
				qstart = (qstart+1)%n;
			}
			rr++;
		}
		printf("Case #%d: %d\n", cc, result);
	}
	return 0;
}

