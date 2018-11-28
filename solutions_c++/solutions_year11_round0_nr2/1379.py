#include <cstdio>
#include <vector>
#include <utility>
#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <limits.h>
#include <time.h>
#include <iomanip>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <list>
#include <stack>
using namespace std;
typedef int LL;


string Solve()
{
	map<pair<char, char>, char> comb;
	int c;
	cin >> c;
	for (int i = 0; i < c; i++)
	{
		string str;
		str.resize(3);
		//getline(cin , str);
		cin >> str[0] >> str[1] >> str[2];
		comb[make_pair(str[0], str[1])] = str[2];
		comb[make_pair(str[1], str[0])] = str[2];
	}
	map<char, vector<char>> opp;
	int d;
	cin >> d;
	for (int i = 0; i < d; i++)
	{
		string str;
		str.resize(2);
		//getline(cin , str);
		cin >> str[0] >> str[1];
		opp[str[0]].push_back(str[1]);
		opp[str[1]].push_back(str[0]);
	}

	//stack<char> panel;
	vector<int> panel;
	panel.resize(110);
	int psize = 0;
	multiset<char> elems;


	int n;
	cin >> n;
	string str;
	cin >> str;
	for (int i = 0; i < n; i++)
	{
		if (psize == 0)
		{
			panel[0] = str[i];
			psize++;
			elems.insert(str[i]);
		}
		else
		{
			if (comb.find(make_pair(panel[psize-1], str[i])) != comb.end())
			{
				char x = comb[make_pair(panel[psize-1], str[i])];
				int ct = elems.count(panel[psize-1]);
					elems.erase(panel[psize-1]);
				if (ct > 1)
					for (int i = 0; i < ct - 1; i++)
						elems.insert(panel[psize-1]);
				panel[psize-1] = x;
				elems.insert(x);
			}
			else
			{
				bool boom = false;
				for (int j = 0; j < opp[str[i]].size(); j++)
				{
					if (elems.find(opp[str[i]][j]) != elems.end())
					{
						boom = true;
						break;
					}
				}
				if (boom)
				{
					elems.clear();
					psize = 0;
				}
				else
				{
					panel[psize] = str[i];
					psize++;
					elems.insert(str[i]);
				}
			}
		}
	}

	string res;
	res.push_back('[');
	if (psize > 0)
	{
		for (int i = 0; i < psize - 1; i++)
		{
			res.push_back(panel[i]);
			res.push_back(',');
			res.push_back(' ');
		}
		res.push_back(panel[psize - 1]);
	}
	res.push_back(']');
	return res;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	cin >> t; 
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i+1 << ": " << Solve() << endl;
	}

	return 0;
}