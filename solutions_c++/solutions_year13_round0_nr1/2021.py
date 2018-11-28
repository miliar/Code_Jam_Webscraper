#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

char str[15];
char maze[15][15];

int chkrow(int x)
{
	int i, ret;
	char ch = 'a';
	for(i = 0; i < 4; i++)
	{
		if(maze[x][i] == 'X')
		{
			ret = 1;
			ch = 'X';
			break;
		}
		if(maze[x][i] == 'O')
		{
			ret = 2;
			ch = 'O';
			break;
		}
	}
	for(i = 0; i < 4; i++)
	{
		if(maze[x][i] == 'T')
			continue;
		if(maze[x][i] != ch)
			return 0;
	}
	return ret;
}

int chkcol(int x)
{
	int i, ret;
	char ch = 'a';
	for(i = 0; i < 4; i++)
	{
		if(maze[i][x] == 'X')
		{
			ret = 1;
			ch = 'X';
			break;
		}
		if(maze[i][x] == 'O')
		{
			ret = 2;
			ch = 'O';
			break;
		}
	}
	for(i = 0; i < 4; i++)
	{
		if(maze[i][x] == 'T')
			continue;
		if(maze[i][x] != ch)
			return 0;
	}
	return ret;
}

int chkdiag1()
{
	int i, j, ret;
	char ch = 'a';
	for(i = 0, j = 0; i < 4; i++, j++)
	{
		if(maze[i][j] == 'X')
		{
			ret = 1;
			ch = 'X';
			break;
		}
		if(maze[i][j] == 'O')
		{
			ret = 2;
			ch = 'O';
			break;
		}
	}

	for(i = 0, j = 0; i < 4; i++, j++)
	{
		if(maze[i][j] == 'T')
			continue;
		if(maze[i][j] != ch)
			return 0;
	}

	return ret;

}

int chkdiag2()
{
	int i, j, ret;
	char ch = 'a';
	for(i = 3, j = 0; j < 4; i--, j++)
	{
		if(maze[i][j] == 'X')
		{
			ret = 1;
			ch = 'X';
			break;
		}
		if(maze[i][j] == 'O')
		{
			ret = 2;
			ch = 'O';
			break;
		}
	}

	for(i = 3, j = 0; j < 4; i--, j++)
	{
		if(maze[i][j] == 'T')
			continue;
		if(maze[i][j] != ch)
			return 0;
	}

	return ret;

}

bool isempty()
{
	int i, j;
	for(i = 0; i < 4; i++)
	{
		for(j = 0; j < 4; j++)
		{
			if(maze[i][j] == '.')
				return true;
		}
	}
	return false;
}


int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int inp, kase, i, j, k;
	scanf("%d", &inp);
	for(kase = 1; kase <= inp; kase++)
	{
		gets(str);
		for(i = 0; i < 4; i++)
		{
			gets(maze[i]);
		}
		printf("Case #%d: ", kase);
		for(i = 0; i < 4; i++)
		{
			j = chkrow(i);
			if(j > 0)
				break;
			j = chkcol(i);
			if(j > 0)
				break;
		}
		if(j == 0)
		{
			j = chkdiag1();
			if(j == 0)
				j = chkdiag2();
		}
		if(j == 0)
		{
			if(isempty())
			{
				printf("Game has not completed\n");
			}
			else
			{
				printf("Draw\n");
			}
		}
		else if(j == 1)
		{
			printf("X won\n");
		}
		else
		{
			printf("O won\n");
		}
	}

	return 0;
}