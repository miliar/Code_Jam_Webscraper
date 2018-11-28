#include <stdio.h>

int main()
{
	char  filename [] = "G:\\GCJ\\GCJ\\A-large.in";
	char  output[] = "G:\\GCJ\\GCJ\\A-large.out";
	FILE * fp1, * fp2;
	int cas;
	int T, N, K;

	fp1 = fopen( filename, "r" );
	fp2 = fopen( output, "w" );

	fscanf( fp1, "%d", &T );
	for ( cas = 1; cas <= T; cas++ )
	{
		fscanf( fp1, "%d %d", &N, &K );
		int X = ( 1 << N );
		K %= X;
		fprintf( fp2, "Case #%d: %s\n",cas, ( K == X - 1 ) ? "ON" : "OFF" );

	}

	fclose( fp1 );
	fclose( fp2 );
	return 0;
}