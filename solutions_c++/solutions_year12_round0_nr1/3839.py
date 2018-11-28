// RQ.cpp : Defines the entry point for the console application.
//
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <fstream>
#include <ostream>
#include <sstream>
using namespace std;


const string lang =  "aybhcedseofcgvhxidjukilgmlnbokprqzrtsntwujvpwfxmyazq";
map<char,char> real;
string decode( const string&  in )
{
	string res;
	for( int i = 0; i < in.size( ); ++i )
	{
		res += real[ in[ i ] ];
	}
	return res;
}

int main(int argc, char* argv[ ] )
{
	freopen( "in.txt", "rt", stdin );
	freopen( "out.txt", "wt", stdout );
	vector<string> in;
	//char buf[ 10000 ];
	//for( int i = 0; i < 3; ++i )
	//{
	//	cin.getline( buf, 10000, '\n' );
	//	string t;
	//	t = buf;
	//	in.push_back( t );
	//}

	//
	//for( int i = 0; i < 3; ++i )
	//{

	//	cin.getline( buf, 10000, '\n' );
	//	string t;
	//	t = buf;
	//	out.push_back( t );
	//}

	//map<char,char> mp;
	//mp[ 'q' ] = 'z';
	//mp[ 'e' ] = 'o';

	//set<char> outs;
	//outs.insert( 'z' );
	//outs.insert( 'o' );

	//for( int i = 0; i < in.size( ); ++i )
	//{
	//	for( int j = 0; j < in[ i ].size( ); ++j )
	//	{
	//		mp[ in[ i ][ j ] ] = out[ i ][ j ];
	//		outs.insert( out[ i ][ j ] );
	//	}
	//}

	//for( int i = 0; i < 26; ++i )
	//{
	//	if( mp.end() == mp.find( 'a' + i ) )
	//	{
	//		for( int j = 0; j < 26; ++j )
	//		{
	//			if( outs.end( ) == outs.find( 'a' + j ) )
	//			{
	//				mp[ 'a' + i ] = 'a' + j;
	//			}
	//		}
	//	}
	//}


	//for( map<char,char>::iterator it = mp.begin( ); it != mp.end( ); ++it )
	//{
	//	cout << it->first << it->second;
	//}

	real.insert( make_pair( ' ', ' ' ) );
	for( int i = 0; i < lang.size( ); i +=2 )
	{
		real.insert( make_pair( lang[ i ], lang[ i + 1 ] ) );
	}

	char buff[ 1000 ] = { 0 };
	int n = 0;
	cin.getline( buff, 1000, '\n' );
	stringstream ss( buff );
	ss >> n;

	for( int i = 0; i < n; ++i )
	{
		cin.getline( buff, 1000, '\n' );
		cout << "Case #" << i + 1 << ": " << decode( string( buff ) ) << endl;
	}

	return 0;
}

