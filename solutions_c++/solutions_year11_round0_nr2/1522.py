#include <stdio.h>
#include <cassert>
#include <memory.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <math.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-8;

void prepare()
{
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

int CASE;
int c, d, n;

char combine[130][130];
bool destroy[130][130];

char s[105];

bool solve()
{
	memset(combine, 0, sizeof(combine));
	memset(destroy, 0, sizeof(destroy));

	scanf("%d", &c);
	for (int i = 0; i < c; i++)
	{
		scanf("%s", s);
		combine[s[0]][s[1]] = combine[s[1]][s[0]] = s[2];
	}

	scanf("%d", &d);
	for (int i = 0; i < d; i++)
	{
		scanf("%s", s);
		destroy[s[0]][s[1]] = destroy[s[1]][s[0]] = true;
	}

	scanf("%d", &n);
	scanf("%s", s);

	string ans = "";
	ans.pb( s[0] );
	for (int i = 1; i < n; i++)
	{
		ans.pb(s[i]);

		while (ans.size() > 1)
		{
			if (combine[ ans[ans.size() - 2] ][ ans[ans.size() - 1] ] != 0)
			{
				char x = combine[ ans[ans.size() - 2] ][ ans[ans.size() - 1] ];
				ans.pop_back();
				ans.pop_back();
				ans.pb( x );
			}
			else
				break;
		}

		for (int j = 0; j < ans.size(); j++)
			for (int k = j + 1; k < ans.size(); k++)
				if (destroy[ ans[j] ][ ans[k] ])
					ans.clear();
	}

	printf("Case #%d: [", CASE++);

	for (int i = 0; i < ans.size(); i++)
	{
		if (i == 0)
			printf("%c", ans[i]);
		else
			printf(", %c", ans[i]);
	}
	
	printf("]\n");

	return false;
}

int main()
{
	prepare();
	int tn;
	CASE = 1;
	for (scanf("%d", &tn); tn; tn--)
		solve();
	return 0;
}