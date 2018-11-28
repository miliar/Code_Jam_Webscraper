#define _CRT_SECURE_NO_DEPRECATE
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
int N, M;
vector<int> Items[100];
bool Less[100][100];
int Len;
int List[100];
int Result;

void search(int Id)
{
	if (Id == N)
	{
		if (Len < Result) Result = Len;
		return;
	}
	if (Len >= Result) return;
	bool Found = false;
	for (int I = Len - 1; I >= 0; I--)
		if (Less[List[I]][Id])
		{
			Found = true;
			int Last = List[I];
			List[I] = Id;
			search(Id + 1);
			List[I] = Last;
		}
	if (!Found)
	{
		List[Len++] = Id;
		search(Id + 1);
		Len--;
	}
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N >> M;
		for (int I = 0; I < N; I++)
		{
			Items[I].resize(M);
			for (int J = 0; J < M; J++) cin >> Items[I][J];
		}
		sort(Items, Items + N);
		for (int I = 0; I < N; I++) for (int J = 0; J < N; J++)
		{
			Less[I][J] = true;
			for (int K = 0; K < M; K++) if (Items[I][K] >= Items[J][K]) Less[I][J] = false;
		}
		Result = N;
		Len = 0;
		search(0);
		printf("Case #%d: %d\n", TT, Result);
	}
	return 0;
}