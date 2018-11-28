#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifdef USE_TESTING_SYSTEM
#include "TestHelpers.h"
PROBLEM_BEGIN(99902,"Code Jam 02")
#endif

const int MAX_SIZE = 100+2;
int Height[MAX_SIZE][MAX_SIZE];
char Val[MAX_SIZE][MAX_SIZE];

const int MAX_HEIGHT = 99999;
char NextBaisin;
void Prepare(int H, int W)
{
	for(int i=0; i <= W+1; i++)
		Height[0][i] = Height[H+1][i] = MAX_HEIGHT;
	for(int i=0; i <= H+1; i++)
		Height[i][0] = Height[i][W+1] = MAX_HEIGHT;

	for(int i=1; i <= H; i++)
	{
		for(int j=1; j <= W; j++)
		{
			Val[i][j] = '*';
		}
	}
	NextBaisin = 'a';
}

char Check(int i, int j)
{
	if( Val[i][j] != '*') return Val[i][j];
	static int D[4][2] =
	{
		{-1,0},
		{0,-1},
		{0,1},
		{1,0},
	};
	int minHeight = Height[i][j];
	int best = -1;
	for(int k=0; k < 4; k++)
	{
		if( minHeight > Height[i+D[k][0]][j+D[k][1]])
		{
			minHeight = Height[i+D[k][0]][j+D[k][1]];
			best = k;
		}
	}
	if( best != -1)
	{
		Val[i][j] = Check(i+D[best][0], j+D[best][1]);
	}
	else
	{
		Val[i][j] = NextBaisin;
		NextBaisin++;
	}
	return Val[i][j];
}


#ifdef USE_TESTING_SYSTEM
TESTING_FUNCTION()
#else
int main()
#endif
{
	int T;
	scanf("%i", &T);
	for(int sample=1; sample <= T; sample++)
	{
		int W, H;
		scanf("%i %i", &H, &W);
		Prepare(H, W);
		for(int i=1; i <= H; i++)
		{
			for(int j=1; j <= W; j++)
			{
				scanf("%i", &Height[i][j]);
			}
		}
		
		for(int i=1; i <= H; i++)
		{
			for(int j=1; j <= W; j++)
			{
				Check(i,j);
			}
		}

		printf("Case #%i:\n", sample);
		for(int i=1; i <= H; i++)
		{
			for(int j=1; j <= W; j++)
			{
				printf("%c ", Val[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}
#ifdef USE_TESTING_SYSTEM
PROBLEM_END()
#endif