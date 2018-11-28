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
int Xs[100000];
int Lens[100000];
int P[100000];

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N;
		for (int I = 0; I < N; I++) cin >> Xs[I] >> Lens[I];
		cin >> Xs[N];
		Lens[N] = Xs[N];
		P[0] = Xs[0];
		for (int I = 1; I <= N; I++) P[I] = -1;
		for (int I = 0; I < N; I++)
			if (P[I] >= 0)
		{
			for (int J = I + 1; J <= N && Xs[J] - Xs[I] <= P[I]; J++)
			{
				int Temp = min(Xs[J] - Xs[I], Lens[J]);
				if (Temp > P[J])
					P[J] = Temp;
			}
		}
		printf("Case #%d: ", TT);
		if (P[N] >= 0) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
