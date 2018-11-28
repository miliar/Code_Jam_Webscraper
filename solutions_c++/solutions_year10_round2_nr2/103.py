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
int N, KK, B, T;
int P[100], Q[100];

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N >> KK >> B >> T;
		for (int I = 0; I < N; I++) cin >> P[I];
		for (int I = 0; I < N; I++) cin >> Q[I];
		int Result = 0;
		int Count = 0;
		for (int I = N - 1; I >= 0; I--)
			if (P[I] + Q[I] * T >= B && Count < KK)
			{
				Result += N - I - 1 - Count;
				Count++;
			}

		printf("Case #%d: ", TT);
		if (Count < KK) printf("IMPOSSIBLE\n");
		else printf("%d\n", Result);
	}
	return 0;
}