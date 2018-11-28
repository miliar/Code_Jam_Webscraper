// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

map<string, int> mp;

const int N = 50;
string row[N];
int order[N];
int index[N];

int getLast(string str)
{
	for(int i = str.length() - 1; i>=0;i--)
	{
		if(str[i] == '1')
			return i;
	}

	return 0;

}


int findNear(int r, int n)
{
	for(int i = r;i<n;i++)
	{
		if(getLast(row[index[i]]) <= r)
			return i;
	}

	return -1;
}


int cmp(const string &a, const string &b)
{
	return getLast(a) < getLast(b);
}

int move(int r, int n)
{
	int tmp = findNear(r, n);

	for(int i = tmp;i>r;i--)
	{
		int swap;
		swap = index[i];
		index[i] = index[i-1];
		index[i-1] = swap;
	}
/*
	for(int i = 0;i<n;i++)
	{
		cout << row[index[i]] << endl;
	}
	cout << "Moved: " << tmp - r << endl;*/
	return tmp - r;
}

void solve()
{
	static int cas = 1;
	mp.clear();
	int n;
	cin>> n;
	for(int i = 0;i<n;i++)
	{
		cin>> row[i];
		///mp[row[i]] = i;
		index[i] = i;
	}

	int ans = 0;

	for(int i = 0;i<n;i++)
	{
		if(getLast(row[index[i]]) > i)
		{

			ans += move(i, n);

		}
	}

	//cout << ans << endl;
	printf("Case #%d: %d\n", cas++, ans);
}


int _tmain(int argc, _TCHAR* argv[])
{
	freopen("data.txt", "r", stdin);
	freopen("data.out", "w", stdout);

	int t;
	cin>>t;
	for(int i = 0;i<t;i++)
	{
		solve();
	}
	return 0;
}