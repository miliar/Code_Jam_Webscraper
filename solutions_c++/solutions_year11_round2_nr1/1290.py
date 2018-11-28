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

		int N;

		cin >> N;

		char** board;
		board = (char**)malloc( N * sizeof( int* ) );

		for( int i = 0 ; i < N ; i ++ )
			board[ i ] = (char*) malloc( N * sizeof( int ) );

		int* num = new int[ N ];
		for( int i = 0 ; i < N ; i ++ )
		{
			num[ i ] = 0;
			for( int j = 0 ; j < N ; j ++ )
			{
				cin >> board[ i ][ j ];
				if( board[ i ][ j ] != '.' )
					num[ i ] ++;
			}
		}
		int* WP = new int[ N ];

		for( int i = 0 ; i < N ; i ++ )
		{
			WP[ i ] = 0;
			for( int j = 0 ; j < N ; j ++ )
			{
				if( board[ i ][ j ] == '1' )
					WP[ i ] ++;
			}
		}
		double* OWP = new double[ N ];
		for( int i = 0 ; i < N ; i ++ )
		{
			OWP[ i ] = 0; 
			for( int j = 0 ; j < N ; j ++ )
			{
				if( board[ i ][ j ] != '.' )
				{
					OWP[ i ] += (double)( WP[ j ] - ( board[ j ][ i ] - '0' ) ) / (double)( num[ j ] - 1 );
				}
			}
			OWP[ i ] /= num[ i ];
		}
		double* OOWP = new double[ N ];
		for( int i = 0 ; i < N ; i ++ )
		{
			OOWP[ i ] = 0;
			for( int j = 0 ; j < N ; j ++ )
			{
				if( board[ i ][ j ] != '.' )
				{
					OOWP[ i ] += OWP[ j ];
				}
			}
			OOWP[ i ] /= num[ i ];
		}
		for( int i = 0 ; i < N ; i ++ )
		{
			double RPI = 0.25 * (double)WP[ i ] / (double)num[ i ] + 0.5 * OWP[ i ] + 0.25 * OOWP[ i ];
			printf( "%.7f\n" , RPI );
		}
	}
	return 0;
}