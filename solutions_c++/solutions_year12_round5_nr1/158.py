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

struct node
{
	int Lev, Time, Prob;
};

struct node_less
{
	bool operator()(const node& A, const node& B) const
	{
		int ScoreA = A.Time * 100 + (100 - A.Prob) * B.Time;
		int ScoreB = B.Time * 100 + (100 - B.Prob) * A.Time;
		if (ScoreA != ScoreB) return ScoreA < ScoreB;
		return A.Lev < B.Lev;
	}
};

int N;
node P[1000];

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N;
		for (int I = 0; I < N; I++) P[I].Lev = I;
		for (int I = 0; I < N; I++) cin >> P[I].Time;
		for (int I = 0; I < N; I++) cin >> P[I].Prob;
		sort(P, P + N, node_less());
		printf("Case #%d:", TT);
		for (int I = 0; I < N; I++) printf(" %d", P[I].Lev);
		printf("\n");
	}
	return 0;
}
