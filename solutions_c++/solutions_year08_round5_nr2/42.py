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

struct node
{
	int X, Y, X1, Y1, X2, Y2;
};

int NN, TT;
int R, C;
bool Walls[15][15];
int StartX, StartY;
int CakeX, CakeY;
const int XOffs[4] = {-1, 0, 1, 0};
const int YOffs[4] = {0, 1, 0, -1};
int ShootXs[15][15][4];
int ShootYs[15][15][4];
bool Marks[15][15][15][15][15][15];
int Len;
node Queue[15 * 15 * 15 * 15 * 15 * 15];
int Found;

inline void add_node(const node& Nd)
{
	if (Marks[Nd.X][Nd.Y][Nd.X1][Nd.Y1][Nd.X2][Nd.Y2]) return;
	Marks[Nd.X][Nd.Y][Nd.X1][Nd.Y1][Nd.X2][Nd.Y2] = true;
	Queue[Len++] = Nd;
}

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> R >> C;
		for (int X = 0; X < R; X++) for (int Y = 0; Y < C; Y++)
		{
			char Ch;
			cin >> Ch;
			Walls[X][Y] = false;
			if (Ch == '#') Walls[X][Y] = true;
			if (Ch == 'O') StartX = X, StartY = Y;
			if (Ch == 'X') CakeX = X, CakeY = Y;
		}
		for (int X = 0; X < R; X++) for (int Y = 0; Y < C; Y++) if (!Walls[X][Y])
			for (int Dir = 0; Dir < 4; Dir++)
		{
			int XX = X;
			int YY = Y;
			while (XX >= 0 && XX < R && YY >= 0 && YY < C && !Walls[XX][YY])
			{
				ShootXs[X][Y][Dir] = XX;
				ShootYs[X][Y][Dir] = YY;
				XX += XOffs[Dir];
				YY += YOffs[Dir];
			}
		}
		memset(Marks, false, sizeof Marks);
		Len = 0;
		Found = -1;
		for (int D1 = 0; D1 < 4; D1++) for (int D2 = 0; D2 < 4; D2++)
		{
			node Nd;
			Nd.X = StartX;
			Nd.Y = StartY;
			Nd.X1 = ShootXs[StartX][StartY][D1];
			Nd.Y1 = ShootYs[StartX][StartY][D1];
			Nd.X2 = ShootXs[StartX][StartY][D2];
			Nd.Y2 = ShootYs[StartX][StartY][D2];
			add_node(Nd);
		}
		int Step = 0;
		int Cursor = 0;
		while (Found < 0 && Cursor < Len)
		{
			int End = Len;
			Step++;
			for (; Cursor < End && Found < 0; Cursor++)
			{
				node Nd = Queue[Cursor];
				node Nd2;
				for (int Dir = 0; Dir < 4; Dir++)
				{
					Nd2.X = Nd.X + XOffs[Dir];
					Nd2.Y = Nd.Y + YOffs[Dir];
					if (Nd2.X < 0 || Nd2.X >= R || Nd2.Y < 0 || Nd2.Y >= C || Walls[Nd2.X][Nd2.Y])
					{
						if (Nd.X == Nd.X1 && Nd.Y == Nd.Y1)
							Nd2.X = Nd.X2, Nd2.Y = Nd.Y2;
						else if (Nd.X == Nd.X2 && Nd.Y == Nd.Y2)
							Nd2.X = Nd.X1, Nd2.Y = Nd.Y1;
						else
							continue;
					}
					if (Nd2.X == CakeX && Nd2.Y == CakeY) Found = Step;
					for (int D1 = -1; D1 < 4; D1++)
					{
						if (D1 >= 0)
							Nd2.X1 = ShootXs[Nd2.X][Nd2.Y][D1],
							Nd2.Y1 = ShootYs[Nd2.X][Nd2.Y][D1];
						else
							Nd2.X1 = Nd.X1, Nd2.Y1 = Nd.Y1;
						for (int D2 = -1; D2 < 4; D2++)
						{
							if (D2 >= 0)
								Nd2.X2 = ShootXs[Nd2.X][Nd2.Y][D2],
								Nd2.Y2 = ShootYs[Nd2.X][Nd2.Y][D2];
							else
								Nd2.X2 = Nd.X2, Nd2.Y2 = Nd.Y2;
							add_node(Nd2);
						}
					}
				}
			}
		}
		printf("Case #%d: ", TT);
		if (Found < 0) printf("THE CAKE IS A LIE\n");
		else printf("%d\n", Found);
	}
	return 0;
}
