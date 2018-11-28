#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <algorithm>
 
using namespace std;

#define MAXN 512

int M, N;
unsigned char grid[MAXN][MAXN];

char buffer[600];

inline int ascii2bin(char c)
{
	c = toupper(c);

	if (c>='A')
		return c-'A'+10;
	else
		return c-'0';
}

bool get_input()
{
	static int T = -1;
	
	if (T<0)
		scanf("%d", &T);
	
	if (T>0)
	{
		--T;

		if (scanf("%d %d", &M, &N)!=2)
			return false;

		while(fgetc(stdin)!='\n') ;

		for(int i=0; i<M; ++i)
		{
			fgets(buffer, 550, stdin);
			for(int j=0; j<N/4; ++j)
			{
				int h = ascii2bin(buffer[j]);
				grid[i][j*4] = h>>3;
				grid[i][j*4+1] = (h>>2)&1;
				grid[i][j*4+2] = (h>>1)&1;
				grid[i][j*4+3] = h&1;
			}
		}

		return true;
	}
	else
		return false;
}

int boards[600];

inline void checkAndExtract(int y, int x, int size)
{
	unsigned char check = grid[y][x] ^ 1;
	if (y+size>M || x+size>N) return;
	for(int i=y; i<y+size; ++i)
	{
		for(int j=x; j<x+size; ++j)
		{
			if (grid[i][j]==check || (grid[i][j]&64))
				return;
			check ^= 1;
		}
		check ^= ((~size) & 1);
	}

	// we have a board now, cut it out
	for(int i=y; i<y+size; ++i)
	{
		for(int j=x; j<x+size; ++j)
			grid[i][j] = 64;
	}

	boards[size]++;
}

int main()
{
	for(int ncase=1; get_input(); ++ncase)
	{
		//fprintf(stderr, "\nCase #%d\n", ncase); fflush(stderr);
		printf("Case #%d: ", ncase);

		for(int i=0; i<=550; ++i)
			boards[i] = 0;

		//if (ncase==1) continue;
		/*printf("\n");
		for(int i=0; i<M; ++i)
		{
			for(int j=0; j<N; ++j)
				printf("%c", (grid[i][j])?'*':'.');
			printf("\n");
		}
		printf("\n"); /**/


		for(int size=((M>N)?N:M); size>=2; --size)
		{
			for(int i=0; i<M; ++i)
			{
				for(int j=0; j<N; ++j)
				{
					checkAndExtract(i,j,size);
				}
			}
		}

		int area=M*N;
		int nres=0;
		for(int k=MAXN; k>=2; --k)
		{
			if (boards[k]>0) nres++;
			area -= boards[k]*k*k;
		}

		if (area>0) nres++;
		printf("%d\n", nres);
		for(int k=MAXN; k>=2; --k)
		{
			if (boards[k]>0)
				printf("%d %d\n", k, boards[k]);
		}
		if (area>0)
			printf("1 %d\n", area);

	}

	return 0;
}