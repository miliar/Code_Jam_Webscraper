#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
	map <char,char> m;
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
	int cases;
	cin >> cases;
	string s;
	getline(cin,s);
	for (int caseno = 1; caseno <= cases; caseno++) {
		cout << "Case #" << caseno << ": ";
		getline(cin,s);
		for (int i = 0; i < s.length(); i++) {
			cout << m[s[i]];
		}
		cout << endl;
	}
}