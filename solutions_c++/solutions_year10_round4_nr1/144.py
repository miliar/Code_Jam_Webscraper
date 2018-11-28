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
int Size;
char P[1000][1000];

int cost_of(int Size)
{
	return (1 + (Size - 1)) * (Size - 1) + Size;
}

int y_start(int X, int Size)
{
	if (X <= Size) return Size - X;
	return X - Size;
}

int y_end(int X, int Size)
{
	if (X <= Size) return y_start(X, Size) + X * 2 - 2;
	return y_start(X, Size) + (Size * 2 - X) * 2 - 2;
}

bool inside(int X, int Y, int Size)
{
	if (X < 1 || X >= Size * 2) return false;
	if (Y < y_start(X, Size) || Y > y_end(X, Size)) return false;
	return true;
}

void get_list(int X0, int Y0, int X, int Y, int Xs[], int Ys[])
{
	Xs[0] = X;
	Ys[0] = Y;
	Xs[1] = X0 + X0 - X;;
	Ys[1] = Y;
	Xs[2] = X;
	Ys[2] = Y0 + Y0 - Y;
	Xs[3] = Xs[1];
	Ys[3] = Ys[2];
}


bool is_ok(int X0, int Y0, int& NewSize)
{
	for (int X = 1; X < Size * 2; X++)
	{
		int YStart = y_start(X, Size);
		int YEnd = y_end(X, Size);
		for (int Y = YStart; Y <= YEnd; Y += 2)
		{
			int Xs[4], Ys[4];
			get_list(X0, Y0, X, Y, Xs, Ys);
			char Temp = P[X][Y];
			for (int I = 0; I < 4; I++)
				if (inside(Xs[I], Ys[I], Size) && P[Xs[I]][Ys[I]] != Temp) return false;
		}
	}
	NewSize = Size;
	for (int X = 1; X < Size * 2; X++)
	{
		int YStart = y_start(X, Size);
		int YEnd = y_end(X, Size);
		for (int Y = YStart; Y <= YEnd; Y += 2)
		{
			int Temp = abs(X - X0) + abs(Y - Y0) + 1;
			if (Temp > NewSize) NewSize = Temp;
		}
	}
	return true;
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		scanf("%d", &Size);
		memset(P, 0, sizeof(P));
		for (int X = 1; X < Size * 2; X++)
		{
			int YStart = y_start(X, Size);
			int YEnd = y_end(X, Size);
			for (int Y = YStart; Y <= YEnd; Y += 2)
				scanf(" %c", &P[X][Y]);
		}
		int NewSize = Size * 10;
		for (int X = 1; X < Size * 2; X++)
		{
			int Temp;
			for (int Y = 0; Y < Size * 2; Y++)
				if (is_ok(X, Y, Temp))
				{
					if (Temp < NewSize) NewSize = Temp;
				}
		}
		printf("Case #%d: %d\n", TT, cost_of(NewSize) - cost_of(Size));
	}
	return 0;
}