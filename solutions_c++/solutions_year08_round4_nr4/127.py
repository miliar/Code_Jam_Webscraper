#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>

using namespace std;

int NN, TT;
int Unit;
int Len;
char S[100001];
int P[16][16][65536];
int Bits[65536];

int count_bits(int V)
{
	int Result = 0;
	while (V > 0)
	{
		if (V & 1) Result++;
		V >>= 1;
	}
	return Result;
}

int main()
{
	for (int I = 0; I < 65536; I++) Bits[I] = count_bits(I);
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> Unit >> S;
		Len = (int)strlen(S);
		for (int I = 0; I < Unit; I++)
			P[I][I][1 << I] = 0;
		int Increases[16][16] = {0};
		for (int R = 0; R < Unit; R++)
			for (int R0 = 0; R0 < Unit; R0++)
				for (int I = 0; I < Len; I += Unit)
					if (S[I + R0] != S[I + R]) Increases[R][R0]++;
		int GIncreases[16][16] = {0};
		for (int L = 0; L < Unit; L++)
			for (int R = 0; R < Unit; R++)
				for (int I = 0; I + Unit < Len; I += Unit)
					if (S[I + R] != S[I + Unit + L]) GIncreases[L][R]++;
		for (int Pos = 1; Pos < Unit; Pos++)
		{
			for (int Mark = 0; Mark < (1 << Unit); Mark++) if (Bits[Mark] == Pos + 1)
				for (int L = 0; L < Unit; L++) if ((Mark >> L) & 1)
					for (int R = 0; R < Unit; R++) if ((Mark >> R) & 1) if (L != R)
					{
						P[L][R][Mark] = 0xfffffff;
						for (int R0 = 0; R0 < Unit; R0++)
							if ((Mark >> R0) & 1) if (R0 != R) if (Pos == 1 || R0 != L)
							{
								int Temp = P[L][R0][Mark & ~(1 << R)];
								if (Temp + Increases[R0][R] < P[L][R][Mark])
									P[L][R][Mark] = Temp + Increases[R0][R];
							}
						if (Pos == Unit - 1) P[L][R][Mark] += GIncreases[L][R];
					}
		}
		int Result = 0x7fffffff;
		for (int L = 0; L < Unit; L++)
			for (int R = 0; R < Unit; R++) if (L != R)
				if (P[L][R][(1 << Unit) - 1] < Result)
					Result = P[L][R][(1 << Unit) - 1];
		Result++;
		cout << "Case #" << TT << ": " << Result << endl;
	}
	return 0;
}
