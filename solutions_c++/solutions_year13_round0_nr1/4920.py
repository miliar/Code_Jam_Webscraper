#include <iostream>
#include <cstdio>

using namespace std;

int T;
char a[4][4];
bool dots;
int Tx, Ty;

int wins(int x, int y)
{
	int i,j;
	if(Tx != -1)
		a[Tx][Ty] = 'X';
	
	if(x + 3 < 4 && a[x][y] == 'X' && a[x+1][y] == 'X' && a[x+2][y] == 'X' && a[x+3][y] == 'X') return 1;
	if(y + 3 < 4 && a[x][y] == 'X' && a[x][y+1] == 'X' && a[x][y+2] == 'X' && a[x][y+3] == 'X') return 1;
	if(x + 3 < 4 && y + 3 < 4 && a[x][y] == 'X' && a[x+1][y+1] == 'X' && a[x+2][y+2] == 'X' && a[x+3][y+3] == 'X') return 1;
	if(x - 3 >= 0 && y + 3 < 4 && a[x][y] == 'X' && a[x-1][y+1] == 'X' && a[x-2][y+2] == 'X' && a[x-3][y+3] == 'X') return 1;
	
	if(Tx != -1)
		a[Tx][Ty] = 'O';
	
	if(x + 3 < 4 && a[x][y] == 'O' && a[x+1][y] == 'O' && a[x+2][y] == 'O' && a[x+3][y] == 'O') return 2;
	if(y + 3 < 4 && a[x][y] == 'O' && a[x][y+1] == 'O' && a[x][y+2] == 'O' && a[x][y+3] == 'O') return 2;
	if(x + 3 < 4 && y + 3 < 4 && a[x][y] == 'O' && a[x+1][y+1] == 'O' && a[x+2][y+2] == 'O' && a[x+3][y+3] == 'O') return 2;
	if(x - 3 >= 0 && y + 3 < 4 && a[x][y] == 'O' && a[x-1][y+1] == 'O' && a[x-2][y+2] == 'O' && a[x-3][y+3] == 'O') return 2;

	return 0;
}

int main(void)
{
	int i,j,k;
	char ch;
	scanf(" %d",&T);
	for(i = 1; i <= T; i++)
	{
		dots = false;
		for(j=0;j<4;j++) scanf("%s",a[j]);
		scanf("%c",&ch);
		Tx = -1;
		Ty = -1;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(a[j][k]=='T')
				{
					Tx = j;
					Ty = k;
				}
			}
		}
		
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				int result = wins(j,k);
				if(result == 1)
				{
					printf("Case #%d: X won\n",i);
					goto here;
				}
				if(result == 2) 
				{
					printf("Case #%d: O won\n",i);
					goto here;
				}
			}
		}
		dots = false;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				if(a[j][k] == '.') dots = true;
			}
		}
		if(dots) printf("Case #%d: Game has not completed\n",i);
		else printf("Case #%d: Draw\n",i);
		here:;
	}
	return 0;
}
