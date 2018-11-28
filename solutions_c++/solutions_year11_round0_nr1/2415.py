#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <vector>
#include <assert.h>

int main()
{
	FILE *fin, *fout;
	if ( fopen_s( &fin, "A-large.in", "r" ) != 0 )
		return -1;

	if ( fopen_s( &fout, "res.txt", "w" ) != 0 )
		return -1;

	int nCases;
	fscanf( fin, "%d", &nCases );
	for( int iCase = 0; iCase < nCases; iCase++ )
	{
		int nButtons;
		fscanf( fin, "%d ", &nButtons );

		std::vector< int > robots;
		std::vector< int > buttons;
		std::vector< int > works[2];
		int iButton;
		for( iButton = 0; iButton < nButtons; iButton++ )
		{
			char c;
			fscanf( fin, "%c ", &c );
			int btn;
			fscanf( fin, "%d ", &btn );
			assert( c == 'O' || c == 'B' );
			int r = ( c == 'O' ? 0 : 1 );
			robots.push_back( r );
			buttons.push_back( btn );
			works[r].push_back( btn );
		}


		std::vector< int >::iterator iw[2] = { works[0].begin(), works[1].begin() };
		int sec = 0;
		int r1pos = 1, r2pos = 1;
		iButton = 0;
		while( iw[0] != works[0].end() ||  iw[1] != works[1].end() )
		{
			sec++;
			bool bPress = false;
			if ( iw[0] != works[0].end() )
			{
				if ( r1pos > *iw[0] )
					r1pos--;
				else if ( r1pos < *iw[0] )
					r1pos++;
				else
				{
					if ( robots[iButton] == 0 )
					{
						iw[0]++;
						bPress = true;
					}
				}
			}

			if ( iw[1] != works[1].end() )
			{
				if ( r2pos > *iw[1] )
					r2pos--;
				else if ( r2pos < *iw[1] )
					r2pos++;
				else
				{
					if ( robots[iButton] == 1 )
					{
						iw[1]++;
						bPress = true;
					}
				}
			}

			if ( bPress )
				iButton++;
		}

		assert( iButton == nButtons );

		fprintf( fout, "Case #%d: %d\n", iCase + 1, sec );
	}

	fclose( fin );
	fclose( fout );
}
