#include <fstream>
#include <map>
#include <string>
using namespace std;


int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	map<char,char> translate;
	int T, t, i;
	char buffer[1024];
	string input;
	
	translate['a'] = 'y';
	translate['b'] = 'h';
	translate['c'] = 'e';
	translate['d'] = 's';
	translate['e'] = 'o';
	translate['f'] = 'c';
	translate['g'] = 'v';
	translate['h'] = 'x';
	translate['i'] = 'd';
	translate['j'] = 'u';
	translate['k'] = 'i';
	translate['l'] = 'g';
	translate['m'] = 'l';
	translate['n'] = 'b';
	translate['o'] = 'k';
	translate['p'] = 'r';
	translate['q'] = 'z';
	translate['r'] = 't';
	translate['s'] = 'n';
	translate['t'] = 'w';
	translate['u'] = 'j';
	translate['v'] = 'p';
	translate['w'] = 'f';
	translate['x'] = 'm';
	translate['y'] = 'a';
	translate['z'] = 'q';
	translate[' '] = ' ';
	
	fin >> T;
	fin.getline(buffer, 1024);
	
	for (t = 1; t <= T; t++) {
		fin.getline(buffer, 1024);
		input = buffer;
		
		for (i = 0; i < input.length(); i++)
			input[i] = translate[input[i]];
		
		fout << "Case #" << t << ": " << input << endl;
	}
	
	fin.close();
	fout.close();
	
	return 0;
}
