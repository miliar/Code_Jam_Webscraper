#include<iostream>
#include<string>
#include<vector>

using namespace std;


int main()
{

	freopen( "data_in.txt" , "r" , stdin );
	freopen( "data_out.txt" , "w" , stdout );

	int T;

	cin >> T;

	for( int t = 1 ; t <= T ; t ++ )
	{
		cout << "Case #" << t << ":\n";	

		int R , C;

		cin >> R >> C;

		char** pic;

		pic = (char**)malloc( R * sizeof( char* ) );
		for( int r = 0 ; r < R ; r ++ )
			pic[ r ] = (char*)malloc( C * sizeof( char ) );

		for( int r = 0 ; r < R ; r ++ )
		{
			for( int c = 0 ; c < C ; c ++ )
				cin >> pic[ r ][ c ];
		}
	
		for( int r = 0 ; r < R - 1 ; r ++ )
		{
			for( int c = 0 ; c < C - 1 ; c ++ )
			{
				if( pic[ r ][ c ] == '#' )
				{
					if( pic[ r + 1 ][ c ] == '#' && 
						pic[ r ][ c + 1 ] == '#' &&
						pic[ r + 1 ][ c + 1 ] == '#' )
					{
						pic[ r ][ c ] = '/';
						pic[ r + 1 ][ c ] = '\\';
						pic[ r ][ c + 1 ] = '\\';
						pic[ r + 1 ][ c + 1 ] = '/';
					}
				}
			}
		}

		bool flag = true;
		for( int r = 0 ; r < R ; r ++ )
		{
			for( int c = 0 ; c < C ; c ++ )
			{
				if( pic[ r ][ c ] == '#' )
				{
					flag = false;
					break;
				}
			}
			if( !flag )
				break;
		}

		if( !flag )
			cout << "Impossible\n";

		else
		{
			for( int r = 0 ; r < R ; r ++ )
			{
				for( int c = 0 ; c < C ; c ++ )
					cout << pic[ r ][ c ];
				cout << "\n";
			}
		}
	}

	return 0;
}