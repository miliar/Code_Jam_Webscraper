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

		// �� ��� ��Ʈ�� ����Ʈ�� �ϰԵǸ� \0�� �ٸ��� ���⶧���� ��� �̾��� ������ ����Ʈ�� �ϰԵ�.*

/*		for( int j = 0; j < 4; j++ )
		{
			for( int k = 0; k < 4; k++ ) printf( "%c", s[j][k] );
			printf( "\n" );
		}*/

		int result = 0;
		int ncpossible = 0;

		//���ζ��� �˻�
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

		// ���ζ��� �˻�
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

		// �밢�� �˻�1
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

		// �밢�� �˻�2
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
