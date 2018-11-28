#include <iostream>
#include <fstream>

using namespace std;

ifstream inf( "A-large.in" );
ofstream outf( "A-large-res.out" );

int main()
{
	int it, T;
	//cin >> T;
	inf >> T;
	
	for ( it = 1; it <= T; ++it )
	{
		
		char A[55][55] = {};
		bool Fail = false;
		int i, j, R, C;
		//cin >> R >> C;
		inf >> R >> C;
		
		for ( i = 1; i <= R; ++i )
			for ( j = 1; j <= C; ++j )
				inf >> A[i][j];
				//cin >> A[i][j];
		
		for ( i = 1; i <= R && !Fail; ++i )
			for ( j = 1; j <= C && !Fail; ++j )
				if ( A[i][j] == '#' )
				{
					if ( A[i + 1][j] == '#' && A[i][j + 1] == '#' && A[i + 1][j + 1] == '#' )
					{
						A[i + 1][j] = A[i][j + 1] = '\\'; 
						A[i][j] = A[i + 1][j + 1] = '/';
					}
					else
						Fail = true;
				}
		
		outf << "Case #" << it << ":" << endl;	
		if ( Fail )
			outf << "Impossible" << endl;
		else
			for ( i = 1; i <= R; outf << endl, ++i )
				for ( j = 1; j <= C; ++j )
					outf << A[i][j];
		/*		
		cout << "Case #" << it << ":" << endl;	
		if ( Fail )
			cout << "Impossible" << endl;
		else
			for ( i = 1; i <= R; cout << endl, ++i )
				for ( j = 1; j <= C; ++j )
					cout << A[i][j];*/
		
	}
	
	return 0;
}
