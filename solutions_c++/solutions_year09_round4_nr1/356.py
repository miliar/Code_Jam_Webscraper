#define _CRT_SECURE_NO_DEPRECATE
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
int N;
char Map[100][101];
int P[100], Q[100];
int Count;

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N;
		for (int X = 0; X < N; X++) cin >> Map[X];
		for (int X = 0; X < N; X++)
		{
			P[X] = X;
			Q[X] = -1;
			for (int Y = 0; Y < N; Y++)
				if (Map[X][Y] == '1')
				{
					Q[X] = Y;
				}
		}
		Count = 0;
		for (; N >= 2; N--)
		{
			int X;
			for (X = 0; X < N; X++)
				if (Q[0] <= P[X]) break;
			if (X == N) printf("???");
			if (X > 0)
			{
				Count += X;
				for (int I = X; I >= 1; I--) P[I] = P[I - 1];
			}
			for (int I = 0; I < N - 1; I++) Q[I] = Q[I + 1], P[I] = P[I + 1];
		}
		printf("Case #%d: %d\n", TT, Count);
	}
	return 0;
}