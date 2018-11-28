#include <iostream>
#include <cstdlib>
using namespace std;

struct line
{
	int A,B;
}Line[ 1010 ];

int main()
{
	FILE *fin  = fopen( "A-large.in" , "r" );
	FILE *fout = fopen( "large.out", "w" );
	int T,N;
	fscanf( fin ,"%d", &T);
	for ( int i = 1 ; i <= T ; ++ i ) {
		fscanf( fin, "%d" , &N);
		for ( int j = 0 ; j < N ; ++ j)
			fscanf( fin, "%d%d" , &Line[ j ].A,&Line[ j ].B );
		long count = 0; 
		for ( int j = 1 ; j < N ; ++ j ) {
			for ( int k = 0 ; k < j ; ++ k )	
				if ( (Line[ k ].A-Line[ j ].A)*(Line[ k ].B-Line[ j ].B) < 0 )
					++ count;
		}
		fprintf( fout, "Case #%d: %d\n",i,count);
	}	
	return 0;
}
