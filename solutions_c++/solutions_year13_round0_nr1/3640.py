#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
using namespace std;

char matrix[4][5];
void Calculate(int testCase);
char win(char a, char b, char c, char d); // 1 X win, -1 O win, 0 tie
bool isFinished;

int main(void)
{
	freopen("A-small.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int nTest;

	scanf("%d", &nTest);
	for (int i = 0; i < nTest ; i++)
	{
		isFinished = true;
		for (int j = 0; j < 4 ; j++)
		{
			scanf("%s", matrix[j]);
			if(
				 (matrix[j][0] == '.')  ||
				 (matrix[j][1] == '.') ||
				 (matrix[j][2] == '.') ||
				 (matrix[j][3] == '.')
				 )
			{
				isFinished = false;
			}
		}
		Calculate(i+1);
	}

	return 1;
}

void Calculate( int testCase )
{
	for (int i = 0; i < 4 ; i++)
	{
		char res = win(matrix[i][0],matrix[i][1], matrix[i][2],matrix[i][3]);
		if (res != 0)
		{
			printf("Case #%d: %c won\n", testCase, res);
			return;
		}

	}
	for (int i = 0; i < 4 ; i++)
	{
		char res = win(matrix[0][i],matrix[1][i], matrix[2][i],matrix[3][i]);
		if (res != 0)
		{
			printf("Case #%d: %c won\n", testCase, res);
			return;
		}
	}
	char res = win(matrix[0][0],matrix[1][1], matrix[2][2],matrix[3][3]);
	if (res != 0)
	{
		printf("Case #%d: %c won\n", testCase, res);
		return;
	}

	res = win(matrix[0][3],matrix[1][2], matrix[2][1],matrix[3][0]);
	if (res != 0)
	{
		printf("Case #%d: %c won\n", testCase, res);
		return;
	}
	else
	{
		if (isFinished)
		{
			printf("Case #%d: Draw\n", testCase);
			return;
		}
		else
		{
			printf("Case #%d: Game has not completed\n", testCase);
			return;
		}
	}

}

char win( char a, char b, char c, char d )
{
	int result = 0;
	char para[4]={a,b,c,d};
	for (int i = 0; i <4  ; i++)
	{
		switch (para[i])
		{
			case 'X': result+=10; break;
			case 'O': result+=1; break;
			case 'T':  break;
			case '.': return 0;
		}
	}
	if ((result == 30) || (result == 40))
	{
		return 'X';
	}
	else if ((result == 3) || (result == 4))
	{
		return 'O';
	}
	else
		return 0;
}
