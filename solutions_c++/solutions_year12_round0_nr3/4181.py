#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

const int size = 1000;
unsigned char nums[size+1];


void reset(){
	for(int i=0; i<size; i++)
		nums[i]=0;
}
int count( int min, int max ){
	unsigned count=0;
	for( int i=min; i<=max; i++ ){
		count += nums[i];
//		if( nums[i] )
//			printf( "nums %d, %d\n", i, nums[i] );
	}
	return count / 2;
}
int get_mirror( int x, int len, int pos ){
	char *val = new char[len+1];
	itoa( x, val, 10 );
	char *result = new char[len+1];
	result[len] = 0;
	
	int inverse = len-pos;
	for( int i=0; i<pos; i++ )
		result[i] = val[inverse+i];
	for( int i=0; i<inverse; i++ )
		result[i+pos] = val[i];
	
	int r = atoi( result );
	delete val;
	delete result;
	return r;
}
void set( int min, int max ){
	int len;
	char *val = new char[10+1];
	itoa( max, val, 10 );
	len = strlen( val );
	delete val;
	
	for( int i=min; i<=max; i++ )
		for( int j=1; j<len; j++){
			int mirror = get_mirror( i, len, j );
			if( mirror >= min && mirror <= max && i != mirror ){
				nums[mirror]++;
			}
		}
}


int get_all( int min, int max ){
	reset();
	set( min, max );
	return count( min, max );
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
			int min, max;
			fscanf( f, "%d %d", &min, &max );
			
			fprintf( o, "Case #%d: %d\n", i, get_all( min, max ) );
		}
	}
	
	
	return 0;
}

