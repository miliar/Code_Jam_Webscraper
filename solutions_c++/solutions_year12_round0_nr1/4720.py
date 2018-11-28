#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <fstream>
using namespace std;

int main(int argc, char **argv)
{
	map<char, char> rMap;
	rMap['y'] = 'a';
	rMap['e'] = 'o';
	rMap['q'] = 'z';
	rMap['z'] = 'q';
	rMap['j'] = 'u';
	rMap['p'] = 'r';
	rMap['m'] = 'l';
	rMap['s'] = 'n';
	rMap['l'] = 'g';
	rMap['c'] = 'e';
	rMap['k'] = 'i';
	rMap['d'] = 's';
	rMap['x'] = 'm';
	rMap['v'] = 'p';
	rMap['n'] = 'b';
	rMap['r'] = 't';
	rMap['i'] = 'd';
	rMap['b'] = 'h';
	rMap['t'] = 'w';
	rMap['a'] = 'y';
	rMap['h'] = 'x';
	rMap['w'] = 'f';
	rMap['f'] = 'c';
	rMap['o'] = 'k';
	rMap['u'] = 'j';
	rMap['g'] = 'v';
	rMap[' '] = ' ';
	ifstream ifstr;
	ifstr.open("input.txt", ios::in);
	int T;
	char buffer[101];
	memset(buffer, 0, 101);
	ifstr.getline(buffer, 101, '\n');
	sscanf(buffer, "%d", &T);
	ofstream ofstr;
	ofstr.open("output.txt", ios::out);

	for (int i = 0; i < T; i++)
	{
		
		memset(buffer, 0, 101);
		ifstr.getline(buffer, 101, '\n');
		ofstr << "Case #" << i+1 << ": ";
		for (int j = 0; j < strlen(buffer); j++)
			ofstr << rMap[buffer[j]];
		ofstr << endl;
	}
	ofstr.close();
	ifstr.close();
	return 0;
}




