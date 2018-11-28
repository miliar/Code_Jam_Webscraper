#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int T, R, k, N;
	ifstream fin;
	fin.open( "C-small.in" );
	if( fin.fail() )
	{
		cout << "FILE WAS NOT SUCCESFULLY OPENED!!" << endl;
		return -1;
	}
	fin >> T;
	if( T < 1 || T > 50 )
	{
		cout << T << " is not a valid number of test cases" << endl;
		return -1;
	}
	
	for( int i = 0; i < T; i++ )
	{
		fin >> R >> k >> N;
		if( R < 1 || R > 1000)
		{
			cout << R << " is not a valid R" << endl;
			return 1;
		}
		if( k < 0 || k > 100)
		{
			cout << k << " is not a valid k" << endl;
			return 1;
		}
		if( N < 0 || N > 10)
		{
			cout << k << " is not a valid k" << endl;
			return 1;
		}
		
		int g[N];
		for( int j = 0; j < N; j++ )
		{
			fin >> g[j];
		}
		
		int euro = 0;
		int seating = 0;

		for( int j = 0; j < R; j++ )
		{
			seating = 0;
			for( int K = 0; K < N; K++ )
			{
				if( seating + g[0] <= k )
				{
					seating += g[0];
					euro += g[0];
					int temp = g[0];
					for( int l = 0; l < N-1; l++ )
						g[l] = g[l+1];
					g[N-1] = temp;
				}
				else
					break;
			}
		}
		cout << "Case #" << i+1 << ": " << euro << endl;

	}
	
	return 0;
}
