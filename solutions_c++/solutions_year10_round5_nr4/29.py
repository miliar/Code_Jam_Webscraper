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
int Base, N;
long long Result;
int Marks[8][10];
int P[100];

void dfs(int Index, int Sum)
{
	if (Sum > N) return;
	if (Sum == N)
	{
		Result++;
		return;
	}
	for (int Val = 1; Val <= N; Val++)
	{
		bool Ok = true;
		int Temp = Val;
		for (int M = 0; Temp > 0; M++)
		{
			int Dig = Temp % Base;
			Temp /= Base;
			if (Marks[M][Dig]) Ok = false;
			Marks[M][Dig]++;
		}
		Temp = Val;
		if (Ok)
		{
			P[Index] = Val;
			if (Index == 0 || Val > P[Index - 1]) dfs(Index + 1, Sum + Val);
		}
		for (int M = 0; Temp > 0; M++)
		{
			int Dig = Temp % Base;
			Temp /= Base;
			Marks[M][Dig]--;
		}
	}
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N >> Base;
		memset(Marks, 0, sizeof(Marks));
		Result = 0;
		dfs(0, 0);
		printf("Case #%d: %d\n", TT, (int)Result);
	}
	return 0;
}