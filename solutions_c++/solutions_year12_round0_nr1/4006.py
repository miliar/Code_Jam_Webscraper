#include <iostream>
#include <vector>
#include <map>
#include <fstream>
using namespace std;





int main()
{
	map < char,char> m;

	m['a'] ='y';
	m['b'] ='h';
	m['c'] ='e';
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
	m['z'] =  'q';
	m[' '] = ' ';
	string s;
	fstream fout("out_a.out",ios::out);
	int t;
	cin >> t;
	cin.ignore();
	int d = 0;
	while ( t-- ) {
	
	getline(cin,s);
	d++;
	for ( int i = 0; i < s.size(); i++) {
		s[i] = m[s[i]];
	}
	cout << "Case #"<<d<<": "<< s << endl;
	fout << "Case #"<<d<<": "<<s << "\n";
	}
	
	return 0;
}



