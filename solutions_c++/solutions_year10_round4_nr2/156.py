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

const long long Inf = 0x7fffffff;
int NN, TT;
int N, P;
int Prices[11][1024];
int Ms[1024];
long long Q[11][1024][11];

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		scanf("%d", &P);
		N = 1 << P;
		memset(Q, 0, sizeof(Q));
		for (int I = 0; I < N; I++) scanf("%d", &Ms[I]);
		for (int I = 1; I <= P; I++)
			for (int J = 0; J < (1 << (P - I)); J++) scanf("%d", &Prices[I][J]);
		for (int I = 0; I < N; I++) for (int J = 0; J <= P; J++)
			if (P - J <= Ms[I]) Q[0][I][J] = 0;
			else Q[0][I][J] = Inf;
		for (int R = 1; R <= P; R++)
			for (int I = 0; I < (1 << (P - R)); I++)
				for (int J = 0; J <= P - R; J++)
				{
					Q[R][I][J] = min(Inf, Q[R - 1][I * 2][J] + Q[R - 1][I * 2 + 1][J]);
					long long Temp = Prices[R][I] + Q[R - 1][I * 2][J + 1] + Q[R - 1][I * 2 + 1][J + 1];
					if (Temp < Q[R][I][J]) Q[R][I][J] = Temp;
				}
		printf("Case #%d: %d\n", TT, (int)Q[P][0][0]);
	}
	return 0;
}