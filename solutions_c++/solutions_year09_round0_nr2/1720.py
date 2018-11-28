#include <stdio.h>
#include <string.h>

#define MAX_ALT 10001

class DisjSet
{
public:
	void Init( int n )
	{
		int i;
		num = n;
		for( i = 0; i < n; ++i )
			{
			set[i] = -1;
			}//end for
	}//end DisjSet

	void Union( int root1, int root2 )
	{
		if( set[root1] > set[root2] )
			{
			set[root1] = root2;
			}
		else{
			if( set[root1] == set[root2] )
				{
				--set[root1];
				}//end if
			set[root2] = root1;
			}//end if
	}//end Union

	int Find( int index )
	{
		while( set[index] >= 0 )
			{
			index = set[index];
			}//end while
		return index;
	}//end Find

private:
	int set[100*100];
	int num;
};

int alt[100][100];
int res[100][100];
char map[100*100];
DisjSet set;
DisjSet lbset;

int main()
{
	int t;
	int ti;
	int h, w;
	int i, j;
	int minalt, mini, minj;
	int r1, r2;
	int bid;
	char cid;

	freopen( "B.in", "r", stdin );
	freopen( "B.out", "w", stdout );

	for( ti = 1, scanf( "%d", &t ); ti <= t; ++ti )
		{
		scanf( "%d%d", &h, &w );
		for( i = 0; i < h; ++i )
			{
			for( j = 0; j < w; ++j )
				{
				scanf( "%d", &alt[i][j] );
				}//end for
			}//end for
		memset( res, -1, sizeof( res[0] ) * h );

		set.Init( h * w );
		lbset.Init( h * w );

		bid = 0;
		for( i = 0; i < h; ++i )
			{
			for( j = 0; j < w; ++j )
				{
				minalt = MAX_ALT;
				if( i > 0 && alt[i][j] > alt[i-1][j] )
					{
					if( minalt > alt[i-1][j] )
						{
						minalt = alt[i-1][j];
						mini = i-1;
						minj = j;
						}//end if
					}//end if
				if( j > 0 && alt[i][j] > alt[i][j-1] )
					{
					if( minalt > alt[i][j-1] )
						{
						minalt = alt[i][j-1];
						mini = i;
						minj = j-1;
						}//end if
					}//end if
				if( j + 1 < w && alt[i][j] > alt[i][j+1] )
					{
					if( minalt > alt[i][j+1] )
						{
						minalt = alt[i][j+1];
						mini = i;
						minj = j+1;
						}//end if
					}//end if
				if( i + 1 < h && alt[i][j] > alt[i+1][j] )
					{
					if( minalt > alt[i+1][j] )
						{
						minalt = alt[i+1][j];
						mini = i+1;
						minj = j;
						}//end if
					}//end if
				
				if( minalt < MAX_ALT )
					{
					r1 = set.Find( i * w + j );
					r2 = set.Find( mini * w + minj );
					if( r1 != r2 )
						{
						set.Union( r1, r2 );
						}//end if
					if( res[mini][minj] == -1 )
						{
						if( res[i][j] == -1 )
							{
							res[i][j] = bid++;
							}//end if
						res[mini][minj] = res[i][j];
						}
					else{
						if( res[i][j] == -1 )
							{
							res[i][j] = res[mini][minj];
							}
						else{
							if( res[i][j] != res[mini][minj] )
								{
								r1 = lbset.Find( res[i][j] );
								r2 = lbset.Find( res[mini][minj] );
								if( r1 != r2 )
									{
									lbset.Union( r1, r2 );
									}//end if
								}//end if
							}//end if
						}//end if
					}
				else{
					if( res[i][j] == -1 )
						{
						res[i][j] = bid++;
						}//end if
					}//end if
				}//end for
			}//end for

		cid = 'a';
		memset( map, -1, sizeof( map[0] ) * bid );
		for( i = 0; i < bid; ++i )
			{
			r1 = lbset.Find( i );
			if( r1 < 0 )
				{
				map[i] = cid++;
				}
			else{
				if( map[r1] < 0 )
					{
					map[r1] = cid++;
					}//end if
				map[i] = map[r1];
				}//end if
			}//end for

		printf( "Case #%d:\n", ti );
		for( i = 0; i < h; ++i )
			{
			putchar( map[res[i][0]] );
			for( j = 1; j < w; ++j )
				{
				putchar( ' ' );
				putchar( map[res[i][j]] );
				}//end for
			putchar( '\n' );
			}//end for
		}//end for

	return 0;
}