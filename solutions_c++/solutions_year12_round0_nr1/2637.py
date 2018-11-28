#include <iostream>
#include <sstream>
#include <map>

using namespace std;



int main()
{
	char repMap[256] = {0};
	
	repMap[' '] = ' ';
	repMap['a'] = 'y';
	repMap['b'] = 'h';
	repMap['c'] = 'e';
	repMap['d'] = 's';
	repMap['e'] = 'o';
	repMap['f'] = 'c';
	repMap['g'] = 'v';
	repMap['h'] = 'x';
	repMap['i'] = 'd';
	repMap['j'] = 'u';
	repMap['k'] = 'i';
	repMap['l'] = 'g';
	repMap['m'] = 'l';
	repMap['n'] = 'b';
	repMap['o'] = 'k';
	repMap['p'] = 'r';
	repMap['q'] = 'z';		// ?
	repMap['r'] = 't';
	repMap['s'] = 'n';
	repMap['t'] = 'w';
	repMap['u'] = 'j';
	repMap['v'] = 'p';
	repMap['w'] = 'f';
	repMap['x'] = 'm';
	repMap['y'] = 'a';
	repMap['z'] = 'q';		// ?

	int nbCases;
	cin >> nbCases;
	
	string nullLine;
	getline(cin, nullLine);
	
	for(int i=0 ; i<nbCases ; i++)
	{
		string line;
		getline(cin, line);
		
		for(int j=0 ; j<line.size() ; j++)
		{
			char val = repMap[line[j]];
			
			if(val == 0)
				line[j] -= 'a'-'A';
			else
				line[j] = val;
		}
		
		cout << "Case #" << (i+1) << ": ";
		cout << line << endl;
	}
	
	return 0;
}



