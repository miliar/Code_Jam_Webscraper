#include <stdio.h>
enum WhoWon{
	X_WON,
	O_WON,
	DRAW,
	NOT_COMPLETED
};
static const int prodX = 'X'*'X'*'X'*'X';
static const int prodXT = 'X'*'X'*'X'*'T';
static const int prodO = 'O'*'O'*'O'*'O';
static const int prodOT = 'O'*'O'*'O'*'T';
// static const int sum
WhoWon check(char arr[4][4])
{
	
	//Horizontal check;
	for (int i = 0; i < 4; ++i)
	{
		int prod = 1;
		for (int j = 0; j < 4; ++j)
		{
			prod *= arr[i][j];
		}
		if(prod == prodX || prod == prodXT)
			return X_WON;
		else if(prod == prodO || prod == prodOT)
			return O_WON;
	}
	//Verticial CHeck
	for (int j = 0; j < 4; ++j)
	{
		int prod=1;
		for (int i = 0; i < 4; ++i)
		{
			prod *= arr[i][j];
		}
		if(prod == prodX || prod == prodXT)
			return X_WON;
		else if(prod == prodO || prod == prodOT)
			return O_WON;
	}
	//Diagonal check
	//d1
	int prod = 1;
	for (int i = 0; i < 4; ++i)
	{
		prod *= arr[i][i];
	}
	if(prod == prodX || prod == prodXT)
		return X_WON;
	else if(prod == prodO || prod == prodOT)
		return O_WON;
	//d2
	prod = 1;
	for (int i = 0; i < 4; ++i)
	{
		prod *= arr[i][3-i];
	}
	if(prod == prodX || prod == prodXT)
		return X_WON;
	else if(prod == prodO || prod == prodOT)
		return O_WON;
	//check if unfinished
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if(arr[i][j] == '.')
				return NOT_COMPLETED;
		}
	}
	return DRAW;
}

int main(int argc, char const *argv[])
{
	int t=0;
	scanf("%d\n", &t);
	char *strArr[4] = {"X won\n", "O won\n", "Draw\n", "Game has not completed\n"};
	char arr[4][4];
	for (int idx = 0; idx < t; ++idx)
	{
		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				scanf("%c", &arr[i][j]);
			}
			scanf("%*c");
		}
		printf("Case #%d: %s", idx+1, strArr[check(arr)]);
		scanf("%*c");
	}
	return 0;
}