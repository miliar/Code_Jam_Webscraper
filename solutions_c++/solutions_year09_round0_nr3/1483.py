#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
using namespace std;

string Pattern = "welcome to code jam";

int res[ 21 ];

int main( )
{
	freopen( "input.txt", "rt", stdin );
	freopen( "output.out", "wt", stdout );

	int N = 0;

	cin >> N;	
	string t;
	getline( cin, t );


	for( int ct = 1; ct <= N; ++ct )
	{
		memset( res, 0, sizeof( res ) );
		res[ 0 ] = 1;
		getline( cin, t );
		for( int i = 0; i < t.size( ); ++i )
		{
			switch( t[ i ] )
			{
			case 'w':
				res[ 1 ] += res[ 0 ];res[ 1 ] %= 10000;
				break;
			case 'e':
				res[ 2 ] += res[ 1 ];res[ 2 ] %= 10000;
				res[ 7 ] += res[ 6 ];res[ 7 ] %= 10000;
				res[ 15 ] += res[ 14 ];res[ 15 ] %= 10000;
				break;
			case 'l':
				res[ 3 ] += res[ 2 ];res[ 3 ] %= 10000;
				break;
			case 'c':
				res[ 4 ] += res[ 3 ];res[ 4 ] %= 10000;
				res[ 12 ] += res[ 11 ];res[ 12 ] %= 10000;
				break;
			case 'o':
				res[ 5 ] += res[ 4 ];res[ 5 ] %= 10000;
				res[ 10 ] += res[ 9];res[ 10 ] %= 10000;
				res[ 13 ] += res[ 12 ];res[ 13 ] %= 10000;
				break;
			case 'm':
				res[ 6 ] += res[ 5 ];res[ 6 ] %= 10000;
				res[ 19 ] += res[ 18 ];res[ 19 ] %= 10000;
				break;
			case ' ':
				res[ 8 ] += res[ 7 ];res[ 8 ] %= 10000;
				res[ 11 ] += res[ 10 ];res[ 11 ] %= 10000;
				res[ 16 ] += res[ 15 ];res[ 16 ] %= 10000;
				break;
			case 't':
				res[ 9 ] += res[ 8 ];res[ 9 ] %= 10000;
				break;
			case 'd':
				res[ 14 ] += res[ 13 ];res[ 14 ] %= 10000;
				break;
			case 'j':
				res[ 17 ] += res[ 16 ];res[ 17 ] %= 10000;
				break;
			case 'a':
				res[ 18 ] += res[ 17 ];res[ 18 ] %= 10000;
				break;
			default:
				break;

			}
		}

		string sres;
		stringstream ss;
		ss<< res[ 19 ];
		ss >> sres;

		while( sres.size( ) < 4 )
		{
			sres = "0" + sres;
		}

		cout << "Case #" << ct << ": " << sres << endl;
	}

}