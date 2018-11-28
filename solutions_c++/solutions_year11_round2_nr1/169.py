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
char Board[1000][1000];
int Wins[1000], Loses[1000];
double WPs[1000], OWPs[1000], OOWPs[1000];

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N;
		for (int I = 0; I < N; I++) for (int J = 0; J < N; J++) cin >> Board[I][J];
		for (int I = 0; I < N; I++)
		{
			Wins[I] = Loses[I] = 0;
			for (int J = 0; J < N; J++)
				if (Board[I][J] == '1') Wins[I]++;
				else if (Board[I][J] == '0') Loses[I]++;
			WPs[I] = double(Wins[I]) / (Wins[I] + Loses[I]);
		}
		for (int I = 0; I < N; I++)
		{
			double OWP = 0;
			int Count = 0;
			for (int J = 0; J < N; J++)
				if (Board[I][J] != '.')
				{
					Count++;
					if (Board[I][J] == '1') OWP += double(Wins[J]) / (Wins[J] + Loses[J] - 1);
					else OWP += double(Wins[J] - 1) / (Wins[J] + Loses[J] - 1);
				}
			OWPs[I] = OWP / Count;
		}
		for (int I = 0; I < N; I++)
		{
			double OOWP = 0;
			int Count = 0;
			for (int J = 0; J < N; J++)
				if (Board[I][J] != '.')
				{
					Count++;
					OOWP += OWPs[J];
				}
			OOWPs[I] = OOWP / Count;
		}
		printf("Case #%d:\n", TT);
		for (int I = 0; I < N; I++)
		{
			printf("%.15f\n", 0.25 * WPs[I] + 0.5 * OWPs[I] + 0.25 * OOWPs[I]);
		}
	}
	return 0;
}
