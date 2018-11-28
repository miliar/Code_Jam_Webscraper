#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int T, N, K;
	ifstream fin;
	fin.open( "A-small.in" );
	if( fin.fail() )
	{
		cout << "FILE WAS NOT SUCCESFULLY OPENED!!" << endl;
		return -1;
	}
	fin >> T;
	if( T < 1 || T > 10000 )
	{
		cout << T << " is not a valid number of test cases" << endl;
		return -1;
	}
	
	for( int i = 0; i < T; i++ )
	{
		fin >> N >> K;
		if( N < 1 || N > 30)
		{
			cout << N << " is not a valid N" << endl;
			return 1;
		}
		if( K < 0 || K > 10e8)
		{
			cout << K << " is not a valid K" << endl;
			return 1;
		}
		
		int S[N];
		int P[N];
		for( int j = 0; j < N; j++ )
		{
				S[j] = 0;
				if( j == 0 )
					P[j] = 1;
				else
					P[j] = 0;
		}

		for( int k = 0; k < K; k++ )
		{
			for( int j = 0; j < N; j++ )
			{				
				if( P[j] == 1 )
				{
					if( S[j] == 0 )
						S[j] = 1;
					else
						S[j] = 0;
				}
				if( j != 0 )
				{
					if( P[j-1] == 1 && S[j-1] == 1)
					{
						P[j] = 1;
					}
					else
						P[j] = 0;
				}
			}
		}	
		if( P[N-1] == 1 && S[N-1] == 1 )
			cout << "Case #" << i+1 << ": ON" << endl;
		else
			cout << "Case #" << i+1 << ": OFF" << endl;
	}
	
	return 0;
}
