#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 600;

int M, N;

char szHex[MAX][MAX];
int chess[MAX][MAX];
int cut[MAX];

int subchess[MAX][MAX][3];

int cov[5];

void Convert( char a )
{
	int val;
	if( a >='0' && a <= '9' )
	{
		val = a - '0';
	}
	else if( a >= 'A' && a <= 'F' )
	{
		val = 10 + a - 'A';
	}
	cov[1] = (val & 8)? 1:0;
	cov[2] = (val & 4)? 1:0;
	cov[3] = (val & 2)? 1:0;
	cov[4] = (val & 1)? 1:0;
}

int main()
{
	freopen( "C-large.in", "r", stdin );
	freopen( "C-large.txt", "w", stdout );

	int cas;
	scanf( "%d", &cas );
	for( int iCas = 1; iCas <= cas; ++iCas )
	{
		int i, j, k;
		scanf( "%d%d", &M, &N );
		for( i = 1; i <= M; ++i )
		{
			scanf( "%s", szHex[i] );
		}
		for( i = 1; i <= M; ++i )
		{
			for( j = 0; j < N/4; ++j )
			{
				Convert( szHex[i][j] );
				for( k = 1; k <= 4; ++k )
				{
					chess[i][4*j+k] = cov[k];
				}
			}
		}
		for( j = 0; j <= N; ++j )
		{
			chess[0][j] = 3;
			chess[j][0] = 3;
			subchess[0][j][0] = subchess[0][j][1] = subchess[0][j][2] = 0;
			subchess[j][0][0] = subchess[j][0][1] = subchess[j][0][2] = 0;
		}
		for( i = 1; i <= M; ++i )
		{
			for( j = 1; j <= N; ++j )
			{
				if( chess[i][j] - chess[i][j-1] == 1 || chess[i][j-1] - chess[i][j] == 1 )
				{
					subchess[i][j][2] = subchess[i][j-1][2]+1;
				}
				else
				{
					subchess[i][j][2] = 1;
				}
				if( chess[i][j] - chess[i-1][j] == 1 || chess[i-1][j] - chess[i][j] == 1 )
				{
					subchess[i][j][1] = subchess[i-1][j][1]+1;
				}
				else
				{
					subchess[i][j][1] = 1;
				}
				if( subchess[i][j][1] != 1 && subchess[i][j][2] != 1 &&
					chess[i][j] - chess[i-1][j-1] == 0 )
				{
					subchess[i][j][0] = min( subchess[i-1][j-1][0]+1, min( subchess[i][j][1], subchess[i][j][2] ) ); 
				}
				else
				{
					subchess[i][j][0] = 1;
				}
			}
		}
		int iMax = 0;
		for( i = 0; i < MAX; ++i )
		{
			cut[i] = 0;
		}
		int ct = M*N;
		//debug
		int cntlp = 1;
		while( 1 )
		{
			iMax = 1;
			int p1, p2;
			for( i = 1; i <= M; ++i )
			{
				for( j = 1; j <= N; ++j )
				{
					if( subchess[i][j][0] > iMax && chess[i][j] != 3 )
					{
						if( chess[i][j-subchess[i][j][0]+1] != 3 &&
							chess[i-subchess[i][j][0]+1][j] != 3 &&
							chess[i-subchess[i][j][0]+1][j-subchess[i][j][0]+1] != 3 )
						{
							iMax = subchess[i][j][0];
							p1 = i;
							p2 = j;
						}
					}
				}
			}
			if( iMax == 1 )
			{
				cut[1] += ct;
				break;
			}
			else
			{
				++cut[iMax];
				for( i = p1-subchess[p1][p2][0]+1; i <= p1; ++i )
				{
					for( j = p2-subchess[p1][p2][0]+1; j <= p2; ++j )
					{
						chess[i][j] = 3;
					}
				}
				ct -= subchess[p1][p2][0]*subchess[p1][p2][0];
			}
			for( i = 1; i <= M; ++i )
			{
				for( j = 1; j <= N; ++j )
				{
					if( chess[i][j] == 3 )
					{
						subchess[i][j][0] = subchess[i][j][1] = subchess[i][j][2] = 0;
						continue;
					}
					if( chess[i][j] - chess[i][j-1] == 1 || chess[i][j-1] - chess[i][j] == 1 )
					{
						subchess[i][j][2] = subchess[i][j-1][2]+1;
					}
					else
					{
						subchess[i][j][2] = 1;
					}
					if( chess[i][j] - chess[i-1][j] == 1 || chess[i-1][j] - chess[i][j] == 1 )
					{
						subchess[i][j][1] = subchess[i-1][j][1]+1;
					}
					else
					{
						subchess[i][j][1] = 1;
					}
					if( subchess[i][j][1] != 1 && subchess[i][j][2] != 1 &&
						chess[i][j] - chess[i-1][j-1] == 0 )
					{
						subchess[i][j][0] = min( subchess[i-1][j-1][0]+1, min( subchess[i][j][1], subchess[i][j][2] ) ); 
					}
					else
					{
						subchess[i][j][0] = 1;
					}
				}
			}
			//debug
		/*	int cnt = 0;
			for( i = 1; i <= M; ++i )
			{
				for( j = 1; j <= N; ++j )
				{
					if( chess[i][j] != 3 )
					{
						++cnt;
					}
				}
			}
			printf( "%d %d %d\n", cntlp++, iMax, cnt );*/
		}
		int iDif = 0;
		for( i = 1; i < MAX; ++i )
		{
			if( cut[i] != 0 )
			{
				++iDif;
			}
		}
		printf( "Case #%d: %d\n", iCas, iDif ); 
		for( i = MAX-1; i > 0; --i )
		{
			if( cut[i] != 0 )
			{
				printf( "%d %d\n", i, cut[i] );
			}
		}


	}

	return 0;
}