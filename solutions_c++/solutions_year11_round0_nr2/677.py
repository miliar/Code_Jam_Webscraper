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
int Combs[26][26];
bool Opps[26][26];
int N;
int Len;
int P[1000];

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		char A, B, C;
		memset(Combs, -1, sizeof(Combs));
		memset(Opps, 0, sizeof(Opps));
		cin >> N;
		while (N-- > 0)
		{
			cin >> A >> B >> C;
			Combs[A - 'A'][B - 'A'] = C - 'A';
			Combs[B - 'A'][A - 'A'] = C - 'A';
		}
		cin >> N;
		while (N-- > 0)
		{
			cin >> A >> B;
			Opps[A - 'A'][B - 'A'] = true;
			Opps[B - 'A'][A - 'A'] = true;
		}
		Len = 0;
		cin >> N;
		while (N-- > 0)
		{
			cin >> A;
			P[Len++] = A - 'A';
			while (Len >= 2 && Combs[P[Len - 1]][P[Len - 2]] >= 0)
			{
				P[Len - 2] = Combs[P[Len - 1]][P[Len - 2]];
				Len--;
			}
			bool Opposed = false;
			for (int I = 0; I < Len - 1; I++)
				if (Opps[P[Len - 1]][P[I]]) Opposed = true;
			if (Opposed) Len = 0;
		}
		printf("Case #%d: [", TT);
		for (int I = 0; I < Len; I++)
		{
			if (I > 0) printf(", ");
			printf("%c", 'A' + P[I]);
		}
		printf("]\n");
	}
	return 0;
}
