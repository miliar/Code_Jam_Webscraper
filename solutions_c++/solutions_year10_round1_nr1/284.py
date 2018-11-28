#include<stdio.h>
#include<string.h>

char map[64][64];
int n, k;

const int dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dy[8] = {0, -1, 1, -1, 1, 0, -1, 1};

void read_it()
{
	scanf( "%d %d", &n, &k );
	for( int i = 0; i < n; ++i )
		scanf( "%s", map[i] );
}


bool cnt_it( char ch )
{
	for( int i = 0; i < n; ++i )
		for( int j = 0; j < n; ++j )
			if( map[i][j] == ch )
				for( int d = 0; d < 8; ++d )
				{
					int cnt = 0;
					int nowx = i;
					int nowy = j;
					while( nowx >= 0 && nowx < n && nowy >= 0 && nowy < n && map[nowx][nowy]==ch )
					{
						++cnt;
						if( cnt >= k )
							return true;
						nowx += dx[d];
						nowy += dy[d];
					}
				}
	return false;
}

void try_it()
{
	for( int i = 0; i < n; ++i )
	{
		int top = n-1;
		for( int j = n -1; j >= 0; --j )
			if( map[i][j] != '.' )
			{
				map[i][top] = map[i][j];
				if( j != top )
					map[i][j] = '.';
				--top;
			}
	}

	bool succ_r = cnt_it( 'R' );
	bool succ_b = cnt_it( 'B' );

	if( !succ_r && !succ_b )
		printf( "Neither\n" );
	else if( succ_r && !succ_b )
		printf( "Red\n" );
	else if( !succ_r && succ_b )
		printf( "Blue\n" );
	else
		printf( "Both\n" );
}

int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t;
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i )
	{
		printf( "Case #%d: ", i+1 );
		read_it();
		try_it();
	}
	return 0;
}