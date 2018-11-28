#include <iostream>
#include <map>
#include <string>
#include <fstream>

using namespace std;

int main( int argc, char **argv )
{
	map<char,char> m;
	m['a']='y';
	m['b']='h';
	m['c']='e';
	m['d']='s';
	m['e']='o';
	m['f']='c';
	m['g']='v';
	m['h']='x';
	m['i']='d';
	m['j']='u';
	m['k']='i';
	m['l']='g';
	m['m']='l';
	m['n']='b';
	m['o']='k';
	m['p']='r';
	m['q']='z';
	m['r']='t';
	m['s']='n';
	m['t']='w';
	m['u']='j';
	m['v']='p';
	m['w']='f';
	m['x']='m';
	m['y']='a';
	m['z']='q';
	m[' ']=' ';
	m['\n']='\n';
	string s;
	int n;
	ifstream fin(argv[1]);
	fin >> n;
	getline( fin, s );
	for( int k = 1; k <= n; k++ ) {
		getline( fin, s );
		cout << "Case #" << k << ": ";
		for( int i = 0; i < s.length(); i++ )
			cout << m[s[i]];
		cout << endl;
	}
	return 0;
}
