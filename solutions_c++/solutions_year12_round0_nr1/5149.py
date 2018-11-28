#include <iostream>
#include <fstream>
#include <string>
#include <map>


//I could use a normal array but the map makes the intent clear

using namespace std;


int main ()
{
	ifstream in("input.in");
	ofstream out("output.out");
	char m[256];
	m['a']  = 'y';//
	m['b']  = 'h';//
	m['c']  = 'e';//
	m['d']  = 's';//
	m['e']  = 'o';//
	m['f']  = 'c';//
	m['g']  = 'v';//
	m['h']  = 'x';//
	m['i']  = 'd';//
	m['j']  = 'u';//
	m['k']  = 'i';//
	m['l']  = 'g';//
	m['m']  = 'l';//
	m['n']  = 'b';//
	m['o']  = 'k';//
	m['p']  = 'r';//
	m['q']  = 'z';//
	m['r']  = 't';//
	m['s']  = 'n';//
	m['t']  = 'w';//
	m['u']  = 'j';//
	m['v']  = 'p';//
	m['w']  = 'f';//
	m['x']  = 'm';//
	m['y']  = 'a';//
	m['z']  = 'q';//
	m[' ']  = ' ';

	int T;
	in >> T;
	in.ignore();
	string s;
	for (int i = 1 ; i <= T; ++i)
	{
		getline(in,s);
		for (int j =0 ; j < s.length(); ++j)
			s[j] = m[s[j]];
		out << "Case #" << i << ": " << s << '\n';
	}
	return 0;
}
