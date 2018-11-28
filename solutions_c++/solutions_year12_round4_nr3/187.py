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
int N;
int Looks[2000];
int Ys[2000];

bool solve(int A, int B, int Gap)
{
	if (A >= B) return true;
	Ys[A] = Ys[B] - (B - A) * Gap;
	while (A != B)
	{
		int C = Looks[A];
		if (C <= A || C > B) return false;
		if (C < B) Ys[C] = Ys[B] - (B - C) * Gap;
		if (!solve(A + 1, C, Gap + 1)) return false;
		A = C;
	}
	return true;
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N;
		for (int I = 0; I < N - 1; I++) cin >> Looks[I];
		for (int I = 0; I < N - 1; I++) Looks[I]--;
		Looks[N - 1] = N;
		printf("Case #%d:", TT);
		Ys[N - 1] = 99999999;
		if (!solve(0, N - 1, 1))
			printf(" Impossible\n");
		else
		{
			for (int I = 0; I < N; I++) printf(" %d", Ys[I]);
			printf("\n");
		}
	}
	return 0;
}
