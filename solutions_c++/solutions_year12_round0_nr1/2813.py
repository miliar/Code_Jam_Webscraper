// ZOJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <cstdio>
#include <map>
#include <queue>

#define REP(i,j,k) for(int i = j ; i < k ; ++i)
#define INF (0x7FFFFFFF)
#define MAX (875714)   
//#define MAX (100)

using namespace std;

int main()
{
	freopen( "test.txt" , "r" , stdin );
	freopen( "C:\\out.txt" , "w" , stdout );

	map< char , char > g2r;
	g2r[ ' ' ] = ' ';
	g2r[ 'y' ] = 'a';
	g2r[ 'e' ] = 'o';
	g2r[ 'q' ] = 'z';


	string google[ 3 ];
	string regular[ 3 ];

	google[ 0 ] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	google[ 1 ] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	google[ 2 ] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

	regular[ 0 ] = "our language is impossible to understand";
	regular[ 1 ] = "there are twenty six factorial possibilities";
	regular[ 2 ] = "so it is okay if you want to just give up";

	REP( c , 0 , 3 )
	{
		REP( i , 0 , google[ c ].size() )
		{
			char g = google[ c ][ i ];
			char r = regular[ c ][ i ];

			if( g2r.find( g ) == g2r.end() )
			{
				g2r[ g ] = r;
			}
		}
	}
	g2r[ 'z' ] = 'q';

	
	int T;
	cin >> T;

	cin.ignore();
	string line;

	REP( cases , 1 , T + 1 )
	{
		printf( "Case #%d: " , cases );

		getline( cin , line );

		REP( i , 0 , line.size() )
		{
			printf( "%c" , g2r[ line[ i ] ] );
		}

		cout << endl;


	}

	return 0;
}