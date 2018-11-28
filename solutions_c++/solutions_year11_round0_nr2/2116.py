#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

char table[256][256];
bool conflict[256][256];

int main(int paramc, char ** params)
{
	if (paramc > 1)
		freopen(params[1], "r", stdin);
	int t;
	cin >> t;
	for (int T = 0; T < t; ++T)
	{
		memset(table, 0, sizeof(table));
		memset(conflict, 0, sizeof(conflict));
		int n;
		cin >> n;
		string s, t;
		for (int i = 0; i < n; ++i)
			cin >> s, table[s[0]][s[1]] = table[s[1]][s[0]] = s[2];
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> s, conflict[s[0]][s[1]] = conflict[s[1]][s[0]] = 1;
		cin >> n;
		cin >> s;
		for (int i = 0; i < n; ++i)
			if (t.size() != 0 && table[s[i]][t[t.size() - 1]] != 0)
				t[t.size() - 1] = table[s[i]][t[t.size() - 1]];
			else
			{
				for (int j = 0; j < t.size(); ++j)
					if (conflict[t[j]][s[i]])
					{
						t = "";
						goto next;
					}
				t += s[i];
next:;
			}
		s = "[";
		for (int i = 0; i < t.size(); ++i)
		{
			if (i != 0)
				s += ", ";
			s += t[i];
		}
		s += "]";
		printf("Case #%d: %s\n", T + 1, s.c_str());
	}
	return 0;
}
