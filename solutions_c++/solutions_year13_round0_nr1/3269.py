#include <cstdio>
#include <cctype>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cmath>
#include <stack>
#include <string>     
#include <map>
#include <set>
#include <list>
#include <queue>
#include <utility>

#define SIZE 5005
#define INT_MAX 2000000000
#define MOD 20071027
#define clr(a) memset(a, 0, sizeof a)
#define reset(a) memset(a, -1, sizeof a)

#define BOUNDARY(i, j) ((i >= 0 && i < row) && (j >= 0 && j < column))

#define max3(x, y, z) max(max(x, y), max(y, z)) 

using namespace std;

int n, m, row, column;

char grid[4][5];

bool test(char c)
{
	int i, j;

	for(i = 0; i < 4; i++)
	{
		for(j = 0; j < 4; j++)
			if(grid[i][j] != c && grid[i][j] != 'T')
				break;
		if(j == 4) return true;
	}

	for(i = 0; i < 4; i++)
	{
		for(j = 0; j < 4; j++)
			if(grid[j][i] != c && grid[j][i] != 'T')
				break;
		if(j == 4) return true;
	}

	for(i = 0; i < 4; i++)
		if(grid[i][i] != c && grid[i][i] != 'T')
			break;
	if(i == 4) return true;

	for(i = 0; i < 4; i++)
		if(grid[i][3-i] != c && grid[i][3-i] != 'T')
			break;
	if(i == 4) return true;

	return false;
}

bool isOver()
{
	for(int i = 0;  i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(grid[i][j] == '.') return false;
	return true;
}

int main()
{	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int i, j, k, l;
	int x, y;
	int tc, t;
	int res = 0;
	
	scanf("%d", &tc);

	for(t = 1; t <= tc; t++)
	{
		getchar();
		for(i = 0; i < 4; i++)
			gets(grid[i]);

		printf("Case #%d: ", t);
		if(test('O')) puts("O won");
		else if(test('X')) puts("X won");
		else if(isOver()) puts("Draw");
		else puts("Game has not completed");
	}
			
	return 0;
}