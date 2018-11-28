// ProbA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>

using namespace std;

void solve()
{
	char buf[1024];
	int T;
	cin >> T;
	cin.getline(buf, 1024);
	for (int t=0;t<T;t++)
	{
		string s;
		cin.getline(buf, 1024);
		s = buf;
		//int num = atoi(buf);
		int sz = s.length();
		vector<int> dt;
		for (int i=0;i<sz;i++)
			dt.push_back(s[i]-'0');
		next_permutation(dt.begin(), dt.end());
		stringstream ss;
		for (int i=0;i<sz;i++)
			ss << (char)('0'+dt[i]);
		if (ss.str()>s)
		{
			cout << "Case #" << (t+1) << ": " << ss.str() << endl;
		}
		else
		{
			dt.push_back(0);
			sort(dt.begin(), dt.end());
			int idx = 0;
			while (dt[idx]==0)
			{
				idx++;
			}
			swap(dt[0], dt[idx]);
			stringstream ss2;
			for (int i=0;i<sz+1;i++)
				ss2 << (char)('0'+dt[i]);
			cout << "Case #" << (t+1) << ": " << ss2.str() << endl;
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	solve();
	return 0;
}

