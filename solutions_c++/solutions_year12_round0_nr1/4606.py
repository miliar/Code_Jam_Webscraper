#include<iostream>
#include<vector>
#include<map>
#include<fstream>

using namespace std;

int main()
{
	ifstream fin ("in.in");
	ofstream fout ("out.out");
	string s;
	int caso = 1;
	int T;
	fin >> T;
	getline(fin,s);
	map<char,char> m;
	m[' '] = ' ';
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x';
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k';
	m['p'] = 'r';
	m['q'] = 'z';
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q';
	for (; T > 0; T--)
	{
		getline(fin,s);
		fout << "Case #" << caso << ": ";
		for (int i = 0; i < s.size(); i++)
		{
			fout << m[s[i]];
		}
		fout << endl;
		caso++;
	}
	
}
