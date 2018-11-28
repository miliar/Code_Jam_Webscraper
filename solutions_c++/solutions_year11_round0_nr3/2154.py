// 1.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"

#include <algorithm>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	scanf("%d", &t);
	for (int k = 1; k <= t; k++)
	{
		int n;
		scanf("%d", &n);
		unsigned v[1024], r = 0, q = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%u", &v[i]);
			r ^= v[i];
			q += v[i];
		}
		
		printf("Case #%d: ", k);
		if (r != 0)
		{
			printf("NO\n");
		}
		else
		{
			printf("%u\n", q-*min_element(v, v+n));
		}
		
	}
	return 0;
}

