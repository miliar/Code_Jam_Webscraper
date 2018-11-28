#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int L, D, N;

vector<string> word;
string s;

bool match(string w, string p)
{
	char ch;
	istringstream is(p);
	string token;
	for (int i = 0; i < w.size(); i++)
	{
		if (is.peek() == '(')
			getline(is, token, ')');
		else
		{
			token = "0";
			is >> ch;
			token[0] = ch;
		}
		if (token.find(w[i]) == string::npos)
			return false;
	}
	return true;
}

int main()
{
	scanf("%d %d %d", &L, &D, &N);
	for (int i = 0; i < D; i++)
	{
		cin >> s;
		word.push_back(s);
	}
	for (int t_case = 1; t_case <= N; t_case++)
	{
		cin >> s;
		int res = 0;
		for (int i = 0; i < word.size(); i++)
			if (match(word[i], s)) res++;
		printf("Case #%d: %d\n", t_case, res);
	}
	return 0;
}
