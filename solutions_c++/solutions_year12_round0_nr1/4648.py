#include <fstream>
#include <vector>
#include <map>
#include <string>
using namespace std;

int main()
{
	int n;
	ifstream ifs("A-small-attempt0.in");
	ofstream ofs("output.txt");
	ifs >> n;
	vector<string> ar;
	string t; getline(ifs,t);
	for (int i = 0; i < n; i++)
	{
		getline(ifs,t);
		ar.push_back(t);
	}

	map<char,char> map;
	map['a'] = 'y'; map['b'] = 'h'; map['c'] = 'e'; map['d'] = 's'; map['e'] = 'o';
	map['f'] = 'c'; map['g'] = 'v'; map['h'] = 'x'; map['i'] = 'd'; map['j'] = 'u';
	map['k'] = 'i'; map['l'] = 'g'; map['m'] = 'l'; map['n'] = 'b'; map['o'] = 'k';
	map['p'] = 'r'; map['q'] = 'z'; map['r'] = 't'; map['s'] = 'n'; map['t'] = 'w';
	map['u'] = 'j'; map['v'] = 'p'; map['w'] = 'f'; map['x'] = 'm'; map['y'] = 'a'; map['z'] = 'q';
	map[' '] = ' ';

	for (int i = 0; i < n; i++)
	{
		ofs << "Case #" << (i+1) << ": ";
		for (int j = 0; j < ar[i].size(); j++)
			ofs << map[ar[i][j]];
		ofs << endl;
	}

}