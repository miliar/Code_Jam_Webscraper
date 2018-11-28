#define _CRT_SECURE_NO_DEPRECATE
#ifdef NDEBUG
	#define _SECURE_SCL 0
#endif
#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
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
char S[] = "welcome to code jam";
char T[1001];
int P[1001][21];

int main()
{
	cin >> NN;
	cin.getline(T, sizeof T);
	for (TT = 1; TT <= NN; TT++)
	{
		N = (int)strlen(S);
		cin.getline(T, sizeof T);
		M = (int)strlen(T);
		memset(P, 0, sizeof P);
		P[0][0] = 1;
		for (int I = 1; I <= M; I++)
		{
			P[I][0] = 1;
			for (int J = 1; J <= N; J++)
			{
				if (S[J - 1] == T[I - 1])
					P[I][J] = P[I - 1][J - 1];
				P[I][J] += P[I - 1][J];
				P[I][J] %= 10000;
			}
		}
		printf("Case #%d: %04d\n", TT, P[M][N]);
	}
	return 0;
}