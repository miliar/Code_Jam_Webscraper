#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


bool solve( __int64 pd, __int64 pg, __int64 n )
{
	if ( pg == 0 )
		return pd == 0;
	else if ( pg == 100 )
		return pd == 100;

	for( __int64 zn = 1; zn <= 100; zn++ )
		for( __int64 ch = 1; ch <= zn; ch++ )
		{
			if ( ch * 100 == pd * zn )
			{
				if ( zn <= n ) return true;
			}
		}

	return false;
}

int main()
{
	FILE *fin, *fout;
	if ( !(fin = fopen( "A-large.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d", &nCases );
	for( int iCase = 0; iCase < nCases; iCase++ )
	{
		__int64 pd, pg, n;
		fscanf( fin, "%I64d %I64d %I64d\n", &n, &pd, &pg );
		bool b = solve( pd, pg, n );

		fprintf( fout, "Case #%d: ", iCase + 1 );
		if ( b ) fprintf( fout, "Possible\n" );
		else fprintf( fout, "Broken\n" );
	}


	fclose( fin );
	fclose( fout );

	return 0;
}
