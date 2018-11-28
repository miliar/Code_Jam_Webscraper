#include <iostream>
#include <fstream>
#include <map>
#include <string>

using namespace std;

map<char, char> trans;

int main()
{
	trans['a'] = 'y';
	trans['b'] = 'h';
	trans['c'] = 'e';
	trans['d'] = 's';
	trans['e'] = 'o';
	trans['f'] = 'c';
	trans['g'] = 'v';
	trans['h'] = 'x';
	trans['i'] = 'd';
	trans['j'] = 'u';
	trans['k'] = 'i';
	trans['l'] = 'g';
	trans['m'] = 'l';
	trans['n'] = 'b';
	trans['o'] = 'k';
	trans['p'] = 'r';
	trans['q'] = 'z';
	trans['r'] = 't';
	trans['s'] = 'n';
	trans['t'] = 'w';
	trans['u'] = 'j';
	trans['v'] = 'p';
	trans['w'] = 'f';
	trans['x'] = 'm';
	trans['y'] = 'a';
	trans['z'] = 'q';
	trans[' '] = ' ';
	ifstream in("tongues.in");
	ofstream out("tongues.out");
	int n;
	in >> n;
	string trash;
	getline(in, trash);
	for (int i = 0; i < n; i++)
	{
		string str;
		getline(in, str);
		for (int j = 0; j < str.length(); j++)
			str[j] = trans[str[j]];
		out << "Case #" << (i + 1) << ": " << str << "\n";
	}
	return 0;
}
