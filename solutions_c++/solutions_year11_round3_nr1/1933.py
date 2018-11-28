#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
using namespace std;

char Table[55][55];
char Result[55][55];


int main()
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.txt", "wt", stdout );

	int T;
	cin >> T;
	char _ch;
	for( int t=1; t<=T; ++t )
	{
		int R, C;
		cin >> R >> C;
		memset( Table, 0, sizeof(Table) );
		

		for( int r=0; r<R; ++r )
		{
			for( int c=0; c<C; ++c )
			{
				cin >> _ch;
				Table[r][c] = _ch;
				Result[r][c] = '.';
			}
		}

		for( int r=0; r<R; ++r )
		{
			for( int c=0; c<C; ++c )
			{
				if( Table[r][c] == '#' )
				{
					if( Table[r+1][c] == '#' &&
						Table[r][c+1] == '#' &&
						Table[r+1][c+1] == '#' )
					{
						Result[r][c] = '/';
						Result[r][c+1] = '\\';
						Result[r+1][c] = '\\';
						Result[r+1][c+1] = '/';
						Table[r+1][c] = '.';
						Table[r][c+1] = '.';
						Table[r+1][c+1] = '.';
					}
					else
					{
						Result[r][c] = '#';
					}
				}
				else
				{
					
				}
			}
		}

		bool flag = true;
		for( int r=0; r<R; ++r )
		{
			for( int c=0; c<C; ++c )
			{
				if( Result[r][c] == '#' )
					flag = false;
			}
		}
		printf( "Case #%d:\n" , t );

		if( flag == false )
		{
			printf( "Impossible\n" );	
			continue;
		}

		for( int r=0; r<R; ++r )
		{
			for( int c=0; c<C; ++c )
				printf( "%c", Result[r][c] );
			printf( "\n" );
		}
		


	}
	return 0;
}
