#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

vector<string> buildPattern(string pattern)
{
	vector<string> alphabet;
	bool inParen = false;
	string group;
	for (int i = 0;i < pattern.size();i++)
	{
		if (pattern[i] == '(')
			inParen = true;
		else if (pattern[i] == ')')
		{
			alphabet.push_back(group);
			group.clear();
			inParen = false;
		}
		else if (!inParen)
		{
			alphabet.push_back(string(1,pattern[i]));
		}
		else
		{
			group += pattern[i];
		}
	}
	return alphabet;
}

inline bool match(string word,vector<string> alphabet)
{
	for (int j = 0;j < word.size();j++)
	{
		if (alphabet[j].find(word[j]) == string::npos)
			return false;
	}
	return true;
}

int main()
{
	ifstream fin("A-small-attempt0.in");
	ofstream fout("out.txt");

	vector<string> words;
	int l,d,n;
	fin >> l >> d >> n;
	for (int i = 0;i < d;i++)
	{
		string temp;
		fin >> temp;
		words.push_back(temp);
	}
	for (int j = 0;j < n;j++)
	{
		string pattern;
		fin >> pattern;
		int count = 0;
		for (int i = 0;i < d;i++)
		{
			vector<string> alphabet = buildPattern(pattern);
			if (match(words[i],alphabet))
				count++;
		}
		fout << "Case #" << j+1 << ": " << count << endl;
	}
}