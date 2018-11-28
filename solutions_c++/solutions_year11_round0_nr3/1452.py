// Candy.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int i=0;i<T;i++)
	{
		int N;
		cin >> N;

		int nXor = 0;
		int nMin = 1000001;
		unsigned long long ullSum = 0;
		for(int j=0;j<N;j++)
		{
			int t;
			cin >> t;
			if (t<nMin)
				nMin = t;
			nXor ^= t;
			ullSum += t;
		}

		ullSum -= nMin;

		if (nXor)
			printf("Case #%d: NO\n", i+1);
		else
			printf("Case #%d: %I64u\n", i+1, ullSum);
		
	}

	return 0;
}

