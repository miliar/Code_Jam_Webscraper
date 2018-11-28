#include <cstdio>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int L, D, N;

bool check(string word, vector<set<char> > pattern)
{
	for (int i = 0; i < L; i++)
		if (pattern[i].find(word[i]) == pattern[i].end())
			return false;
	return true;
}

vector<set<char> > string2pattern(string str)
{
	vector<set<char> > pattern(L);
	bool compound = false;
	int j = 0;
	for (int i = 0; i < str.length(); i++)
	{
		if (str[i] == '(')
			compound = true;
		else if (str[i] == ')')
			compound = false;
		else
			pattern[j].insert(str[i]);
		if (!compound)
			j++;
	}
	return pattern;
}

int main()
{
	cin >> L >> D >> N;

	vector<string> word_list(D);
	for (int i = 0; i < D; i++)
		cin >> word_list[i];

	vector<vector<set<char> > > pattern_list(N);
	for (int i = 0; i < N; i++)
	{
		string str;
		cin >> str;
		pattern_list[i] = string2pattern(str);
	}
	
	for (int p = 0; p < N; p++)
	{
		int n = 0;
		for (int w = 0; w < D; w++)
			if (check(word_list[w], pattern_list[p]))
				n++;
		printf("Case #%d: %d\n", p+1, n);
	}
}
