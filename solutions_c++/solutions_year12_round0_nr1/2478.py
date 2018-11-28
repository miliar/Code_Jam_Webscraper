#include <iostream>

using namespace std;

char fromGooglerese[ 26 ] = 
{
	'y',
	'h',
	'e',
	's',
	'o',
	'c',
	'v',
	'x',
	'd',
	'u',
	'i',
	'g',
	'l',
	'b',
	'k',
	'r',
	'z',
	't',
	'n',
	'w',
	'j',
	'p',
	'f',
	'm',
	'a',
	'q',
};

char toGooglerese[ 26 ] = 
{
	'y',
	'n',
	'f',
	'i',
	'c',
	'w',
	'l',
	'b',
	'k',
	'u',
	'o',
	'm',
	'x',
	's',
	'e',
	'v',
	'z',
	'p',
	'd',
	'r',
	'j',
	'y',
	't',
	'h',
	'a',
	'q',
	
};

int main( int argc, char* argv[] )
{
	int num;
	std::string line;
	cin >> num;
	getline( cin, line );
	int cur = 0;
	while (cur++ < num)
	{
		cout << "Case #" << cur << ": ";
		getline( cin, line );
		for ( int i = 0; i < line.size(); i++ )
		{
			if ( line.at( i ) == ' ' )
			{
				cout << " ";
				continue;
			}
			char c = fromGooglerese[ tolower( line.at( i ) ) - 'a' ];
			cout << c;
		}
		cout << "\n";
	}
	return 0;
}
