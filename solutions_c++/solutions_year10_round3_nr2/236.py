// 123.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <sstream>
#define MAX 128
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("B-large.in", "rt", stdin);
	freopen("large.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		unsigned long long L,P,C,sum=0,i;
		unsigned long long x=1;
		scanf("%lld%lld%lld",&L,&P,&C);
		//printf("%lld %lld %lld ",L,P,C);
		if (L*C >= P)
		{
			printf("Case #%d: 0\n",it);
			continue;
		}
		for (i=0;L<P;++i)
		{
			L *= C;
		}

		for (sum=0;x<i;sum++,x*=2)
		{

		}
		printf("Case #%d: %lld\n",it,sum);
		//	printf("Case #%d: %d\n",it,sum);
	}
	return 0;
}

