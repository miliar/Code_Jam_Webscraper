#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

char picture[100][100];

int R, C;


void init()
{
	R = C = 0;
	memset(picture, 0, sizeof(picture));
}

bool isConvertable(int x, int y)
{
	if( x + 1 < R && y + 1 <  C )
	{
		for(int i = x; i <= x + 1; i++)
		{
			for(int j = y; j <= y + 1; j++)
			{
				if( '#' != picture[i][j]  )
				{
					return false;
				}
			}
		}
	}
	else
	{
		return false;
	}

	return true;
}


void convert(int x, int y)
{
	picture[x][y] = picture[x+1][y+1] = '/';
	picture[x+1][y] = picture[x][y+1] = '\\';
}

bool isContains()
{
	for(int i = 0; i < R; i++)
	{
		for(int j = 0; j < C; j++)
		{
			if( '#' == picture[i][j] )
			{
				return true;
			}
		}
	}

	return false;
}


int main()
{

	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int testNum= 0;
	scanf("%d", &testNum);

	for(int tc = 1; tc <= testNum; tc++)
	{
		init();
		scanf("%d%d", &R, &C);

		for(int i = 0; i < R; i++)
		{
			scanf("%s", picture[i]);
		}

		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
			{
				if( isConvertable(i, j) )
				{
					convert(i, j);
				}
			}
		}


		printf("Case #%d:\n", tc);
		if( isContains() )
		{
			cout << "Impossible" << endl;
		}
		else
		{
			for(int i = 0; i < R; i++)
			{
				for(int j = 0; j < C; j++)
				{
					printf("%c", picture[i][j]);
				}
				printf("\n");
			}
		}

	}



	return 0;
}