#include <iostream>
#include <fstream>
#include <string.h>
#include <conio.h>

using namespace std;

enum BOOL {FALSE, TRUE};

int C, R;
BOOL Cells[101][101];
ifstream ifile;
ofstream ofile;

void Input();
int Process();


void main()
{
	int i, result;

	ifile.open("A-small-practice.in");
	ofile.open("A-small-practice.out");

	ifile >> C;

	for ( i = 0; i < C; i++)
	{
		Input();
		result = Process();

		ofile << "Case #" << i+1 << ": " << result + 1 << endl;
	}

	ifile.close();
	ofile.close();
}

void Input()
{
	int X1, X2, Y1, Y2, i, o, x;

	ifile >> R;

	for(i = 0;i < R; i++)
	{
		ifile >> X1 >> Y1 >> X2 >> Y2;
		for(o = Y1; o <= Y2; o++)
		{
			for(x = X1; x <= X2; x++)
				Cells[o][x] = TRUE;
		}
	}
}

int Process()
{
	BOOL IsDone = TRUE, Copy[101][101];
	int x, y, count = -1;

		for(y = 1; y<= 100; y++)
		{
			for(x = 1; x <= 100; x++)
			{
				Copy[y][x] = Cells[y][x];
				if(Cells[y][x])
					IsDone = FALSE;
			}
		}
	while(!IsDone)
	{
		IsDone = TRUE;
		count++;

		for(y = 1;y <= 100; y++)
		{
			for(x = 1; x <= 100; x++)
			{
				if(Cells[y][x])
				{
					if(y == 1 && x == 1)
						Copy[1][1] = FALSE;
					else if(y == 1 && !Cells[y][x - 1])
						Copy[y][x] = FALSE;
					else if(x == 1 && !Cells[y - 1][x])
						Copy[y][x] = FALSE;
					else
					{
						if(!Cells[y-1][x] && !Cells[y][x-1])
							Copy[y][x] = FALSE;
					}
				}
				else
				{
					if(x > 1 && y > 1)
					{
						if(Cells[y - 1][x] && Cells[y][x - 1])
							Copy[y][x] = TRUE;
					}
				}
			//	if(Cells[y][x] == Copy[y][x])
			//	{
			//	}
				//Copy[y][x] = Cells[y][x]
			}
		}
		/*for(y = 1; y<= 20; y++)
		{
			for(x = 1; x <= 20; x++)
			{
				cout << Cells[y][x];
			}
			cout << endl;
		}

		getch();*/

		for(y = 1; y<= 100; y++)
		{
			for(x = 1; x <= 100; x++)
			{
				Cells[y][x] = Copy[y][x];
				if(Cells[y][x])
					IsDone = FALSE;
			}
		}
	}

	return count;
}