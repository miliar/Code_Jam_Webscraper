#include <iostream>
using namespace std;

char table[4][4];

bool check(int x, int y)
{
	return x >= 0 && y >= 0 && x < 4 && y < 4;
}

int check(int x, int y, int vx, int vy)
{
	int cntO = 0, cntX = 0, cntT = 0;
	while (check(x, y))
	{
		if (table[x][y] == 'O')
			cntO++;
		if (table[x][y] == 'X')
			cntX++;
		if (table[x][y] == 'T')
			cntT++;
		x += vx;
		y += vy;
	}
	if (cntO + cntT == 4)
		return 0;
	if (cntX + cntT == 4)
		return 1;
	return 2;
}

void printAns(int num, int p, bool q)
{
	if (p == 0)
		printf("Case #%d: O won\n", num);
	if (p == 1)
		printf("Case #%d: X won\n", num);
	if (p == 2)
	{
		if (q)
			printf("Case #%d: Game has not completed\n", num);
		else
			printf("Case #%d: Draw\n", num);			
	}
}

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	int c;
	scanf("%d", &c);
	for (int k = 0; k < c; k++)
	{           
		scanf("\n");
		for (int s = 0; s < 4; s++)
			scanf("%s", table[s]);
                
        int t = 2;
		for (int i = 0; i < 4; i++)
		{       
			if (check(0, i, 1, 0) != 2)
				t = check(0, i, 1, 0);
			if (check(i, 0, 0, 1) != 2)
				t = check(i, 0, 0, 1);
		}
		if (check(0, 0, 1, 1) != 2)
			t = check(0, 0, 1, 1);
		if (check(3, 0, -1, 1) != 2)
			t = check(3, 0, -1, 1);

		bool is = false;
	
		for (int i = 0; i < 4; i++)
			for (int s = 0; s < 4; s++)
				if (table[i][s] == '.')
					is = true;
                        
        printAns(k + 1, t, is);
	}

	return 0;
}