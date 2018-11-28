#include <cstdio>
#include <cstring>

int R, C;
char m[100][100];
int memo[12][ 1 << 12 ];

int prest[100];

int BitCount(int x)
{
	int res = 0;
	while( x )
	{
		res++;
		x &= x-1;
	}
	return res;
}

int go(int x, int st)
{
	//printf("%d %d\n", x, st);
	if( x == -1 )
		return 0;
	if( memo[x][st] != -1 )
		return memo[x][st];

	int best = 0;
	for(int i = 0; i < (1 << C); i++)
	{
		if( i & st )
			continue;

		//printf("%d %d -- %d\n", x, st, i);
		bool ok = true;
		for(int j = 0; j < C-1; j++)
			if( (i & ( 1 << j )) && (i & ( 1 << (j+1) )) )
			{
				ok = false;
				break;
			}
		if( !ok )
			continue;

		int count = BitCount( i );

		int mask = 0;
		for(int j = 0; j < C; j++)
		{
			if( i & ( 1 << j ) )
			{
				if( j > 0 )
					mask |= 1 << (j-1);
				if( j < C-1 )
					mask |= 1 << (j+1);
			}
		}

		int aux = count + go( x-1, mask | prest[x-1] );
		if( aux > best )
			best = aux;
	}
	return memo[x][st] = best;
}

int main()
{
	int K;
	scanf("%d", &K);
	for(int k = 1; k <= K; k++)
	{
		printf("Case #%d: ", k);
		scanf("%d %d", &R, &C);

		for(int i = 0; i < R; i++)
			scanf("%s", m[i]);

		memset( memo, -1, sizeof(memo) );
		memset( prest, 0, sizeof(prest) );
		for(int i = 0; i < R; i++)
		{
			for(int j = 0; j < C; j++)
				if( m[i][j] == 'x' )
					prest[i] |= (1 << j);
		}

		printf("%d\n", go(R-1, prest[R-1]) );
	}
}