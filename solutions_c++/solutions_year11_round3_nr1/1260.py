#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <vector>
#include <assert.h>


int main()
{
	FILE *fin, *fout;
	if ( !(fin = fopen( "A-large.in", "r" ) ) ) return -1;

	if ( !( fout = fopen( "res.txt", "w" ) ) ) return -1;

	int nCases;
	fscanf( fin, "%d", &nCases );
	for( int iCase = 0; iCase < nCases; iCase++ )
	{
		int rows, cols;
		fscanf( fin, "%d %d\n", &rows, &cols );

		std::vector< std::vector< int > > pic;
		pic.resize( rows );
		for( int y = 0; y < rows; y++ )
		{
			pic[y].resize( cols );
			for( int x = 0; x < cols; x++ )
			{
				char c = fgetc( fin );
				if ( c == '.' ) pic[y][x] = 0;
				else if ( c == '#' ) pic[y][x] = 1;
				else assert( false );
			}
			fgetc( fin );
		}

		fprintf( fout, "Case #%d:\n", iCase + 1 );
		bool ok;
		while( true )
		{
			ok = true;
			bool action = false;
			for( int y = 0; y < rows; y++ )
			{
				for( int x = 0; x < cols; x++ )
				{
					if ( pic[y][x] == 1 )
					{
						if ( y + 1 == rows || x + 1 == cols )
						{
							ok = false;
							break;
						}
						if ( pic[y+1][x] == 1 && pic[y+1][x+1] == 1 && pic[y][x+1] == 1 )
						{
							pic[y][x] = '/';
							pic[y][x+1] = '\\';
							pic[y+1][x] = '\\';
							pic[y+1][x+1] = '/';
							action = true;
						}
						else 
						{
							ok = false;
							break;
						}
					}
				}
				if ( !ok ) break;
			}
			if ( !ok ) break;
			if ( !action ) break;
		}

		if ( !ok )
			fprintf( fout, "Impossible\n" );
		else
		{
			for( int y = 0; y < rows; y++ )
			{
				for( int x = 0; x < cols; x++ )
				{
					if ( pic[y][x] == 0 ) fprintf( fout, "." );
					else if ( pic[y][x] == '/' || pic[y][x] == '\\' )
						fprintf( fout, "%c", char(pic[y][x]) );
					else assert( false );
				}
				fprintf( fout, "\n" );
			}
		}
	}

	fclose( fin );
	fclose( fout );

	return 0;
}
