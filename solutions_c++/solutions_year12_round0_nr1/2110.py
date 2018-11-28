#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <stack>
#include <map>
using namespace std;

#define REP(i,n) for(int i=0; i < (n); i++)
#define REP2(i,s,n) for(int i=(s); i < (n); i++)

int main()
{
	string input[] = {
		"yeq",
		"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv",
		"z",
	};

	string output[] = {
		"aoz",
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up",
		"q",
	};

	char table[26] = { };
	REP(i, 5) REP(j, input[i].size())
		if (input[i][j] != ' ')
			table[input[i][j] - 'a'] = output[i][j];

	int TESTCASES; cin >> TESTCASES;
	string x; 
	getline(cin, x);
	for (int CASE = 1; CASE <= TESTCASES; CASE++)
	{
		getline(cin, x);
		REP(i, x.size())
			x[i] = x[i] == ' ' ? ' ' : table[x[i] - 'a'];

		cout << "Case #" << CASE << ": " << x << endl;

	}

	return 0;
}