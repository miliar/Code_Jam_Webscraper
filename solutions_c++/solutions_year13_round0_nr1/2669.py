#include <stdio.h>
#include <vector>
#include <iostream>

using namespace std;

int val(char x)
{
	switch(x)
	{
	case 'X': return 100;
	case 'O': return 10000;
	default: return 1;
	}
}

void tictactoe()
{
	int T;
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases += 1)
	{
		char map[4][100];

		for(int i = 0; i < 4; i += 1)
		{
			scanf("%s", map[i]);
		}
		char dummy[1024];
		cin.getline (dummy,sizeof(dummy));

		bool someEmpty = false;

		// check won?
		int nx, no;
		int vx, vo;
		int vvx1, vvx2, vvo1, vvo2;
		bool won = false;
		vvx1 = vvx2 = vvo1 = vvo2 = 0;
		for(int i = 0; i < 4; i += 1)
		{
			nx = no = 0;
			vx = vo = 0;
			for(int j = 0; j < 4; j += 1)
			{
				if (map[i][j] == '.') someEmpty = true;

				nx += (map[i][j] == 'X' ? val(map[i][j]) : 0);
				nx += (map[i][j] == 'T' ? val(map[i][j]) : 0);
				no += (map[i][j] == 'O' ? val(map[i][j]) : 0);
				no += (map[i][j] == 'T' ? val(map[i][j]) : 0);

				vx += (map[j][i] == 'X' ? val(map[j][i]) : 0);
				vx += (map[j][i] == 'T' ? val(map[j][i]) : 0);
				vo += (map[j][i] == 'O' ? val(map[j][i]) : 0);
				vo += (map[j][i] == 'T' ? val(map[j][i]) : 0);

				if (i == j)
				{
					vvx1 += (map[i][j] == 'X' ? val(map[i][j]) : 0);
					vvx1 += (map[i][j] == 'T' ? val(map[i][j]) : 0);

					vvo1 += (map[i][j] == 'O' ? val(map[i][j]) : 0);
					vvo1 += (map[i][j] == 'T' ? val(map[i][j]) : 0);
				}

				if (i + j == 3)
				{
					vvx2 += (map[i][j] == 'X' ? val(map[i][j]) : 0);
					vvx2 += (map[i][j] == 'T' ? val(map[i][j]) : 0);

					vvo2 += (map[i][j] == 'O' ? val(map[i][j]) : 0);
					vvo2 += (map[i][j] == 'T' ? val(map[i][j]) : 0);
				}
			}

			

			if ((nx == 301 || nx == 400) || 
				(vx == 301 || vx == 400) ||
				(vvx1 == 301 || vvx1 == 400) ||
				(vvx2 == 301 || vvx2 == 400))
			{
				printf("Case #%d: X won\n", cases);
				i = 10;
				won = true;
				break;
			}
			else if ((no == 30001 || no == 40000) || 
				     (vo == 30001 || vo == 40000) ||
					 (vvo1 == 30001 || vvo1 == 40000) ||
				     (vvo2 == 30001 || vvo2 == 40000))
			{
				printf("Case #%d: O won\n", cases);
				i = 10;
				won = true;
				break;
			}
		}

		if (won) continue;

		if (someEmpty)
			printf("Case #%d: Game has not completed\n", cases);
		else
			printf("Case #%d: Draw\n", cases);
		
	}
}