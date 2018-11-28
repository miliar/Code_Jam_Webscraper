/*
 * 2008. Gooogle Code Jam.
 * Round C
 *   A. Text Messaging Outrage
 * Code by Kyoungmoon Sun
 */

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

void process( char* filename )
{
	unsigned int caseCount, P, K, L, i, j, k, l, tmp, result;
	vector<unsigned int> pressed;
	ifstream inputfile( filename );

	if( !inputfile.is_open() )
	{
		cout << "Unable to open " << filename << endl;
		return;
	}

	inputfile >> caseCount;

	for( i = 0; i < caseCount; i++ )
	{
		pressed.clear();
		inputfile >> P;
		inputfile >> K;
		inputfile >> L;
		for( j = 0; j < L; j++ )
		{
			inputfile >> tmp;
			pressed.push_back( tmp );
		}
		sort( pressed.begin(), pressed.end(), greater<unsigned int>() );
		result = 0;
		k = 1;
		l = 0;
		for( j = 0; j < L; j++ )
		{
			if( l >= K )
			{
				l = 0;
				k++;
			}
			l++;
			result += pressed[j] * k;
		}
		cout << "Case #" << i + 1 << ": " << result << endl;
	}

	inputfile.close();
}

int main( int argc, char* argv[] )
{
	if( argc != 2 )
	{
		cout << argv[0] << " [input file]" << endl;
		return 0;
	}

	process( argv[1] );

	return 0;
}
