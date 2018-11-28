#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <iostream>
#include <climits>
using namespace std;

typedef long long ll;
typedef long double ld;

#define SIZE

int t;
char board[5][5];
int rowx[5];
int rowo[5];
int colx[5];
int colo[5];
int row[5];
int col[5];
int diax, diao, dia, adiax, adiao, adia;
int main()
{
	int i, j, k;
	bool mark;
//	freopen("A-large.in", "r", stdin);
//	freopen("out", "w", stdout);
	cin >> t;
	for (i = 0; i < t; i++)
	{
		memset(rowx, 0, sizeof(rowx));
		memset(rowo, 0, sizeof(rowo));
		memset(colx, 0, sizeof(colx));
		memset(colo, 0, sizeof(colo));
		memset(row, 0, sizeof(row));
		memset(col, 0, sizeof(col));
		diax = 0;
		diao = 0;
		dia = 0;
		adiax = 0;
		adiao = 0;
		adia = 0;
		
		mark = false;
		for (j = 0; j < 4; j++)
			cin >> board[j];
			
		for (j = 0; j < 4; j++)
		for (k = 0; k < 4; k++)
		{
			if(board[j][k] != '.')
			{
				row[j]++;
				col[k]++;
				if (j == k)
					dia++;
				else if (j+k == 3)
					adia++;
			}
			if (board[j][k] == 'O')
			{
				rowo[j]++;
				colo[k]++;
				if (j == k)
					diao++;
				else if (j+k == 3)
					adiao++;	
			}
			else if (board[j][k] == 'X')
			{
				rowx[j]++;
				colx[k]++;
				if (j == k)
					diax++;
				else if (j+k == 3)
					adiax++;
			}
			else if (board[j][k] == 'T')
			{
				rowx[j]++;
				colx[k]++;
				rowo[j]++;
				colo[k]++;
				if (j == k)
				{
					diax++;
					diao++;
				}
				else if (j+k == 3)
				{	
					adiax++;
					adiao++;
				}
			}	
		}
		printf("Case #%d: ", i+1);
		if (rowo[0] == 4 || rowo[1] == 4 || rowo[2] == 4 || rowo[3] == 4 || colo[0] == 4 || colo[1] == 4 || colo[2] == 4 || colo[3] == 4 || diao == 4 || adiao == 4)
			printf("O won\n");
		else if (rowx[0] == 4 || rowx[1] == 4 || rowx[2] == 4 || rowx[3] == 4 || colx[0] == 4 || colx[1] == 4 || colx[2] == 4 || colx[3] == 4 || diax == 4 || adiax == 4)
			printf("X won\n");
		else if (row[0] == 4 && row[1] == 4 && row[2] == 4 && row[3] == 4 && col[0] == 4 && col[1] == 4 && col[2] == 4 && col[3] == 4 && dia == 4 && adia == 4)
			printf("Draw\n");
		else
			printf("Game has not completed\n");
				
	}
	return 0;
}
