#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

typedef vector<string> vs;
bool guess(const vs& dict, char ch)
{
	for (int i = 0; i < dict.size(); i++)
		for (int j = 0; j < dict[i].size(); j++)
			if (dict[i][j] == ch)
				return true;
	return false;
}
int game(const vs& dict, const string& word, const string& list)
{
	int ret = 0;
	vs tdict;
	for (int i = 0; i < dict.size(); i++)
	{
		if (dict[i].size() == word.size())
			tdict.push_back(dict[i]);
	}
	for (int i = 0; i < list.size(); i++)
		if (guess(tdict, list[i]))
		{
			{
				bool flag = true;
				for (int j = 0; j < word.size(); j++)
					if (word[j] == list[i])
					{
						flag = false;
					}
				if (flag)
					ret++;
			}
			vs tmp;
			for (int j = 0; j < tdict.size(); j++)
			{
				bool flag = true;
				for (int k = 0; k < word.size(); k++)
				{
					if (word[k] == list[i] && tdict[j][k] != list[i])
					{
						flag = false;
					}
					if (word[k] != list[i] && tdict[j][k] == list[i])
					{
						flag = false;
					}
				}
				if (flag)
					tmp.push_back(tdict[j]);
			}
			tdict.swap(tmp);
		}
	return ret;
}

string calc(const vs& dict, const string& list)
{
	int ret = 0;
	int idx = 0;
	for (int i = 0; i < dict.size(); i++)
	{
		int tmp = game(dict, dict[i], list);
		if (tmp > ret)
		{
			ret = tmp;
			idx = i;
		}
	}
	return dict[idx];
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	for (int testcase = 1; testcase <= T; testcase++)
	{
		int n, m;
		cin >> n >> m;
		vs dict, list;
		for (int i = 1; i <= n; i++)
		{
			string st;
			cin >> st;
			dict.push_back(st);
		}
		for (int i = 1; i <= m; i++)
		{
			string st;
			cin >> st;
			list.push_back(st);
		}
		cout << "Case #" << testcase << ":";
		for (int i = 0; i < m; i++)
			cout << " " << calc(dict, list[i]);
		cout << endl;
	}
}