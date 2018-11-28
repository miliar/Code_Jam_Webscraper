# include <iostream>
# include <fstream>

using namespace std;


int convert ( char str[8][8], int row, int col )
{
	for ( int i=0; i<row; i++ )
	{
		for ( int j=0; j<col; j++ )
		{
			if ( str[i][j] == '#' )
			{
			
				if ( str[i][j+1] != '#' || str[i+1][j] != '#' || str[i+1][j+1] != '#' )
								return 0;

				str[i][j] = '//';
				str[i][j+1] = '\\';
				str[i+1][j] = '\\';
				str[i+1][j+1] = '//';
	
			}
		}

	}

return 1;
}


int main()
{

	int T=0, row=0, col=0, counter=1, i=0;
	char str [8][8];

	ifstream ifptr;
	ofstream ofptr;

	ifptr.open ( "A-small-attempt1 (1).in" );
	ofptr.open ( "out.txt" );

	ifptr >> T;

	while ( T )
	{
		ifptr >> row >> col;


		ifptr.getline ( str[0], 6 );

		for ( i=0; i<row; i++ )
		{
			ifptr.getline ( str[i], 8 );
		}
	
	
		ofptr << "Case #" << counter << endl;

		if ( convert ( str, row, col ) )
		{
			for ( i=0; i<row; i++ )
			{
				ofptr << str[i] << endl;
			}
		
		}
		else
			ofptr << "Impossible" << endl;


		counter++;
		T--;
	}
	



return 0;
}