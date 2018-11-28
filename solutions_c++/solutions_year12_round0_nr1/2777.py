#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <map>

using namespace std;

int main(int argc, char* argv)
{
	map<char, char> lib;
	
	lib['a'] = 'y';
	lib['b'] = 'h';
	lib['c'] = 'e';
	lib['d'] = 's';
	lib['e'] = 'o';
	lib['f'] = 'c';
	lib['g'] = 'v';
	lib['h'] = 'x';
	lib['i'] = 'd';
	lib['j'] = 'u';
	lib['k'] = 'i';
	lib['l'] = 'g';
	lib['m'] = 'l';
	lib['n'] = 'b';
	lib['o'] = 'k';
	lib['p'] = 'r';
	lib['q'] = 'z';
	lib['r'] = 't';
	lib['s'] = 'n';
	lib['t'] = 'w';
	lib['u'] = 'j';
	lib['v'] = 'p';
	lib['w'] = 'f';
	lib['x'] = 'm';
	lib['y'] = 'a';
	lib['z'] = 'q';
	lib[' '] = ' ';
	
	string line;
	
	int cases;
	cin >> cases;
	
	cin.ignore();
	
	for(int i = 0; i < cases; i++)
	{
		line = "";
		char bits[102];
		cin.getline(bits, 101);
		
		for(int j = 0; j < strlen(bits); j++)
		{
			char temp = bits[j];
			line = line + lib[temp];
		}	
		
		cout << "Case #" << (i+1) << ": " << line << endl;
	}
	
	return 0;
}
