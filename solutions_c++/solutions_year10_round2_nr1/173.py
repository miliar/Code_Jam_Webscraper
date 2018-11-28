#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <limits.h>
#include <string>

using namespace std;

typedef long long int64;

char ch[200000];

vector<vector<string>> dirs;

vector<string> process(char* c)
{
	int l = strlen(c);
	vector<string> res;
	string tmp;
	for (int i = 0; i < l; i++)
	{
		if (c[i] == '/')
		{
			if (!tmp.empty())
			{
				res.push_back(tmp);
				tmp = string();
			}
		}
		tmp.append(1, c[i]);
	}
	if (!tmp.empty())
	{
		res.push_back(tmp);
		tmp = string();
	}
	return res;
}

int check(vector<string>& p)
{
	int result = p.size();
	for (int i = 0; i < dirs.size(); i++)
	{
		int q = p.size();
		for (int j = 0; j < min(dirs[i].size(), p.size()); j++)
		{
			if (dirs[i][j] == p[j])
				--q;
			else
				break;
		}
		result = min(result, q);
	}
	return result;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	for (int test = 0; test < t; test++)
	{
		dirs.clear();
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; i++)
		{
			scanf("%s", ch);
			vector<string> p = process(ch);
			dirs.push_back(p);
		}
		int ans = 0;
		for (int i = 0; i < m; i++)
		{
			scanf("%s", ch);
			vector<string> p = process(ch);
			ans += check(p);
			dirs.push_back(p);
		}
		printf("Case #%d: %d\n", test + 1, ans);
	}
	return 0;
}