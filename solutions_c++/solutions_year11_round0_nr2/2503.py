#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory.h>
#include <deque>
#include <cstdio>
#include <map>
#include <string>

using namespace std;

int main()
{
	int test;
	freopen("input.txt", "rt", stdin);
	freopen("ouput.txt", "wt", stdout);
	scanf("%d", &test);
	for (int t = 0; t < test; t++)
	{
		int c;
		scanf("%d", &c);
		map<pair<char, char>, char> m;
		char buff[200];
		for (int i = 0; i < c; i++)
		{
			scanf("%s", buff);
			m[make_pair(buff[0], buff[1])] = buff[2];
			m[make_pair(buff[1], buff[0])] = buff[2];
		}

		scanf("%d", &c);
		vector<string> vs;
		for (int i = 0; i < c; i++)
		{
			scanf("%s", buff);
			vs.push_back((string)buff);
		}
		int q[26];
		memset(q, 0, sizeof(q));
		char xuy[200];
		scanf("%d", &c);
		scanf("%s", buff);
		int sz = 0;
		for (int i = 0; i < (int)strlen(buff); i++)
		{
			q[buff[i] - 'A']++;
			xuy[sz] = buff[i];
			++sz;
			while (sz > 1 && m.count(make_pair(xuy[sz - 2], xuy[sz - 1])) != 0)
			{
				q[xuy[sz - 1] - 'A']--;
				q[xuy[sz - 2] - 'A']--;
				char cc = m[make_pair(xuy[sz - 1], xuy[sz - 2])];
				xuy[sz - 2] = cc;
				q[xuy[sz - 2] - 'A']++;
				--sz;
			}
			bool ok = false;
			for (int j = 0; j < vs.size(); j++)
			{
				if (q[vs[j][0] - 'A'] > 0 && q[vs[j][1] - 'A'] > 0)
				{
					ok = true;
				}
				continue;
			}
			if (ok)
			{
				sz = 0;
				memset(q, 0, sizeof(q));
			}
		}
		xuy[sz] = '\0';
		cout << "Case #" << t + 1 << ": [";
		for (int i = 0; i < sz; i++)
		{
			cout << xuy[i];
			if (i < sz - 1)
				cout << ", ";

		}
		cout << "]";

		cout << endl;
	}
  return 0;
}
