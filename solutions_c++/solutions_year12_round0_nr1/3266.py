#include <iostream>
#include <map>
#include <sstream>
#include <stdio.h>

using namespace std;

int main(int argc, char *argv[]) {
	map<char, char> m;
	
	m['a'] = 'y';
	m['b'] = 'h';
	m['c'] = 'e';
	m['d'] = 's';
	m['e'] = 'o';
	m['f'] = 'c';
	m['g'] = 'v';
	m['h'] = 'x'; // ?
	m['i'] = 'd';
	m['j'] = 'u';
	m['k'] = 'i';
	m['l'] = 'g';
	m['m'] = 'l';
	m['n'] = 'b';
	m['o'] = 'k'; //a b c d e f g h i j k l m n o p r s t u v w y z 
	m['p'] = 'r'; // q x
	m['q'] = 'z';
	m['r'] = 't';
	m['s'] = 'n';
	m['t'] = 'w';
	m['u'] = 'j';
	m['v'] = 'p';
	m['w'] = 'f';
	m['x'] = 'm';
	m['y'] = 'a';
	m['z'] = 'q'; // ?
	
	int t; 
	cin >> t;
	
	getchar();
	for(int ncaso = 1; ncaso <= t; ++ ncaso){
		string frase;
		getline(cin, frase);
		
		cout << "Case #" << ncaso << ": ";
		
		int len = frase.size();
		for(int i = 0; i < len; ++ i){
			if(frase[i] == ' ') cout << ' ';
			else cout << m[frase[i]];
		}
		
		cout << endl;
	
	}
	
	return 0;
}

