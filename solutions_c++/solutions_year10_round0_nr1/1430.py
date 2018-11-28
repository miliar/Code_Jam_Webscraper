#include "stdafx.h"

#include <cstdio>
#include <cctype>
#include <cstring>
#include <vector>
#include <string>

typedef unsigned int UINT ;
using namespace std;

UINT sum;
UINT groupSize[2000];
UINT indexToMoney[2000];
UINT indexToIndex[2000];
UINT history[2000];

UINT _tmain(UINT argc, _TCHAR* argv[])
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	UINT i, j, tc;
	scanf("%u",&tc);

	

	UINT k,n;
	for (i=0; i<tc; i++)
	{
		scanf("%u%u",&n,&k);

		UINT mod = 1<<n;
		
		if ((k % mod) == mod -1)
			printf("Case #%u: %s\n", i+1, "ON");
		else
			printf("Case #%u: %s\n", i+1, "OFF");


	}

	return 0;
}

