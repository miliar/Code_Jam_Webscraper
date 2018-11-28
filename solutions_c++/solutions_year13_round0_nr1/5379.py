#include <stdio.h>

char tab[5][5];
bool winO, winX;

int verifyRow(int i)
{
	char result = tab[i][0];
	
	for(int j=0; j<4; j++)
		if(tab[i][j] != tab[i][0] && tab[i][j] != 'T')
			result = '.';
	
	return result;
}

int verifyCol(int j)
{
	char result = tab[0][j];
	
	for(int i=0; i<4; i++)
		if(tab[i][j] != tab[0][j] && tab[i][j] != 'T')
			result = '.';
	
	return result;
}

int verifyDiagP()
{
	char result = tab[0][0];
	
	for(int i=0; i<4; i++)
		if(tab[i][i] != tab[0][0] && tab[i][i] != 'T')
			result = '.';
	
	return result;
}

int verifyDiagS()
{
	char result = tab[0][3];
	
	for(int i=0; i<4; i++)
		if(tab[i][3-i] != tab[0][3] && tab[i][3-i] != 'T')
			result = '.';
	
	return result;
}

void updateResult(char result)
{
	if(result == 'X')
		winX = true;
	else if(result == 'O')
		winO = true;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	
	int n;
	scanf(" %d", &n);
	for(int k=1; k<=n; k++)
	{
		winO = false;
		winX = false;
		
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				scanf(" %c", &tab[i][j]);
		
		for(int i=0; i<4; i++)
		{
			updateResult(verifyRow(i));
			updateResult(verifyCol(i));
		}
		updateResult(verifyDiagP());
		updateResult(verifyDiagS());
		
		if(winX && winO)
			printf("Case #%d: Draw\n", k);
		else if(winX)
			printf("Case #%d: X won\n", k);
		else if(winO)
			printf("Case #%d: O won\n", k);
		else
		{
			bool isOver = true;
			
			for(int i=0; i<4; i++)
				for(int j=0; j<4; j++)
					if(tab[i][j] == '.')
						isOver = false;
			
			if(isOver)
				printf("Case #%d: Draw\n", k);
			else
				printf("Case #%d: Game has not completed\n", k);
		}
	}
	return 0;
}
