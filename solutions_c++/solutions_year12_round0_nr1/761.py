#include "stdafx.h"
#include <stdio.h>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <iostream>
#include <sstream>
#include <math.h>
#include <iostream>

using namespace std;

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w+", stdout );

	char m[ 256 ] = { 0 };
	//Was generated during the parsing of problem's main example :)
	m[ ' ' ] = ' ', m[ 'a' ] = 'y', m[ 'b' ] = 'h', m[ 'c' ] = 'e', m[ 'd' ] = 's', m[ 'e' ] = 'o', m[ 'f' ] = 'c', m[ 'g' ] = 'v', m[ 'h' ] = 'x', m[ 'i' ] = 'd', m[ 'j' ] = 'u', m[ 'k' ] = 'i', m[ 'l' ] = 'g', m[ 'm' ] = 'l', m[ 'n' ] = 'b', m[ 'o' ] = 'k', m[ 'p' ] = 'r', m[ 'q' ] = 'z', m[ 'r' ] = 't', m[ 's' ] = 'n', m[ 't' ] = 'w', m[ 'u' ] = 'j', m[ 'v' ] = 'p', m[ 'w' ] = 'f', m[ 'x' ] = 'm', m[ 'y' ] = 'a', m[ 'z' ] = 'q';	
	int TC; scanf( "%d", &TC );
	for ( int _ = 0; _ < TC; _++ )
	{
		printf( "Case #%d: ", _+1 );
		char c;
		int len=0;
		while( scanf( "%c", &c ) != EOF )
		{
			if ( ( 'a' <= c && c <= 'z' ) || c == ' ' )
			{
				printf( "%c", m[ c ] );
				if ( m[ c ] == 0 )
				{
					len=len;
				}
				len++;
			}
			else if ( len ) break;
		}
		printf( "\n" );
	}
	return 0;
}
