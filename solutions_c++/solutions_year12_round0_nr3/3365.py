// recycle.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>

using namespace std;

ifstream in("test.txt");
ofstream out("out.txt");

void runCase(int test)
{
	int n,m,result = 0;
	vector<pair<int,int>> r;

	in >> n >> m;

	for(int i = n; i <= m; i++)
	{
		stringstream tmp;
		tmp << i;
		string s = tmp.str();
		tmp.clear();

		for(int j = 0; j < s.length(); j++)
		{
			s = s.at(s.length() - 1) + s;
			s.erase( s.length() - 1);

			if(s.at(0) == '0')
				continue;

			int toRecycle = atoi(s.c_str());

			if(toRecycle <= m && toRecycle >= n && toRecycle > i && find(r.begin(), r.end(), make_pair(i, toRecycle)) == r.end())
			{
					r.push_back(make_pair(i, toRecycle));
					result++;
			}
		}	}	out << "Case #" << test << ": " << result << endl;}

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	in >> T;

	for(int i = 0; i < T; i++)
		runCase( i+1);

	return 0;
}

