#include <map>
#include <cstring>
#include <sstream>
#include <iostream>

using namespace std;

int main() {
	//map<char, char> m;
	char m[200];
	m['y']='a'; m['n']='b'; m['f']='c'; m['i']='d'; m['c']='e'; 
	m['w']='f'; m['l']='g'; m['b']='h'; m['k']='i'; m['u']='j'; 
	m['o']='k';	m['m']='l'; m['x']='m'; m['s']='n'; m['e']='o'; 
	m['v']='p'; m['z']='q';	m['p']='r';	m['d']='s'; m['r']='t';	
	m['j']='u'; m['g']='v'; m['t']='w'; m['h']='x'; m['a']='y'; 
	m['q']='z'; m[' ']=' ';
	// for (int i = 0; i < 3; i++) {
		// string a, b;
		// getline(cin, a);
		// getline(cin, b);cout << a << endl << b << endl;
		// for (int j = 0; j < a.size(); j++)
			// m[b[j]] = a[j];
	// }
	// map <char, char> :: iterator it;
	// for (it = m.begin(); it != m.end(); it++)
		// cout << "m['" << (*it).second << "']=" << "'" << (*it).first<< "'; ";
	int n;
	string a;
	cin >> n;
	getline(cin, a);
	for (int i = 0; i < n; i++) {
		getline(cin, a);
		cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < a.size(); j++)
			cout << m[(int)a[j]];
		cout << "\n";
	}
}
