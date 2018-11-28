//Made by diver_ru, made with love^^
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <iostream>
#include <memory.h>
#include <fstream>

std::string NAME = "test";
using namespace std;

typedef long long int64;

int N, M;

int res;

set<string> was;

void addDir(string &s)
{
	int d = (int)was.size();
	for (int i = 1; i < (int)s.size(); ++i)
	{
		if (s[i] == '/')
			was.insert(s.substr(0, i));
	}
	was.insert(s);
	res += (was.size() - d);
}

int main()
{
	if (!NAME.empty())
	{
		freopen((NAME+".in").c_str(), "r", stdin);
		freopen((NAME+".out").c_str(), "w", stdout);
	}
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		was.clear();
		cin >> N >> M;
		string s;
		getline(cin, s);
		for (int j = 0; j < N; ++j)
		{
			getline(cin, s);
			addDir(s);
		}
		res = 0;
		for (int j = 0; j < M; ++j)
		{
			getline(cin, s);
			addDir(s);
		}

		cout << "Case #" << i << ": " << res << endl;
	}

	return 0;
}