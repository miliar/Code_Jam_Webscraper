
#include <iostream>

#include <vector>
#include <string>

using namespace std;

int tests;


int main()
{
	cin >> tests;

	for( int curTest=0; curTest<tests; ++curTest )
	{

		int r, c;
		cin >> r >> c;
		vector<string> line( r, string() );
		for( int i=0; i<r; ++i )
			cin >> line[i];
		bool b_ok = true;
		for( int i=0; i<r; ++i )
			for( int j=0; j<line[i].size(); ++j )
			{
				if ( line[i][j] == '#' )
				{
					if ( i+1 >= r || j+1 >= c )
						b_ok = false;
					else
					{
						if ( line[i][j] == '#' && line[i+1][j] == '#' && line[i][j+1] == '#' && line[i+1][j+1] == '#' )
						{
							line[i][j] = line[i+1][j+1] = '/';
							line[i+1][j] = line[i][j+1] = '\\';
						}
					}
				}
			}
		for( int i=0; i<r; ++i )
			for( int j=0; j<c; ++j )
			{
				if ( line[i][j] == '#' )
					b_ok = false;
			}

		cout << "Case #" << (curTest+1) << ": " << endl;
		if ( b_ok )
			for( int i=0; i<r; ++i )
				cout << line[i] << endl;
		else
			cout << "Impossible" << endl;
	}

	return 0;
}

