// B_r2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
using namespace std;

int locat[55];
int speed[55];

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("B.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	void solve();
	int c;
	cin >> c;
	for(int i = 0;i<c;i++)
	{
		solve();
	}
	return 0;
}

int n, k, b, t;

void solve()
{
	static int cas = 1;
	cin >> n >> k >> b >> t;

	for(int i = 0;i<n;i++)
	{
		cin >> locat[i];
	}
	for(int i = 0;i<n;i++)
	{
		cin >> speed[i];
	}

	int count = 0;
	int res = 0;

	for(int i = n - 1;i>=0;i--)
	{
		if(1.0 * (b - locat[i]) / speed[i] <= t)
		{
			count ++;
			res += (n - i - count);
		}

		if(count >= k)
			break;
	}

	if(count >=k)
	{
		printf("Case #%d: %d\n", cas ++, res);
	}
	else
	{
		printf("Case #%d: IMPOSSIBLE\n", cas ++);
	}
}