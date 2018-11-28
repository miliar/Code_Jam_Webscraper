//============================================================================
// Name        : A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
using namespace std;

int map[26] = {24, 13, 5, 8, 2, 22, 11, 1, 10, 20, 14, 12, 23, 18, 4, 21, 25, 15, 3, 17, 9, 6, 19, 7, 0, 16};
int mapop[26];
string st, s;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d\n", &T);
	for (int i = 0; i < 26; ++i)
		mapop[map[i]] = i;
	for (int casenum = 1; casenum <= T; ++casenum)
	{
		printf("Case #%d:", casenum);
		getline(cin, st);
		stringstream stream(st);
		while (stream >> s)
		{
			printf(" ");
			for (int i = 0; i < s.length(); ++i)
				printf("%c", 'a' + mapop[s[i] - 'a']);
		}
		printf("\n");
	}
	return 0;
}
