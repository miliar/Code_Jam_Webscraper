#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <bitset>
#include <list>

using namespace std;

int main ( )
{
	freopen ( "input", "r", stdin );
	freopen ( "output", "w", stdout );
	
	const string s = "yhesocvxduiglbkrztnwjpfmaq";
	
	string line;
	int n;
	
	getline ( cin, line );
	sscanf ( line.c_str(), "%d", &n );
	
	for ( int i = 1; i <= n; ++i )
	{
		getline ( cin, line );
		printf ( "Case #%d: ", i );
		for ( int j = 0; j < (int)line.size(); ++j )
			if ( line[j] < 'a' || line[j] > 'z' )
				printf ( " " );
			else
				printf ( "%c", s[line[j]-'a'] );
		printf ( "\n" );
	}
	
	return 0;
} 
