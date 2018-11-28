// GCJR1B.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;


int main(int argc, char* argv[])
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.txt", "wt", stdout );

	int cases = 0;
	cin >> cases;

	for( int ct = 0; ct < cases; ++ct )
	{
		int teams = 0;
		cin >> teams;

		vector<string> gameresults;
		vector<int> valls;
		vector<int> vwons;
		vector<double> rpis;
		vector<double> wps;
		vector<double> owps;
		vector<double> oowps;

		string t;

		for( int i = 0; i < teams; ++i )
		{
			cin >> t;
			gameresults.push_back( t );
		}


		for( int i = 0; i < gameresults.size( ); ++i )
		{
			int all = 0;
			int loses = 0;
			int wons = 0;

			for( int j = 0; j < gameresults[ 0 ].size( ); ++j )
			{
				if( '0' == gameresults[ i ][ j ] )
				{
					++loses;
					++all;
				}
				else if( '1' == gameresults[ i ][ j ] )
				{
					++wons;
					++all;
				}
			}

			wps.push_back( (double)wons / all );
			vwons.push_back( wons );
			valls.push_back( all );
		}

		for( int i = 0; i < teams; ++i )
		{
			double owp = 0.0;

			for( int j = 0; j < teams; ++j )
			{
				double awpNoYou = 0.0;

				if( i != j )
				{
					if( gameresults[ i ][ j ]  == '1' )
					{
						awpNoYou = (double)( vwons[ j ] ) / ( valls[ j ] - 1.0 );
					}
					else if( gameresults[ i ][ j ] == '0' )
					{
						awpNoYou = (double) ( vwons[ j ] - 1.0 ) / ( valls[ j ] - 1.0 );
					}
				}

				owp += awpNoYou;
			}

			owps.push_back( owp / valls[ i ]  );
		}

		for( int i = 0; i < teams; ++i )
		{
			double oowp = 0.0;

			for( int j = 0; j < teams; ++j )
			{
				if( i != j )
				{
					if( '.' != gameresults[ i ][ j ] )
					{
						oowp += owps[ j ];
					}
				}
			}

			oowps.push_back( oowp / valls[ i ] );
		}

		cout << "Case #" << ct + 1 << ":" << endl;

		for( int i = 0; i < teams; ++i )
		{
			cout << ( 0.25* wps[ i ] + 0.50 * owps[ i ] + 0.25 * oowps[ i ] ) << endl;
		}
	}

	return 0;
}

