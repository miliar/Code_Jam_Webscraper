#include <cstdio>
#include <cstring>

int MAP[ 102 ][ 102 ];
int ANS[ 102 ][ 102 ];


int DX[] = { 0, -1, 1, 0 };
int DY[] = { -1, 0, 0, 1 };

char SERIAL;
int X, Y;

char label( int x, int y )
{
	if( ANS[x][y] != 0 )
		return ANS[x][y];
	int min=MAP[x][y], mini=-1;
	for( int i=0;i<4;i++ )
		if( min > MAP[ x + DX[i] ][ y + DY[i] ] ) {
			min = MAP[ x + DX[i] ][ y + DY[i] ];
			mini = i;
		}
	if( mini == -1 ) {
		return ANS[x][y] = SERIAL++;
	}
	return ANS[x][y] = label( x + DX[mini], y + DY[mini] );
}

int main()
{
	int ccN;
	scanf("%d",&ccN);
	for( int cc=0;cc<ccN;cc++ ) {
		for( int i=0;i<102;i++ )
			for( int j=0;j<102;j++ )
				MAP[i][j] = 100000000;
		memset( ANS, 0, sizeof(ANS) );
		SERIAL = 'a';
		scanf("%d%d", &Y, &X );
		for( int i=1;i<=Y;i++ )
			for( int j=1;j<=X;j++ )
				scanf("%d", &MAP[j][i] );
		for( int i=1;i<=Y;i++ )
			for( int j=1;j<=X;j++ )
				label( j, i );
		printf("Case #%d:\n", cc+1);
		for( int i=1;i<=Y;i++ ) {
			for( int j=1;j<=X;j++ )
				printf("%c ", ANS[j][i] );
			printf("\n");
		}
	}
}
