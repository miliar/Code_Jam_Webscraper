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
const int N = 101;
bool P[101][101];

bool process()
{
	bool Result = false;
	for (int X = N - 1; X > 0; X--) for (int Y = N - 1; Y > 0; Y--)
	{
		if (P[X][Y])
		{
			if (!P[X - 1][Y] && !P[X][Y - 1]) P[X][Y] = false;
		}
		else
		{
			if (P[X - 1][Y] && P[X][Y - 1]) P[X][Y] = true;
		}
		if (P[X][Y]) Result = true;
	}
	return Result;
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		int R;
		scanf("%d", &R);
		memset(P, 0, sizeof(P));
		while (R-- > 0)
		{
			int X1, Y1, X2, Y2;
			scanf("%d%d%d%d", &X1, &Y1, &X2, &Y2);
			for (int X = X1; X <= X2; X++) for (int Y = Y1; Y <= Y2; Y++)
				P[X][Y] = true;
		}
		int Time = 0;
		while (process()) Time++;
		printf("Case #%d: %d\n", TT, Time + 1);
	}
	return 0;
}