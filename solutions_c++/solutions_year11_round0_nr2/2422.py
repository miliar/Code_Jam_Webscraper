#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
using namespace std;

int mabs(int num)
{
	return num > 0? num: -num;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	//scanf("%d", &t);
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		int c, d;
		cin >> c;
		string s;
		map< pair<char, char>, char> m;
		set< pair<char, char> > opp;
		for(int i = 0; i < c; i++)
		{
			cin >> s;
			m[make_pair(s[0], s[1])] = s[2];
			m[make_pair(s[1], s[0])] = s[2];
		}
		cin >> d;
		for(int i = 0; i < d; i++)
		{
			cin >> s;
			opp.insert(make_pair(s[0], s[1]));
			opp.insert(make_pair(s[1], s[0]));
		}
		int n;
		cin >> n;
		cin >> s;
		vector<char> res;
		bool f = false;
		for(int i = 0; i < (int)s.size(); i++)
		{
			if(res.size() == 0)
				res.push_back(s[i]);
			else if(m.find(make_pair(s[i], res[res.size() - 1])) != m.end())
			{
				char tmp = m[make_pair(s[i], res[res.size() - 1])];
				res.pop_back();
				res.push_back(tmp);
			}
			else
			{
				f = false;
				for(int j = 0; j < (int)res.size(); j++)
				{
					if(opp.find(make_pair(s[i], res[j])) != opp.end())
					{
						res.clear();
						f = true;
						break;
					}
				}
				if(!f)
					res.push_back(s[i]);
			}
		}
		cout << "Case #" << test << ": [";
		for(int i = 0; i < (int)res.size(); i++)
		{
			if(i != 0)
				printf(", ");
			cout << res[i];
		}
		printf("]\n");
	}
	return 0;
}