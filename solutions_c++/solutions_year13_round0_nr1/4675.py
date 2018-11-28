#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <stdio.h>
//#include <math.h>

using namespace std;

typedef pair<int, int>  pii;

#define LS <
#define Size(x) (int(x.size()))

#define FOR(k,a,b) for(int k=(a); k LS (b); ++k)

char table[4][5];

int check(int sum)
{
	if (sum == 316 || sum == 321) return 'O';
	if (sum == 352 || sum == 348) return 'X';
	return 0;
}

int checkColumn(int col)
{
	int sum = table[0][col];
	FOR(i,1,4) sum += table[i][col];
	return check(sum);
}

int checkRow(int row)
{
	int sum = table[row][0];
	FOR(i,1,4) sum += table[row][i];
	return check(sum);
}

void solveCase()
{
	scanf("%s",table[0]);
	scanf("%s",table[1]);
	scanf("%s",table[2]);
	scanf("%s",table[3]);
	
	// check rows and columns
	int res;
	FOR(i, 0, 4)
	{
		res = checkRow(i);
		if (res == 'X' || res == 'O')
		{
			printf("%c won\n", res);
			return;
		}
		
		res = checkColumn(i);
		if (res == 'X' || res == 'O')
		{
			printf("%c won\n", res);
			return;
		}
	}

	// check diagonals
	int sum = table[0][0];
	FOR(i,1,4) sum += table[i][i];
	res = check(sum);
	if (res == 'X' || res == 'O')
	{
		printf("%c won\n", res);
		return;
	}

	sum = table[0][3];
	FOR(i,1,4) sum += table[i][3-i];
	res = check(sum);
	if (res == 'X' || res == 'O')
	{
		printf("%c won\n", res);
		return;
	}

	FOR(i, 0, 4)
	{
		FOR(j, 0, 4)
		{
			if (table[i][j] == '.')
			{
				printf("Game has not completed\n");
				return;
			}
		}
	}

	printf("Draw\n");
}

int main() 
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int T;
	scanf("%d",&T);
	FOR(_t, 0, T)
	{
		printf("Case #%d: ",_t+1);
		solveCase();
	}
	return 0;
}