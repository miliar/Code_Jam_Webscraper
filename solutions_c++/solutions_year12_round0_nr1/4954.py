#include <cstdio>
#include <string>
#include <cstdlib>
#include <cctype>
using namespace std;

char from_googlerese( char g ){
	switch( g ){ //Casing?
		case 'a': return 'y';
		case 'b': return 'h';
		case 'c': return 'e';
		case 'd': return 's';
		case 'e': return 'o';
		case 'f': return 'c';
		case 'g': return 'v';
		case 'h': return 'x';
		case 'i': return 'd';
		case 'j': return 'u';
		case 'k': return 'i';
		case 'l': return 'g';
		case 'm': return 'l';
		case 'n': return 'b';
		case 'o': return 'k';
		case 'p': return 'r';
		case 'q': return 'z';
		case 'r': return 't';
		case 's': return 'n';
		case 't': return 'w';
		case 'u': return 'j';
		case 'v': return 'p';
		case 'w': return 'f';
		case 'x': return 'm';
		case 'y': return 'a';
		case 'z': return 'q';
		default: return g;
	}
}

string read_line( FILE *f ){
	string s = "";
	char c;
	while( ((c = getc(f)) != '\n') && (c != EOF) )
		s += c;
	return s;
}

int main(){
	FILE *f = fopen( "small.txt", "r" );
	FILE *o = fopen( "small-result.txt", "w" );
	
	if( f ){
		int i = atoi( read_line(f).c_str() );
		for( int foo=1; foo <= i; foo++ ){
			string g = read_line(f);
			string latin = "";
			for( int j=0; j<g.size(); j++ )
				latin += from_googlerese( g[j] );
				
			fprintf( o, "Case #%d: %s\n", foo, latin.c_str() );
		}
	}
	
	return 0;
}

