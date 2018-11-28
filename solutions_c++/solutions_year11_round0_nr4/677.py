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
int N;
int P[1000];
int Q[1000];

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N;
		for (int I = 0; I < N; I++) cin >> P[I];
		for (int I = 0; I < N; I++) Q[I] = P[I];
		sort(Q, Q + N);
		int Temp = 0;
		for (int I = 0; I < N; I++)
			if (P[I] != Q[I]) Temp++;
		printf("Case #%d: %d.000000\n", TT, Temp);
	}
	return 0;
}
