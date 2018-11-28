// q.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <iostream>
#include <set>
#include <queue>

using namespace std;


vector<pair<bool, int>> a;

bool reached(int cur, int& pos) {
	if (pos>cur) --pos; else if (pos<cur) ++pos; else return true;
	return false;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	vector<int> or, bl;
	int io = 0, ib = 0;
	int cur_o = 1, cur_b = 1;
	int t;
	cin >> t;	
	for (int test = 1; test <= t; ++test) 
	{
		int n;
		cin >> n;
		int res = 0;
		a.clear(); or.clear(); bl.clear();
		cur_o = cur_b = 1;
		io = ib = 0;
		for (int i = 0; i < n; ++i) 
		{
			a.push_back(make_pair(true, 0));
			char c;	cin >> c >> a[i].second;
			a[i].first = c=='O';
			if (a[i].first)	or.push_back(a[i].second); else bl.push_back(a[i].second);
		}
		for (int k = 0; k < n; ++k) 
		{
			if (a[k].first) 
			{
				if (ib < bl.size())	reached(bl[ib], cur_b);
				++res;
				while (!reached(a[k].second, cur_o)) 
				{
					if (ib < bl.size())	reached(bl[ib], cur_b);
					++res;
				}
				++io;
			} 
			else 
			{
				if (io < or.size())	reached(or[io], cur_o);
				++res;
				while (!reached(a[k].second, cur_b)) 
				{
					if (io < or.size())
						reached(or[io], cur_o);
					++res;
				}
				++ib;
			}
		}		
		cout << "Case #" << test << ": " << res << endl;
	}
	return 0;
}