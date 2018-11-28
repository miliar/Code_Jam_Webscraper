#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
using namespace std;

int trie[6553600][26];
int top;
void insert(const char* str)
{
	int curr = 0;
	for (int i = 0; str[i]; ++i)
	{
		int next = str[i] - 'a';
		if (trie[curr][next] == 0)
		{
			trie[curr][next] = top++;
		}
		curr = trie[curr][next];
	}
}

int result;
map<string, int> searched;
void search(string text, int curr, int state, string ans)
{
	if (!text[curr])
	{
		if (searched.find(ans) == searched.end()) ++result;
		++searched[ans];
	}
	else
	{
		if (text[curr] == '(')
		{
			int end;
			for (end = ++curr; text[end] != ')'; ++end);
			++end;
			for (; text[curr] != ')'; ++curr)
			{
				int next = trie[state][text[curr]-'a'];
				if (next) search(text, end, next, ans + text[curr]);
			}
		}
		else
		{
			int next = trie[state][text[curr]-'a'];
			if (next)
			search(text, curr+1, next, ans + text[curr]);
		}
	}
}
int main()
{
	freopen("A-large.in", "r", stdin);freopen("Download A-small.out", "w", stdout);
	//freopen("Download A-large.in", "r", stdin);freopen("Download A-large.out", "w", stdout);
	int l, d, n;
	while (scanf("%d%d%d", &l, &d, &n) == 3)
	{
		string str;
		memset(trie, 0, sizeof(trie));top = 1;
		for (int i = 0; i < d; ++i)
		{
			cin>>str;insert(str.c_str());
		}
		for (int caseid = 1; caseid <= n; ++caseid)
		{
			cin >> str;
			searched.clear();
			result = 0;
			search(str, 0, 0, "");
			printf("Case #%d: %d\n", caseid, result);
		}
	}
	return 0;
}
