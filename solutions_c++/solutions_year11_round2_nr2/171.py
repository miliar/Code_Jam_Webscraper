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
long long Dis;
pair<long long, long long> List[1000];

bool possible(long long Time)
{
	long long LastPos = -0x7fffffffffffffff;
	for (int I = 0; I < N; I++)
	{
		long long Pos = List[I].first - Time;
		if (Pos < LastPos + Dis) Pos = LastPos + Dis;
		Pos += (List[I].second - 1) * Dis;
		if (Pos > List[I].first + Time) return false;
		LastPos = Pos;
	}
	return true;
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N >> Dis;
		for (int I = 0; I < N; I++) cin >> List[I].first >> List[I].second;
		Dis *= 2;
		for (int I = 0; I < N; I++) List[I].first *= 2;
		long long Time = 1;
		while (!possible(Time)) Time *= 2;
		for (long long Delta = Time; Delta >= 1; Delta /= 2)
			while (possible(Time - Delta)) Time -= Delta;
		printf("Case #%d: %.1f\n", TT, (double)Time / 2);
	}
	return 0;
}
