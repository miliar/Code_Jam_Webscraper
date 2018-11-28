#include <iostream>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cctype>

using namespace std;

#define FIN "A-large.in"
#define FOUT "A-large.out"


#define SMAX 106
#define QMAX 1006
#define INF 1006
#define STRING_SIZE 300

int A[QMAX][SMAX];
int ASK[QMAX];
char SERVER[SMAX][STRING_SIZE];
char querry[STRING_SIZE];
int Q, S, T;

int min( int a, int b )
{
	return a < b ? a : b;
}

int solve()
{
	int i, j, current, last = 0;
	
	for( i = 1; i <= Q; i++ )
	for( j = 1; j <= S; j++ )
		A[i][j] = 0;
		
	for( i = 1; i <= Q; i++ ) {
		current = INF;
		for( j = 1; j <= S; j++ ) {
			if ( ASK[i] == j )	A[i][j] = INF;
			else A[i][j] = min( A[i-1][j], last + 1);
			current = min( current, A[i][j] );
		}
		last = current;
	}
 return last;
}


		
	

int main()
{
	FILE *fin = fopen( FIN, "r" );
	FILE *fout = fopen( FOUT, "w" );
	int i, j;
	
	fscanf( fin, "%d\n", &T );
	for( int T_STEP = 1; T_STEP <= T; T_STEP++) {
		fscanf( fin, "%d\n", &S );
		for( i = 1; i <= S; i++ ) 
			fgets( SERVER[i], STRING_SIZE - 1, fin );
			
		fscanf( fin, "%d\n", &Q );
		
		for( i = 1; i <= Q; i++ ) {
			fgets( querry, STRING_SIZE - 1, fin );
			for( j = 1; j <= S; j++ ) 
				if( strcmp( querry, SERVER[j] ) == 0 ) {
					ASK[i] = j;
					break;
				}
		}
		ASK[Q+1] = INF;
	
		
		fprintf( fout, "Case #%d: %d\n", T_STEP, solve() );
	}		
		
	fclose( fin );
	fclose( fout );			
		
	

	return 0;
}

