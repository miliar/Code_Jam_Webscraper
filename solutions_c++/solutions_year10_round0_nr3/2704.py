// testcpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "windows.h"


#include "stdio.h"
#include "stdlib.h"
#include "signal.h"
#include "process.h"
#include "malloc.h"

#include "fstream"
#include "list"
#include "vector"
#include "algorithm"
#include "time.h"

#include "queue"
#include "stack"

using namespace std;


typedef unsigned __int64 uint64;

unsigned int grp[1001];

inline int nextJ(int j, int n)
{
	if ( j==n)
	{
		return 1;
	}
	else
	{
		return j+1;
	}
}

int main()
{


	int T;
	cin >> T;

	unsigned int R, K, N;

	uint64 OUTP1 = 0;

	int t = 1;
	for (t = 1; t <= T; ++t)
	{
		OUTP1 = 0;
		cin >> R >> K >> N;
		for (int i = 1; i <= N; ++i)
			cin>> grp[i];

		int cur = 1;

		while (R--)
		{
			unsigned int tmp = grp[cur];
			unsigned int cnt = 1;
			while (tmp + grp[nextJ(cur, N)] <= K && cnt < N)
			{
				cur = nextJ(cur,N);
				tmp += grp[cur];
				++cnt;
			}
			cur = nextJ(cur, N);
			OUTP1 += tmp;
		}

		cout << "Case #"<< t << ": " << OUTP1;
		if (t < T)cout << endl;

	}

	return 0;
}


