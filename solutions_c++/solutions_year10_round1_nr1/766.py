// CodeJam2010_r1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int t, k, n;
char mp[55][55];

void solve();

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("test.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin>>t ;
	for(int i = 0;i<t;i++)
	{
		solve();
	}

	return 0;
}

void rotate(string &buf)
{
	vector<char> vec;
	vec.clear();

	for(int i = 0;i<n;i++)
	{
		if(buf[i] != '.')
			vec.push_back(buf[i]);
	}

	for(int i = 0;i<n;i++)
	{
		if( i < vec.size())
		{
			buf[n - i - 1] = vec[vec.size() - i - 1];
		}
		else
		{
			buf[n - i - 1] = '.';
		}
	}
}

void solve()
{
	static int cas = 1;

	cin >> n >> k;
	string buf;
	for(int i = 0;i<n;i++)
	{
		cin >> buf;

		rotate(buf);

		for(int j = 0;j<n;j++)
		{
			mp[i][j] = buf[j];
		}
	}

	int judge();

	int res = judge();

	printf("Case #%d: ", cas ++ );
	switch(res)
	{
	case -1:
		//RED
		//cout << "r" << endl;
		printf("Red\n");
		break;
	case 0: // Neither
		//cout << "N" << endl;
		printf("Neither\n");
		break;
	case 1: // blue
		//cout << "B" << endl;
		printf("Blue\n");
		break;
	case 2: // Both
		//cout << "Both" << endl;
		printf("Both\n");
		break;
	}
}

int judge()
{
	int res = 0;

	int judgeLocation(int x, int y);

	for(int i = 0;i<n;i++)
	{
		for(int j = 0;j<n;j++)
		{
			if(res != -1 && mp[i][j] == 'R' && judgeLocation(i, j))
			{
				if(res == 1)
				{
					return 2;
				}
				else
					res = -1;
			}
			else if(res != 1 && mp[i][j] == 'B' && judgeLocation(i, j))
			{
				if(res == -1)
				{
					return 2;
				}
				else
					res = 1;
			}

		}
	}

	return res;
}

int judgeLocation(int x, int y)
{
	int countDirect(int x, int y, int d1, int d2);
	if(countDirect(x, y, 0, 1) + countDirect(x, y, 0, -1) + 1 >= k)
	{
		return 1;
	}
	else if(countDirect(x, y, 1, 0) + countDirect(x, y, -1, 0) + 1 >= k)
	{
		return 1;
	}
	else if(countDirect(x, y, 1, 1) + countDirect(x, y, -1, -1) + 1 >=k)
	{
		return 1;
	}
	else if(countDirect(x, y, 1, -1) + countDirect(x, y, -1, 1) + 1 >= k)
	{
		return 1;
	}
	else 
		return 0;
}

int countDirect(int x, int y, int d1, int d2)
{
	int x1, y1;
	for(int i = 1;i<k;i++)
	{
		x1 = x + d1 * i;
		y1 = y + d2 * i;

		if(x1 < 0 || x1 >= n || y1 < 0 || y1 >=n)
		{
			return i - 1;
		}
		if(mp[x1][y1] != mp[x][y])
		{
			return i - 1;
		}
	}
}