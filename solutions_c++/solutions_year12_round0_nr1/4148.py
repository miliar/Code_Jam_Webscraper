#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable: 4018)
#ifdef NDEBUG
	#define _SECURE_SCL 0
#endif
#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>

using namespace std;

int NN, TT;
map<char, char> Map;
bool AMarks[256], BMarks[256];

void doit(string A, string B)
{
	for (int I = 0; I < (int)A.length(); I++)
		Map[A[I]] = B[I];
}

char remaining(bool P[])
{
	for (char Ch = 'a'; Ch <= 'z'; Ch++)
		if (!P[Ch]) return Ch;
	return 0;
}

int main()
{
	Map['y'] = 'a';
	Map['e'] = 'o';
	Map['q'] = 'z';
	doit("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	doit("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	doit("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
	for (map<char, char>::iterator It = Map.begin(); It != Map.end(); ++It)
	{
		AMarks[It->first] = true;
		BMarks[It->second] = true;
	}
	Map[remaining(AMarks)] = remaining(BMarks);
	cin >> NN;
	string S;
	getline(cin, S);
	for (TT = 1; TT <= NN; TT++)
	{
		printf("Case #%d: ", TT);
		getline(cin, S);
		for (int I = 0; I < (int)S.length(); I++)
			printf("%c", Map[S[I]]);
		printf("\n");
	}
	return 0;
}
