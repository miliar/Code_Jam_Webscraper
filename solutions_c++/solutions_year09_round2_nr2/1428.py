// CodeJam.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <sstream>
using namespace std;


int main(int argc, char* argv[])
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.out", "wt", stdout );

	int ca = 0;
	cin >> ca;
	
	vector<int> digits( 10 );
	vector<bool> used;


	for( int ct = 1; ct <= ca; ++ct )
	{
		digits.clear( );
		digits.resize( 10, 0 );
		used.clear( );
		used.resize( 10, false );
		int N = 0;

		cin >> N;

		int temp = N;

		while( temp > 0 )
		{
			digits[ temp % 10 ]++;
			used[ temp % 10  ] = true;

			temp /= 10;
		}


		vector<int> vtemp( 10 );

		string t;

		for( int i = N + 1;; ++i )
		{
			stringstream ss;
			ss << i;
			ss >> t;

			for( int j = 0; j  < vtemp.size( ); ++j )
			{
				vtemp[ j ] = 0;
			}

			for( int j = 0; j < t.size( ); ++j )
			{
				++vtemp[ t[ j ] - '0' ];
			}

			bool flag = true;

			for( int j = 1; j < 10; ++j )
			{
					if( vtemp[ j ] != digits[ j ] ) 
					{
						flag = false;
					}
			}

			if( flag )
			{
				cout << "Case #" << ct << ": " << t << endl;

				break;
			}
		}
	}
	return 0;
}

