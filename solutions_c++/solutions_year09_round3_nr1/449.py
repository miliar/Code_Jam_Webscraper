// a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <string>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)

map<char,int> maps;

int number = 0;

int getNextNum()
{
	if (number == 0)
		return 1;
	if (number == 1)
		return 0;
	return number;
}

LL getNumber(string word, int base)
{
	LL res = 0;
	for (int i = 0; i < word.size(); i++)
	{
		res *= (LL)base;
		res += (LL)maps[word[i]];
	}
	return res;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin >> t;
	int caseId = 1;
	while(t--)
	{
		number = 0;
		maps.clear();
		string word;
		cin >> word;
		for (int i = 0; i < word.size(); i++)
		{
			if (maps.count(word[i]) == 0)
			{
				maps[word[i]] = getNextNum();
				number++;
			}
		}
		
		int base = maps.size();
		if (base == 1)
			base = 2;
		LL res = getNumber(word,base);
		cout << "Case #" << caseId++ << ": " << res << endl;
	}
	return 0;
}

