// Codejam2010.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
using namespace std;

int judgeOn(int n, int k);

int _tmain(int argc, _TCHAR* argv[])
{
	int t, n, k;

	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin>>t;
	
	for(int i = 0;i<t;i++)
	{
		cin >> n >> k;
		if(judgeOn(n, k))
		{
			printf("Case #%d: ON\n", i+1);
		}
		else
		{
			printf("Case #%d: OFF\n", i+1);
		}
	}

	return 0;
}

int judgeOn(int n, int k)
{
	for(int i = 0;i<n;i++)
	{
		if((k & (1 << i)) == 0)
			return 0;
	}

	return 1;
}