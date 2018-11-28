#include <cstdio>
#include <cstdlib>

char charTable[4][5];

void loadMatrix()
{
	for(int i = 0; i < 4; i++)
		scanf("%s",charTable[i]);
}

int check(int x, int y, int xdiff, int ydiff, bool & emptyBox)
{
	int player = 0;
	for(int i = 0; i < 4; i++)
	{
		if (charTable[x][y] == '.')
		{
			emptyBox = true;
			return 0;
		}
		else if (charTable[x][y] == 'O')
		{
			if (player == 2 || player == 3)
				player = 3;
			else
				player = 1;
		}
		else if (charTable[x][y] == 'X')
		{
			if (player == 1 || player == 3)
				player = 3;
			else
				player = 2;
		}
		x += xdiff;
		y += ydiff;
	}
	if (player == 3)
		return 0;
	else
		return player;
}

void printResult(int result, bool emptyBox, int caseNumber)
{
	if (result == 0)
	{
		if(emptyBox)
			printf("Case #%d: Game has not completed\n",caseNumber);
		else
			printf("Case #%d: Draw\n",caseNumber);
	}
	else if (result == 1)
	{
		printf("Case #%d: O won\n",caseNumber);
	}
	else
	{
		printf("Case #%d: X won\n",caseNumber);
	}
}

void doCase(int caseNumber)
{
	loadMatrix();
	bool emptyBox = false;
	int result;
	
	for(int i = 0; i < 4; i++)
	{
		result = check(0,i,1,0,emptyBox);
		if (result)
		{
			printResult(result,emptyBox,caseNumber);
			return;
		}
	}
	for(int i = 0; i < 4; i++)
	{
		result = check(i,0,0,1,emptyBox);
		if (result)
		{
			printResult(result,emptyBox,caseNumber);
			return;
		}
	}
	result = check(0,0,1,1,emptyBox);
	if (result)
	{
		printResult(result,emptyBox,caseNumber);
		return;
	}
	result = check(3,0,-1,1,emptyBox);
	printResult(result,emptyBox,caseNumber);
}

int main(int argc, char const *argv[])
{
	int testCases;
	scanf("%d",&testCases);

	for(int i = 0; i < testCases; i++)
		doCase(i+1);

	return 0;
}
