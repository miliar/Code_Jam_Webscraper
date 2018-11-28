#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <iostream>

using namespace std;
std::map< char, char > table;

void learn( std::string from, std::string to )
{
	for( size_t i=0; i<from.size(); i++ ) {
		table[ from[i] ] = to[i];
	}
}

std::string translate( std::string from )
{
	std::string ans;
	for( size_t i=0; i<from.size(); i++ ) {
		char ch = table[ from[i] ];
		if( ch == 0 )
			ch = from[i];
		
		ans.push_back( ch );
	}
	
	return ans;
}

int main()
{
	FILE *fin = fopen( "../../input.txt", "rt" );
	FILE *fout = fopen( "../../out.txt", "wt" );
//	FILE *fout = stdout;
	
	learn("a", "y");
	learn("o", "e");
	learn("z", "q");
	learn("q", "z");
	learn("ejp mysljylc kd kxveddknmc re jsicpdrysi", 
		  "our language is impossible to understand");
	learn("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", 
		  "there are twenty six factorial possibilities");
	learn("de kr kd eoya kw aej tysr re ujdr lkgc jv", 
		  "so it is okay if you want to just give up");

	int tc = 0;
	fscanf( fin, "%d\n", &tc );
	
	for( int i=1; i<=tc; i++ )
	{
		char line[256];
		fgets( line, 255, fin );
		fprintf( fout, "Case #%d: %s", i, translate(line).c_str() );
	}
	
    return 0;
}