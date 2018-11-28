#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <cstdio>

using namespace std;
const int MAX = 20;

bool exist[MAX][200];
vector<string> word;

int build_partten(string partten)
{
	memset(exist, false, sizeof(exist));
	bool in_bracket = false;
	int cnt = -1;
	for(int i = 0; i < partten.length(); i++)
	{
		if(!in_bracket)
		{
			if(partten[i] == '(')
				cnt++, in_bracket = true;
			else
				exist[++cnt][partten[i]] = true;
		}
		else
		{
			if(partten[i] == ')')
				in_bracket = false;
			else
				exist[cnt][partten[i]] = true;
		}
	}
	return cnt + 1;
}

bool check(string str)
{
	for(int i = 0; i < str.length(); i++)
		if(!exist[i][str[i]]) return false;
	return true;
}

int match(int len)
{
	int cnt = 0;
	if(len != word[0].size()) return 0;
	for(int i = 0; i < word.size(); i++)
		if(check(word[i])) cnt++;
	return cnt;
}
int main()
{
	int n, d, k;
	freopen("Download A-large.in", "r", stdin);
	freopen("Download A-large.out", "w", stdout);
	cin >> n >> d >> k;
	for(int i = 0; i < d; i++)
	{
		string tmp;
		cin >> tmp;
		word.push_back(tmp);
	}
	for(int i = 1; i <= k; i++)
	{
		string partten;
		cin >> partten;
		int len;
		len = build_partten(partten);
		cout << "Case #" << i << ": " << match(len) << endl;
	}
	return 0;
}