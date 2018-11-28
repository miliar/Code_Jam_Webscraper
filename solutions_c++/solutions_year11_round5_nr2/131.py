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
int Counts[10001];
vector<int> P, Q;
int Answer;

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		memset(Counts, 0, sizeof(Counts));
		cin >> N;
		for (int I = 0; I < N; I++)
		{
			int Temp;
			cin >> Temp;
			Counts[Temp - 1]++;
		}
		Answer = 999999;
		P.clear();
		for (int Val = 0; Val <= 10000; Val++)
		{
			int Count = Counts[Val];
			if (Count < (int)P.size())
			{
				for (int I = 0; I < Count; I++) P[I]++;
				if (P[Count] < Answer) Answer = P[Count];
				P.resize(Count);
			}
			else
			{
				for (int I = 0; I < (int)P.size(); I++) P[I]++;
				Q.assign(Count - P.size(), 1);
				P.insert(P.begin(), Q.begin(), Q.end());
			}
		}
		if (N == 0) Answer = 0;
		printf("Case #%d: %d\n", TT, Answer);
	}
	return 0;
}
