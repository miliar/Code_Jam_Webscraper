#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <utility>
#include <cmath>
#include <string>
using namespace std;

vector<struct Combine> combineRules;
vector<pair<char, char> > opposeRules;

struct Combine
{
	char x;
	char y;
	char c;

	Combine(char xx, char yy, char cc) :
		x(xx), y(yy), c(cc) 
	{
	}
};

char combine(char x, char y)
{
	for (int i=0; i<combineRules.size(); i++)
	{
		if ((x == combineRules[i].x && y == combineRules[i].y) || (x == combineRules[i].y && y == combineRules[i].x))
			return combineRules[i].c;
	}
	return ' ';
}

bool oppose(vector<char>& r)
{
	char last = r[r.size()-1];
	for (int i=0; i<r.size()-1; i++)
	{
		char c = r[i];
		for (int j=0; j<opposeRules.size(); j++)
		{
			if ((last == opposeRules[j].first && c == opposeRules[j].second) || (last == opposeRules[j].second && c == opposeRules[j].first))
			{
				return true;
			}
		}
	}
	return false;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t=0; t<T; t++)
	{
		//TODO: implement your algorithm here
		combineRules.clear();
		opposeRules.clear();

		int n;
		cin >> n;
		for (int i=0; i<n; i++)
		{
			string s;
			cin >> s;
			combineRules.push_back(Combine(s[0], s[1], s[2]));
		}
		cin >> n;
		for (int i=0; i<n; i++)
		{
			string s;
			cin >> s;
			opposeRules.push_back(make_pair(s[0], s[1]));
		}

		cin >> n;
		string s;
		cin >> s;
		vector<char> res;
		for (int i=0; i<n; i++)
		{
			res.push_back(s[i]);
			here:int sz = res.size();
			if (sz >= 2)
			{
				char c = combine(res[sz-1], res[sz-2]);
				if (c != ' ')
				{
					res.pop_back();
					res.pop_back();
					res.push_back(c);
					goto here;
				}
				else
				{
					if (oppose(res))
					{
						res.clear();
					}
				}
			}
		}

		printf("Case #%d: [", t+1);
		if (res.empty())
			printf("]\n");
		else
		{
			printf("%c", res[0]);
			for (int i=1; i<res.size(); i++)
				printf(", %c", res[i]);
			printf("]\n");
		}
	}
}