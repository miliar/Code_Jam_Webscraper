#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

#define INF (2000000000)

const int nmax = 1 << 7;

char triple[nmax][3];
char opposite[nmax][2];

int c, d;
string ans;

bool add(char g)
{
	if ((int)ans.length() == 0)
	{
		return false;
	}
	char last = ans[ans.length() - 1];
	for(int i = 0; i < c; ++i)
	{
		if (triple[i][0] == last && triple[i][1] == g)
		{
			ans[ans.length() - 1] = triple[i][2];
			return true;
		}
	}
	return false;
}

bool opp(char g)
{
	int lg = (int)ans.length();
	for(int i = 0; i < lg; ++i)
	{
		for(int j = 0; j < d; ++j)
		{
			if (ans[i] == opposite[j][0] && g == opposite[j][1])
			{
				ans = "";
				return true;
			}
		}
	}
	return false;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("B.in", "rt", stdin);
	freopen("B.out", "wt", stdout);
#endif
	int t;
	scanf("%d", &t);
	for(int tt = 0; tt < t; ++tt)
	{
		int n;
		scanf("%d", &c);
		int cnt = 0;
		for(int i = 0; i < c; ++i)
		{
			cin >> triple[cnt][0] >> triple[cnt][1] >> triple[cnt][2];
			++cnt;
			triple[cnt][0] = triple[cnt - 1][1];
			triple[cnt][1] = triple[cnt - 1][0];
			triple[cnt][2] = triple[cnt - 1][2];
			++cnt;
		}
		c = cnt;
		scanf("%d", &d);
		cnt = 0;
		for(int i = 0; i < d; ++i)
		{
			cin >> opposite[cnt][0] >> opposite[cnt][1];
			++cnt;
			opposite[cnt][0] = opposite[cnt - 1][1];
			opposite[cnt][1] = opposite[cnt - 1][0];
			++cnt;
		}
		d = cnt;
		scanf("%d", &n);
		string s;
		cin >> s;
		if ((int)s.length() != n)
		{
			throw -1;
		}
		ans = "";
		for(int i = 0; i < n; ++i)
		{
			if (add(s[i]))
			{
				continue;
			}
			if (opp(s[i]))
			{
				continue;
			}
			ans += s[i];
		}
		printf("Case #%d: [", tt + 1);
		int lg = (int)ans.length();
		for(int i = 0; i < lg; ++i)
		{
			printf("%c", ans[i]);
			if (i != lg - 1)
			{
				printf(", ");
			}
		}
		puts("]");
	}
	return 0;
}