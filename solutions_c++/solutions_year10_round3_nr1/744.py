// Google CodeJam R1 C.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include< vector>
using namespace std;


 
int main(int argc, char * argv[ ]  )
{
	freopen ( "A.in", "rt", stdin );
	freopen( "A.out", "wt", stdout );

	int T = 0;
	cin >> T;

	for( int ct = 0; ct < T; ++ct )
	{
		int N = 0;
		cin >> N;

		vector<int> As;
		vector<int> Bs;

		for( int i = 0;  i < N; ++i )
		{
			int a, b;
			cin >> a >> b;
			As.push_back( a );
			Bs.push_back( b );
		}

		int res = 0;

		for( int i = 0; i < N; ++i )
		{
			for( int j = i + 1; j < N; ++j )
			{
				if( As[ i ] < As[ j ] && Bs[ i ] > Bs[ j ] )
				{
					++res;
				}
				else if( As[ i ] > As[ j ] && Bs[ i ] < Bs[ j ] )
				{
					++res;
				}
			}
		}

		cout << "Case #" << ct + 1 << ": " << res << endl;
	}
	return 0;
}

