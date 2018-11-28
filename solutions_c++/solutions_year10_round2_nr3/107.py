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

const int Base = 100003;

int NN, TT;
int N;
int P[501][501][501];

int main()
{
	cin >> NN;
	memset(P, 0, sizeof(P));
	for (int I = 2; I <= 500; I++)
	{
		for (int J = 1; J < I; J++)
		{
			for (int K = 2; K < I; K++)
			{
				P[I][J][K] = P[I - 1][J][K];
				if (J != K) P[I][J][K] += P[I - 1][J - 1][K];
				P[I][J][K] %= 100003;
			}
			if (J == 1) P[I][J][I] = 1;
			else P[I][J][I] += P[I - 1][J - 1][J];
			P[I][J][I] %= 100003;
		}
	}
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N;
		int Result = 0;
		for (int I = 1; I <= N; I++) Result = (Result + P[N][I][N]) % 100003;
		printf("Case #%d: %d\n", TT, Result);
	}
	return 0;
}