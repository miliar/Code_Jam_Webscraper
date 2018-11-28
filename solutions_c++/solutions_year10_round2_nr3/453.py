// C_r2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
using namespace std;

int res[505];
int subset[505][505];

int _tmain(int argc, _TCHAR* argv[])
{
	void init();

	freopen("C.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	init();

	int t;
	cin>>t;
	int tmp;

	for(int i = 0;i<t;i++)
	{
		cin >> tmp;
		printf("Case #%d: %d\n", i + 1, res[tmp]);		
	}
	return 0;
}
 
__int64 C(int b, int c)
{
	if(c < 0)
		return 0;
	else if(c == 0)
		return 1;

	if(c > b)
		return 0;

	int start, end;
	start = 1;
	end = b;

	if( c > b - c)
		c = b- c;

	__int64 res = 1;

	for(int i = 0;i<c;i++)
	{
		res *= end;
		res /= start;

		start ++;
		end --;
	}

	return res;
}

void init()
{
	subset[2][1] = 1;

	for(int i = 3;i<=25;i++)
	{
		subset[i][1] = 1;

		for(int j = 2;j<i;j++) // For subset with length j
		{
			int total = 0;
			int k = j;
//			for(int k = 1;k<i;k++) // derive from k-th subset
//			{
				for(int l = 1;l < j;l++) // derive from length l
				{
					total += subset[k][l] * C(i - k - 1, j - 1 - l);
				}
//			}
			subset[i][j] = total;
		}
	}

	memset(res, 0, sizeof(res));
	for(int i = 2;i<=25;i++)
	{
		for(int j = 1;j<i;j++)
		{
			res[i] += subset[i][j];
			res[i] %= 100003;
		}
	}
}
