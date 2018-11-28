// codejam09.cpp : Defines the entry point for the console application.
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

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)

VS getWordList(string str)
{
	VS vec;
	bool isin = false;
	string word = "";
	for (int i = 0; i < str.length(); i++)
	{
		if (str[i] == '(')
		{
			word = "";
			isin = true;
			continue;
		}
		if (str[i] == ')')
		{
			vec.push_back(word);
			word = "";
			isin = false;
			continue;
		}
		if (isin)
			word += str[i];
		else
		{
			word = str[i];
			vec.push_back(word);
		}
	}
	return vec;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int L,D,N;
	cin >> L >> D >> N;
	VS words;
	for (int i = 0; i < D; i++)
	{
		string temp;
		cin >> temp;
		words.push_back(temp);
	}

	for (int i = 0; i < N; i++)
	{
		string temp;
		cin >> temp;
		VS vec = getWordList(temp);
		int cnt = 0;
		for (int i = 0; i < words.size(); i++)
		{
			bool hasword = true;
			string word = words[i];
			for (int j = 0; j < L; j++)
			{
				if (vec[j].count(word[j]) == 0)
					hasword = false;
			}
			if (hasword)
				cnt++;
		}
		cout << "Case #" << i + 1 << ": " << cnt << endl;
	}
	
	return 0;
}

