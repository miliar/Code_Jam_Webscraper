// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
using namespace std;

int m[2088];

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("data.txt", "r", stdin);
	freopen("data.out", "w", stdout);

	void solve();

	int t;
	cin >> t;
	for(int i = 0;i<t;i++)
	{
		solve();
	}
	return 0;
}

int getTick(int start, int length)
{
	for(int i = start;i<start + length;i++)
	{
		if(m[i] > 0)
		{
			for(int j = start;j<start + length;j++)
			{
				m[j] --;
			}
			return 1;
		}
	}

	return 0;
}

void solve()
{
	int ans = 0;
	int p;

	cin >> p;
	for(int i = 0;i< (1<<p);i++)
	{
		cin >> m[i];
		m[i] = p - m[i];
	}

	int tmp;
	for(int i = 0;i< (1<<p) - 1 ;i++)
	{
		cin >> tmp;
	}

	for(int i = p;i>0;i--)
	{
		for(int j = 0;j< (1<<p);j+=(1 << i))
		{
			for(int k = 0;k<(1<<i);k += (1<<i))
			{
				ans += getTick(j + k, (1<<i));
			}
		}

		int flag = 0;

		for(int i = 0;i<(1<<p);i++)
		{
			if(m[i] > 0)
			{
				flag = 1;
				break;
			}
		}
		if(flag == 0)
			break;
	}

	//cout << ans << endl;
	static int cas = 1;
	printf("Case #%d: %d\n", cas ++, ans );
}