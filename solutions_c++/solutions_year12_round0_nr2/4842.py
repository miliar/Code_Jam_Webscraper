#include <cstdio>
#include <string>
#include <cstdlib>
#include <cctype>
using namespace std;


enum can_beat{
	NOPE,
	YES,
	IF_SURPRISED
};

can_beat googler( unsigned sum, unsigned p ){
	int base = sum / 3;
	if( base >= p )
		return YES;
	
	switch( sum ){
		case 0:
		case 1: return NOPE;
		case 2:
			if( p == 1 )
				return YES;
			else
				return ( p == 2 ) ? IF_SURPRISED : NOPE;
	}
	
	switch( sum % 3 ){
		case 0: return ( base + 1 == p ) ? IF_SURPRISED : NOPE;
		case 1: return ( base + 1 == p ) ? YES : NOPE;
		case 2:
				if( base + 1 == p )
					return YES;
				else
					return ( base + 2 == p ) ? IF_SURPRISED : NOPE;
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
		int amount = atoi( read_line(f).c_str() );
		for( int i=1; i <= amount; i++ ){
			int N, S, p;
			fscanf( f, "%d %d %d", &N, &S, &p );
			
			int can = 0;
			int depends = 0;
			
			for( int j=0; j<N; j++ ){
				int sum;
				fscanf( f, "%d", &sum );
				switch( googler( sum, p ) ){
					case YES: can++; break;
					case IF_SURPRISED: depends++; break;
				}
				
			}
			
			int besters = can + (( S > depends ) ? depends : S);
			fprintf( o, "Case #%d: %d\n", i, besters );
		}
	}
	
	return 0;
}

