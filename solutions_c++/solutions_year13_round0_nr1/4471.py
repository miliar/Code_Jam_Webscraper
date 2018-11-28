#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <algorithm>
using namespace std;

char str[10][10];

bool check(int x, int y, int dx, int dy, int fx, int fy)
{
	char c = str[x][y];
	int cntc = 1, cntt = 0;
	for (int i = 1; i < 4; i++)
	{
		int tx = x + dx * i;
		int ty = y + dy * i;
		if (tx < 0 || ty < 0 || tx >= 4 || ty >= 4)
			break;
		if (str[tx][ty] == '.')
			break;
		if (str[tx][ty] == 'T')
		{
			if (cntt == 1)
				break;
			cntt++;
		}
		else if (str[tx][ty] == c)
			cntc++;
		else
			break;
	}
	for (int i = 1; i < 4; i++)
	{
		int tx = x + fx * i;
		int ty = y + fy * i;
		if (tx < 0 || ty < 0 || tx >= 4 || ty >= 4)
			break;
		if (str[tx][ty] == '.')
			break;
		if (str[tx][ty] == 'T')
		{
			if (cntt == 1)
				break;
			cntt++;
		}
		else if (str[tx][ty] == c)
			cntc++;
		else
			break;
	}
	if (cntc >= 4 || (cntc == 3 && cntt == 1))
		return true;
	return false;
}

bool check(int x, int y)
{
	if (check(x, y, 1, 0, -1, 0))
		return true;
	if (check(x, y, 0, 1, 0, -1))
		return true;
	if (check(x, y, -1, -1, 1, 1))
		return true;
	if (check(x, y, -1, 1, 1, -1))
		return true;
	return false;
}

void solved(int cas)
{
	printf ("Case #%d: ", cas);
	for (int i = 0; i < 4; i++)
		scanf ("%s", str[i]);
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (str[i][j] != '.' && str[i][j] != 'T' && check(i, j))
			{
				printf ("%c won\n", str[i][j]);
				return ;
			}
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (str[i][j] == '.')
			{
				printf ("Game has not completed\n");
				return ;
			}
	printf ("Draw\n");
	return ;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf ("%d", &T);
	for (int i = 1; i <= T; i++)
		solved(i);
	return 0;
}