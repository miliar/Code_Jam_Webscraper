//
//  tongues.cpp
//  qualification
//	Paul O'Neil
//

#include <iostream>
#include <map>
#include <string>
#include <array>
using namespace std;

#define LINE_LEN 100

int main(int argc, const char * argv[])
{
	map<char, char> translator;
	translator[' '] = ' ';
	translator['y'] = 'a';
	translator['n'] = 'b';
	translator['f'] = 'c';
	translator['i'] = 'd';
	translator['c'] = 'e';
	translator['w'] = 'f';
	translator['l'] = 'g';
	translator['b'] = 'h';
	translator['k'] = 'i';
	translator['u'] = 'j';
	translator['o'] = 'k';
	translator['m'] = 'l';
	translator['x'] = 'm';
	translator['s'] = 'n';
	translator['e'] = 'o';
	translator['v'] = 'p';
	translator['z'] = 'q';
	translator['p'] = 'r';
	translator['d'] = 's';
	translator['r'] = 't';
	translator['j'] = 'u';
	translator['g'] = 'v';
	translator['t'] = 'w';
	translator['h'] = 'x';
	translator['a'] = 'y';
	translator['q'] = 'z';
	
	
	int lineCount;
	cin >> lineCount;
	while( cin.get() != '\n') ;
	//std::array<char, LINE_LEN + 1> buffer; 
	for( int i = 0; i < lineCount ; ++i )
	{
		cout << "Case #" << i+1 << ": ";
		for( char ch = cin.get(); ch != '\n'; ch = cin.get() ) {
			cout << translator[ch];
		}
		cout << endl;
	}
	
	return 0;
}

