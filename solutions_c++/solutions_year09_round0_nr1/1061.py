/*
 * test.cpp
 *
 *  Created on: 2009-9-3
 *      Author: gao
 */

#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <cstdlib>
#include <cstring>
#include <cstdio>

using namespace std;

vector<set<char> > vsc;

void generate(string word)
{
	vsc.clear();
	set<char> sc;
	sc.clear();
	bool found = false;
	for (int i = 0; i < word.size(); i++)
	{
		if (word[i] == '(')
		{
			found = true;
		}
		else if (word[i] == ')')
		{
			vsc.push_back(sc);
			sc.clear();
			found = false;
		}
		else
		{
			if (!found)
			{
				sc.insert(word[i]);
				vsc.push_back(sc);
				sc.clear();
			}
			else
			{
				sc.insert(word[i]);
			}
		}
	}
}

bool ok(string word)
{
	for (int i = 0; i < word.size(); i++)
	{
		if (!vsc[i].count(word[i]))
			return false;
	}
	return true;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	vector<string> vs;
	string temp;
	string word;

	int L, D, N;
	cin>>L>>D>>N;
	int i, j, l;
	for (i = 0; i < D; i++)
	{
		cin>>temp;
		vs.push_back(temp);
	}
	for (int k = 1; k <= N; k++)
	{
		cin>>word;
		generate(word);
		int count = 0;
		for (i = 0; i < D; i++)
		{
			if (ok(vs[i]))
				count++;
		}
		printf ("Case #%d: %d\n", k, count);
	}
	return 0;
}


