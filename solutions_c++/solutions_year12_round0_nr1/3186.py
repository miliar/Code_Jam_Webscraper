#include <iostream>
#include <fstream>
#include <istream>
using namespace std;

int main() {
	ifstream inputFile;
	char line[1024];
	int count, i, j;
	cin >> count;
	cin.getline( line, 100 );
	for( j = 1; j <= count; j++ ) { 
		cin.getline( line, 1024 );
		// Go through and change all letters
		for( i = 0; i < strlen( line ); i++ ) {
			if( line[i] == 'a' )
				line[i] = 'y';
			else if( line[i] == 'b' )
				line[i] = 'h';
			else if( line[i] == 'c' )
				line[i] = 'e';
			else if( line[i] == 'd' )
				line[i] = 's';
			else if( line[i] == 'e' )
				line[i] = 'o';
			else if( line[i] == 'f' )
				line[i] = 'c';
			else if( line[i] == 'g' )
				line[i] = 'v';
			else if( line[i] == 'h' )
				line[i] = 'x';
			else if( line[i] == 'i' )
				line[i] = 'd';
			else if( line[i] == 'j' )
				line[i] = 'u';
			else if( line[i] == 'k' )
				line[i] = 'i';
			else if( line[i] == 'l' )
				line[i] = 'g';
			else if( line[i] == 'm' )
				line[i] = 'l';
			else if( line[i] == 'n' )
				line[i] = 'b';
			else if( line[i] == 'o' )
				line[i] = 'k';
			else if( line[i] == 'p' )
				line[i] = 'r';
			else if( line[i] == 'q' )
				line[i] = 'z';
			else if( line[i] == 'r' )
				line[i] = 't';
			else if( line[i] == 's' )
				line[i] = 'n';
			else if( line[i] == 't' )
				line[i] = 'w';
			else if( line[i] == 'u' )
				line[i] = 'j';
			else if( line[i] == 'v' )
				line[i] = 'p';
			else if( line[i] == 'w' )
				line[i] = 'f';
			else if( line[i] == 'x' )
				line[i] = 'm';
			else if( line[i] == 'y' )
				line[i] = 'a';
			else if( line[i] == 'z' )
				line[i] = 'q';
		}
		cout << "Case #" << j << ": " << line << "\n";
	}
}