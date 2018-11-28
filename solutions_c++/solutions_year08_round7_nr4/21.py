#include <cstdio>
#include <cstring>

int R, C;
int memo[1 << 16][4][4];
int dx[8] = {-1,-1,-1,0,0,1,1,1};
int dy[8] = {-1,0,1,-1,1,-1,0,1};


int good(int mask, int x, int y )
{
	bool b = x >= 0 && x < R && y >= 0 && y < C;
	if( b && !( mask & ( 1 << ( C*(R-1-x)+C-1-y )) ) )
		return 1;
	return 0;
}

void Print( int mask, int x, int y)
{
	printf("m = %d\n", mask);
	for(int i = 0; i < R; i++,printf("\n"))
		for(int j = 0; j < C; j++)
			if( i == x && j == y )
				printf("K");
			else if( mask & ( 1 << ( C*(R-1-i)+C-1-j ) ) )
				printf("#");
			else
				printf(".");

}

int go( int mask, int x, int y )
{
	if( memo[mask][x][y] != -1 )
		return memo[mask][x][y];
	
	mask |= 1 << ( C*(R-1-x)+C-1-y );
	//Print(mask, x, y);
	int res = 0;
	for(int i = 0; i < 8; i++)
		if( good( mask, x+dx[i], y+dy[i] ) )
			res |= !go( mask, x+dx[i], y+dy[i] );

	return memo[mask][x][y] = res;
}

int main()
{
	int K;
	scanf("%d", &K);
	for(int k = 1; k <= K; k++)
	{		
		scanf("%d %d", &R, &C);
		memset( memo, -1, sizeof(memo) );
		int mask = 0;
		int iR, iC;
		for(int i = 0; i < R; i++)
		{
			char s[100];
			scanf("%s", s);
			for(int j = 0; j < C; j++)
			{
				mask <<= 1;
				if( s[j] == '.' )
					continue;
				if( s[j] == 'K' )
				{
					iR = i;
					iC = j;
				}
				else
					mask |= 1;
			}
		}
		//printf("mask = %d\n", mask);
		printf("Case #%d: %c\n" , k, go(mask, iR, iC) ? 'A' : 'B' );
	}
}