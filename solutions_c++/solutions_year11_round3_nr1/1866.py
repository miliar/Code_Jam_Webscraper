#include <stdlib.h>
#include <vector>
#include <iostream>

using namespace std;

int main( int argc, char* argv[])
{
	int T, R, C, nBlue;
	char tile[60][60];

	cin >> T ;
	string line;
	for( int i=1; i<= T; ++i )
	{
		cin >> R >> C;
		memset( tile, 0, sizeof( tile ) );
		nBlue=0;
		for( int j=0;j<R;++j )
		{
			cin >> line;
			for ( int k=0; k<C; ++k )
			{
				tile[j][k] = line[k];
				if( line[k]=='#' )
					++nBlue;
			}
		}
		

		int error=0;
		cout << "Case #" << i << ":" << endl;
		if( nBlue %4 != 0 )
		{
			cout << "Impossible" << endl;
			continue;
		}

		for( int j=0;j<R-1;++j )
		{
			for( int k=0; k<C-1; ++k )
			{
				if( tile[j][k]=='#' )
				{
					if( tile[j][k+1] !='#' || tile[j+1][k] != '#' || tile[j+1][k+1] != '#' )
						goto OUT;
					else
					{
						tile[j][k] = tile[j+1][k+1] = '/';
						tile[j+1][k] = tile[j][k+1] = '\\';
						nBlue -= 4;
					}
				}
			}
		}
OUT:
		if( nBlue )
			cout << "Impossible" << endl;
		else
		{
			for( int j=0; j< R; ++ j )
				cout << tile[j] << endl;
		}
	}

	return 0;
}
