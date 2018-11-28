#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

void solve()
{
	int i,j,k,l,flag = 1,xflag = 0,oflag = 0;
	char CHESS[4][4];

	getchar();
	for (i = 0 ; i < 4 ;i++)
	{
		for(j = 0 ; j < 4 ; j++)
		{
			scanf("%c",&CHESS[i][j]);
			if (CHESS[i][j] == '.') flag = 0;
		}
		getchar();
	}
	for (i = 0; i < 4 ; i++)
		for ( j = 0 ; j < 4 ; j++)
		{
			if ((CHESS[i][j] == '.') ||(CHESS[i][j] == 'T'))  continue;
			if (CHESS[i][j] == 'O')
			{
				for (k = 1 ;k <= 3; k++)
				{
					if (CHESS[i][(j+k)%4] == 'X' || CHESS[i][(j+k)%4] == '.') break;
				}
				for (l = 1 ;l <= 3; l++)
				{
					if (CHESS[(i+l)%4][j] == 'X' || CHESS[(i+l)%4][j] == '.') break;
				}
				if (k == 4 || l == 4) oflag = 1;
			}
			else if (CHESS[i][j] == 'X')
			{
				for (k = 1 ;k <= 3; k++)
				{
					if (CHESS[i][(j+k)%4] == 'O' || CHESS[i][(j+k)%4] == '.') break;
				}
				for (l = 1 ;l <= 3; l++)
				{
					if (CHESS[(i+l)%4][j] == 'O' || CHESS[(i+l)%4][j] == '.') break;
				}
				if (k == 4 || l == 4) xflag = 1;
			}
		}
	for (i = 0 ; i < 4 ; i ++)
	{
		if(CHESS[i][i] == 'O' || CHESS[i][i] == '.') break;
	}
	if (i == 4) xflag = 1;
	for (i = 0 ; i < 4 ; i ++)
	{
		if(CHESS[i][3-i] == 'O' || CHESS[i][3-i] == '.') break;
	}
	if (i == 4) xflag = 1;
	for (i = 0 ; i < 4 ; i ++)
	{
		if(CHESS[i][i] == 'X' || CHESS[i][i] == '.') break;
	}
	if (i == 4) oflag = 1;
	for (i = 0 ; i < 4 ; i ++)
	{
		if(CHESS[i][3-i] == 'X' || CHESS[i][3-i] == '.') break;
	}
	if (i == 4) oflag = 1;
	if (xflag == 1)
	{
		printf("X won\n");	
	}
	else if(oflag == 1)
	{
		printf("O won\n");
	}
	else if(flag == 1)
	{
		printf("Draw\n");
	}
	else if (flag == 0)
	{
		printf("Game has not completed\n");
	}
}

int main()
{
	int T;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	scanf("%d",&T);
	for (int t = 1 ; t <= T ;t++)
	{
		printf("Case #%d: ",t);
		solve();
	}
return 0;
}