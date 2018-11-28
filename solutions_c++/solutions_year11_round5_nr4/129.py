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
int Len;
char Str[100];
long long Target;
int N;
int List[20];
int Choices[100];

bool solve(long long Value)
{
	long long Ans = 0;
	for (long long Delta = 1LL << 30; Delta >= 1; Delta >>= 1)
		if ((Ans + Delta) * (Ans + Delta) <= Value) Ans += Delta;
	if (Ans * Ans == Value) return true;
	return false;
}

bool dfs(long long Value, int I)
{
	if (I >= N)
	{
		return solve(Value);
	}
	int J = List[I];
	Choices[J] = 0;
	if (dfs(Value, I + 1)) return true;
	Choices[J] = 1;
	return dfs(Value | 1LL << J, I + 1);
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> Str;
		Len = strlen(Str);
		Target = 0;
		reverse(Str, Str + Len);
		N = 0;
		for (int I = 0; I < Len; I++)
		{
			if (Str[I] == '1') Target |= 1LL << I;
			if (Str[I] == '?') List[N++] = I;
		}
		if (!dfs(Target, 0)) printf("ERROR\n");
		printf("Case #%d: ", TT);
		for (int I = Len - 1; I >= 0; I--)
		{
			if (Str[I] != '?') printf("%c", Str[I]);
			else printf("%d", Choices[I]);
		}
		printf("\n");
	}
	return 0;
}
