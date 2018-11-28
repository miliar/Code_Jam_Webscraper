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

using namespace std;

int NN, TT;
int L;
int Area;
int MinX, MinY, MaxX, MaxY;
int MinXs[10000], MaxXs[10000], MinYs[10000], MaxYs[10000];
bool Marks[6001][6001];

inline void walk(int& X, int& Y, int Dir)
{
	static const int XOffs[4] = {0, 1, 0, -1};
	static const int YOffs[4] = {1, 0, -1, 0};
	int XX = X + XOffs[Dir];
	int YY = Y + YOffs[Dir];
	Area += X * YY - XX * Y;
	if (XX < MinX) MinX = XX;
	if (XX > MaxX) MaxX = XX;
	if (YY < MinY) MinY = YY;
	if (YY > MaxY) MaxY = YY;
	if (Dir % 2 == 0)
	{
		int MY = min(Y, YY);
		if (X < MinXs[MY]) MinXs[MY] = X;
		if (X > MaxXs[MY]) MaxXs[MY] = X;
	}
	else
	{
		int MX = min(X, XX);
		if (Y < MinYs[MX]) MinYs[MX] = Y;
		if (Y > MaxYs[MX]) MaxYs[MX] = Y;
	}
	X = XX;
	Y = YY;
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> L;
		int X = 3000;
		int Y = 3000;
		int Dir = 0;
		Area = 0;
		MinX = MaxX = MinY = MaxY = 3000;
		for (int I = 0; I <= 6000; I++) MinXs[I] = MinYs[I] = 999999;
		for (int I = 0; I <= 6000; I++) MaxXs[I] = MaxYs[I] = -999999;
		while (L-- > 0)
		{
			char S[101];
			int T;
			cin >> S >> T;
			while (T-- > 0)
				for (int I = 0; S[I] != 0; I++)
				{
					if (S[I] == 'L') Dir = (Dir + 3) % 4;
					else if (S[I] == 'R') Dir = (Dir + 1) % 4;
					else if (S[I] == 'F') walk(X, Y, Dir);
				}
		}
		if (Area < 0) Area = -Area;
		Area /= 2;
		for (int X = MinX; X < MaxX; X++)
			for (int Y = MinY; Y < MaxY; Y++)
				Marks[X][Y] = false;
		for (int X = MinX; X < MaxX; X++)
			for (int Y = MinYs[X]; Y < MaxYs[X]; Y++)
				Marks[X][Y] = true;
		for (int Y = MinY; Y < MaxY; Y++)
			for (int X = MinXs[Y]; X < MaxXs[Y]; X++)
				Marks[X][Y] = true;
		int Total = 0;
		for (int X = MinX; X < MaxX; X++)
			for (int Y = MinY; Y < MaxY; Y++)
				Total += Marks[X][Y];
		printf("Case #%d: %d\n", TT, Total - Area);
	}
	return 0;
}
