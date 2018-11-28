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
int Table[2][31];

int main()
{
	memset(Table, -1, sizeof(Table));
	for (int I = 0; I <= 10; I++)
		for (int J = max(I - 1, 0); J <= 10; J++)
			for (int K = max(I - 1, 0); K <= 10; K++)
				Table[0][I + J + K] = max(Table[0][I + J + K], I);
	for (int I = 0; I <= 10; I++)
		for (int J = max(I - 2, 0); J <= 10; J++)
			for (int K = max(I - 2, 0); K <= 10; K++)
				if (I - K == 2 || I - J == 2)
					Table[1][I + J + K] = max(Table[1][I + J + K], I);
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		int N, S, P;
		cin >> N >> S >> P;
		int Cnts[4] = {0};
		int Spec = 0;
		for (int I = 0; I < N; I++)
		{
			int Tmp;
			cin >> Tmp;
			bool A = Table[0][Tmp] >= P;
			bool B = Table[1][Tmp] >= P;
			Cnts[A + B * 2]++;
			if (A + B * 2 == 0 && Tmp >= 2) Spec++;
		}
		int Ans = Cnts[1] + Cnts[2] + Cnts[3];
		if (S < Cnts[2]) Ans -= Cnts[2] - S;
		else if (S > Spec + Cnts[2] + Cnts[3]) Ans -= S - (Spec + Cnts[2] + Cnts[3]);
		printf("Case #%d: %d\n", TT, Ans);
	}
	return 0;
}
