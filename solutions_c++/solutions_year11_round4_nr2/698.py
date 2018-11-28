#include <iostream>
#include <xutility>
#include <vector>
#include <functional>
#include <algorithm>
#include <math.h>

using namespace std;

void SolveTest();

void main()
{
	int numTests;
	cin >> numTests;

	for(int i = 0; i < numTests; ++i)
	{
		cout << "Case #" << i+1 << ": ";
		SolveTest();
		cout << endl;
	}
}

void SolveTest()
{
	int R, C, D;
	cin >> R >> C >> D;

	int cells[10][10];

	//Read in
	for(int i = 0; i < R; ++i)
	{
		for(int j = 0; j < C; ++j)
		{
			char next = 0;
			while(next < '0' || next > '9')
				scanf("%c", &next);
			
			cells[i][j] = D + int(next - '0');
		}
	}

	//Try squares largest to smallest
	int squareSize = min(R, C);
	while(squareSize >= 3)
	{
		for(int startX = 0; startX <= R - squareSize; ++startX)
		{
			for(int startY = 0; startY <= C - squareSize; ++startY)
			{
				//Check if centre of mass is at centre
				double cX = double(squareSize) / 2 + startX;
				double cY = double(squareSize) / 2 + startY;

				pair<double, double> sum(0,0);

				for(int i = startX; i < startX + squareSize; ++i)
				{
					for(int j = startY; j < startY + squareSize; ++j)
					{
						if((i == startX || i == startX + squareSize - 1) && (j == startY || j == startY + squareSize - 1))
							continue; //Corner piece

						pair<double, double> disp(i - cX + 0.5, j - cY + 0.5);

						sum.first += disp.first * cells[i][j];
						sum.second += disp.second * cells[i][j];
					}
				}

				if(fabs(sum.first) < 0.000001 && fabs(sum.second) < 0.000001)
				{
					cout << squareSize;
					return;
				}
			}
		}

		--squareSize;
	}

	cout << "IMPOSSIBLE";
}

