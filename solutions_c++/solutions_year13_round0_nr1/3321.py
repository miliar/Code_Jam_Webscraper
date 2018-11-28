#include <iostream>
#include <cstdio>
using namespace std;

char dat[10][10];
bool checkX()
{
	for (int i = 0; i < 4; i++)
	{
		bool found = false;
		for (int j = 0; j < 4; j++)
			if (dat[i][j] != 'X' && dat[i][j] != 'T')
			{
				found = true;
				break;
			}
		if (!found) return true;
		
		found = false;
		for (int j = 0; j < 4; j++)
			if (dat[j][i] != 'X' && dat[j][i] != 'T')
			{
				found = true;
				break;
			}
		if (!found) return true;
	}
	
	bool found = false;
	for (int i = 0; i < 4; i++)
		if (dat[i][i] != 'X' && dat[i][i] != 'T')
		{
			found = true;
			break;
		}
	if (!found) return true;
	
	found = false;
	for (int i = 0; i < 4; i++)
		if (dat[i][3 - i] != 'X' && dat[i][3 - i] != 'T')
		{
			found = true;
			break;
		}
	if (!found) return true;
	
	return false;
}

bool checkfull()
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (dat[i][j] == '.') return false;
	return true;
}

void reverse()
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (dat[i][j] == 'X') dat[i][j] = 'O';
			else if (dat[i][j] == 'O') dat[i][j] = 'X';
}

void init()
{
	for (int i = 0; i < 4; i++) scanf("%s", dat[i]);
}

void work()
{
	if (checkX()) printf("X won\n");
	else
	{
		reverse();
		if (checkX()) printf("O won\n");
		else if (checkfull()) printf("Draw\n");
		else printf("Game has not completed\n");
	}
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		init();
		printf("Case #%d: ", i);
		work();
	}
	return 0;
}
