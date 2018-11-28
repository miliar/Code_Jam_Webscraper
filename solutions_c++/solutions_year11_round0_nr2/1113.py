/*
 * Author ahfyth
*/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

const char base[] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

map<char, int> basemap;
char combine[8][8];
bool oppose[8][8];


string solve( string s )
{
	char *p = new char[ s.size() ];
	string :: iterator it;
	it = s.begin();
	p[0] = *it;
	unsigned int curr = 1;
	int i, j;
	char c;
	for( ++it; it!=s.end(); ++it )
	{
//		cerr << "GET : " << *it << "\n";
		if( curr == 0 )
		{
			p[ curr++ ] = *it;
			continue;
		}
		if( basemap.find ( p[curr-1] ) != basemap.end() )	// maybe a combine
		{
			c = combine[ basemap.find(p[curr-1])->second ] [ basemap.find( *it )->second ] ;
			if( c != '\0' )
			{
				p[ curr-1 ] = c;
//				cerr << "Combine to " << c << "\n";
				continue;
			}
		}
		// check oppose
		for( i=curr-1; i>=0; --i )
		{
			if( basemap.find ( p[i] ) == basemap.end() )	// maybe a combine
				continue;
			if( oppose[ basemap.find(p[i])->second ] [ basemap.find( *it )->second ] )
				break;
		}
		if( i >= 0 )
		{
			curr = 0;
//			cerr << "Oppose : " << i << endl;
			continue;
		}
		p[ curr ++ ] = *it;
	}

//	p[ curr ] = '\0';
//	cerr << p << "\n";
	if( curr == 0 )return "[]";

	string key("[");
	for( i=0; i<curr-1; ++i )
	{
		key += p[i];
		key += ", ";
	}
	key += p[i];
	key += ']';
	return key;
}


int main( int argc, char *argv[] )
{
	if( argc < 2 )
	{
		cerr << "Usage : " << argv[0] << " <file>\n";
		cerr << "This program is designed to \n";
		exit( 1 );
	}
	ifstream fin;
	fin.open( argv[1], ios::in );
	if( fin.fail() )
	{
		cerr << "Error : open file failed!\n";
		return 2;
	}

	basemap.insert( pair<char, int>( base[0], 0 ) );
	basemap.insert( pair<char, int>( base[1], 1 ) );
	basemap.insert( pair<char, int>( base[2], 2 ) );
	basemap.insert( pair<char, int>( base[3], 3 ) );
	basemap.insert( pair<char, int>( base[4], 4 ) );
	basemap.insert( pair<char, int>( base[5], 5 ) );
	basemap.insert( pair<char, int>( base[6], 6 ) );
	basemap.insert( pair<char, int>( base[7], 7 ) );

	unsigned int TOTAL;
	fin >> TOTAL;

	unsigned int i, j, k;
	unsigned int C, D, N;
	string tmp;
	
	for( i=1; i<=TOTAL; ++i )
	{
		for( j=0; j<8; ++j )
		{
			for( k=0; k<8; ++k )
			{
				oppose[j][k] = false;
				combine[j][k] = '\0';
			}
		}

		fin >> C;
		for( j=0; j<C; ++j )
		{
			fin >> tmp;
			combine[ basemap.find(tmp[0])->second ][ basemap.find(tmp[1])->second ] = tmp[2];
			combine[ basemap.find(tmp[1])->second ][ basemap.find(tmp[0])->second ] = tmp[2];
		}

		fin >> D;
		for( j=0; j<D; ++j )
		{
			fin >> tmp;
			oppose[ basemap.find(tmp[0])->second ][ basemap.find(tmp[1])->second ] = true;
			oppose[ basemap.find(tmp[1])->second ][ basemap.find(tmp[0])->second ] = true;
		}

		fin >> N;
		fin >> tmp;

		tmp = solve( tmp );

		cout << "Case #" << i << ": " << tmp << endl;
	}

	fin.close();

	return 0;
}



