// A_r2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <map>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	void solve();
	freopen("A.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;

	for(int i = 0;i<t;i++)
	{
		solve();
	}

	return 0;
}

int n, m; // exist, non-exist
map <string, int> direct;

void solve()
{
	static int cas = 1;
	int mkdir(string str);

	string buf;

	cin >> n >> m;

	direct.clear();
	direct["/"] = 1;

	for(int i = 0;i<n;i++)
	{
		cin >> buf;
		mkdir(buf);
	}

	int res = 0;
	for(int i = 0;i<m;i++)
	{
		cin >> buf;
		res += mkdir(buf);
	}

	printf("Case #%d: %d\n", cas ++, res);
}

int mkdir(string str)
{
	int count = 0;

	string::size_type index = 0;
	do
	{
		index = str.find_first_of('/', index + 1);

		string tmp = str.substr(0, index );
		if(direct[str.substr(0, index)] == 0)
		{
			direct[str.substr(0, index)] = 1;
			count ++;
		}

	}
	while(index != str.npos);

	return count;
}