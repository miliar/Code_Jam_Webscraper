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
#include <cassert>

using namespace std;

int NN, TT;
int N, M;
set<string> Dict;

int add(const string& S)
{
	int Count = 0;
	for (int I = S.length(); I > 0; I--)
		if (I == S.length() || S[I] == '/')
		{
			if (Dict.find(S.substr(0, I)) == Dict.end())
			{
				Count++;
				Dict.insert(S.substr(0, I));
			}
			else
				break;
		}
	return Count;
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N >> M;
		Dict.clear();
		string S;
		for (int I = 0; I < N; I++)
		{
			cin >> S;
			add(S);
		}
		int Result = 0;
		for (int I = 0; I < M; I++)
		{
			cin >> S;
			Result += add(S);
		}
		printf("Case #%d: %d\n", TT, Result);
	}
	return 0;
}