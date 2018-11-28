#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen( "A-large.in", "rt", stdin );
	freopen( "output2.txt", "wt", stdout );

	int T = 0;
	scanf( "%d", &T );

	for( int i = 0; i < T; i++ )
	{
		char s[4][4];

		for( int j = 0; j < 4; j++ )
			scanf( "%s", s[j] );

		// 이 경우 스트링 프린트를 하게되면 \0가 줄마다 없기때문에 계속 이어진 끝까지 프린트를 하게됨.*

/*		for( int j = 0; j < 4; j++ )
		{
			for( int k = 0; k < 4; k++ ) printf( "%c", s[j][k] );
			printf( "\n" );
		}*/

		int result = 0;
		int ncpossible = 0;

		//가로라인 검사
		for( int j = 0; j < 4; j++ )
		{
			int X = 0;
			int O = 0;

			for( int k = 0; k < 4; k++ )
			{
				if( s[j][k] == 'X' )
				{
					X++;
					continue;
				}
				if( s[j][k] == 'O' )
				{
					O++;
					continue;
				}
				if( s[j][k] == 'T' )
				{
					X++;
					O++;
					continue;
				}
				if( s[j][k] == '.' )
				{
					ncpossible = 1;
					break;
				}
			}

			if( X == 4 )
			{
				result = 1;
				goto there;
			}
			if( O == 4 )
			{
				result = 2;
				goto there;
			}
		}

		// 세로라인 검사
		for( int j = 0; j < 4; j++ )
		{
			int X = 0;
			int O = 0;

			for( int k = 0; k < 4; k++ )
			{
				if( s[k][j] == 'X' )
				{
					X++;
					continue;
				}
				if( s[k][j] == 'O' )
				{
					O++;
					continue;
				}
				if( s[k][j] == 'T' )
				{
					X++;
					O++;
					continue;
				}
				if( s[k][j] == '.' )
				{
					ncpossible = 1;
					break;
				}
			}

			if( X == 4 )
			{
				result = 1;
				goto there;
			}
			if( O == 4 )
			{
				result = 2;
				goto there;
			}
		}

		// 대각선 검사1
		int X = 0;
		int O = 0;

		for( int j = 0; j < 4; j++ )
		{
			if( s[j][j] == 'X' )
			{
				X++;
				continue;
			}
			if( s[j][j] == 'O' )
			{
				O++;
				continue;
			}
			if( s[j][j] == 'T' )
			{
				X++;
				O++;
				continue;
			}
			if( s[j][j] == '.' )
			{
				ncpossible = 1;
				break;
			}
		}
			
		if( X == 4 )
		{
			result = 1;
			goto there;
		}
		if( O == 4 )
		{
			result = 2;
			goto there;
		}

		// 대각선 검사2
		X = 0;
		O = 0;

		for( int j = 0; j < 4; j++ )
		{
			if( s[j][3-j] == 'X' )
			{
				X++;
				continue;
			}
			if( s[j][3-j] == 'O' )
			{
				O++;
				continue;
			}
			if( s[j][3-j] == 'T' )
			{
				X++;
				O++;
				continue;
			}
			if( s[j][3-j] == '.' )
			{
				ncpossible = 1;
				break;
			}
		}
			
		if( X == 4 )
		{
			result = 1;
			goto there;
		}
		if( O == 4 )
		{
			result = 2;
			goto there;
		}

there:
		printf( "Case #%d: ", i+1 );

		if( result == 1 ) printf( "X won\n");
		if( result == 2 ) printf( "O won\n");
		if( result == 0 )
			if( ncpossible == 1 ) printf( "Game has not completed\n");
			else if( ncpossible == 0 ) printf( "Draw\n");
	}

	return 0;
}
