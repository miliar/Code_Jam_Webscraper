#define _CRT_SECURE_NO_DEPRECATE
#ifdef NDEBUG
	#define _SECURE_SCL 0
#endif
#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

const int Xs[4] = {-1, 0, 0, 1};
const int Ys[4] = {0, -1, 1, 0};

int NN, TT;
int H, W;
int Map[100][100];
char Results[100][100];
char Cursor;

char dfs(int X, int Y)
{
	if (Results[X][Y] != 0) return Results[X][Y];
	int X0 = X, Y0 = Y;
	for (int D = 0; D < 4; D++)
	{
		int XX = X + Xs[D];
		int YY = Y + Ys[D];
		if (XX >= 0 && XX < H && YY >= 0 && YY < W && Map[XX][YY] < Map[X0][Y0])
		{
			X0 = XX;
			Y0 = YY;
		}
	}
	if (X0 == X && Y0 == Y)
		return Results[X][Y] = Cursor++;
	return Results[X][Y] = dfs(X0, Y0);
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> H >> W;
		for (int X = 0; X < H; X++) for (int Y = 0; Y < W; Y++) cin >> Map[X][Y];
		memset(Results, 0, sizeof Results);
		Cursor = 'a';
		for (int X = 0; X < H; X++) for (int Y = 0; Y < W; Y++) dfs(X, Y);
		printf("Case #%d:\n", TT);
		for (int X = 0; X < H; X++)
		{
			for (int Y = 0; Y < W; Y++)
			{
				if (Y > 0) printf(" ");
				printf("%c", Results[X][Y]);
			}
			printf("\n");
		}
	}
	return 0;
}