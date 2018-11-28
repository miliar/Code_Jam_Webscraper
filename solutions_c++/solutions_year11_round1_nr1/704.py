#include <cstdio>
#include <cstdlib>


int gcd( int a , int b )
{
	if( a == 0 ) return b;
	return gcd( b%a , a );
}


int main()
{
	FILE * fin = fopen("in.txt" , "r" );
	FILE * fout = fopen("out.txt" , "w" );
	
	int T;
	fscanf( fin , "%d" , &T );
	
	for( int t = 1 ; t <= T ; t++ )
	{
		__int64 N;
		int Pd , Pg;
		fscanf( fin , "%I64d %d %d" , &N , &Pd , &Pg );
		int D = 100/gcd( Pd , 100 );
		if( Pd == 0 ) D = 1;
		if( D > N ) goto FAIL;
		if( Pg == 100 && Pd < 100 ) goto FAIL;
		if( Pg == 0 && Pd > 0 ) goto FAIL;
		fprintf( fout , "Case #%d: Possible\n" , t );
		continue;
FAIL:;
		fprintf( fout , "Case #%d: Broken\n" , t );
	}
	
	return 0;
}
