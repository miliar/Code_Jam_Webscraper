#include <iostream>
#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(){

	map<char, char> mapin;
	
	mapin['e'] = 'o'; 
	mapin['j'] = 'u'; 
	mapin['p'] = 'r'; 
	mapin['m'] = 'l'; 
	mapin['y'] = 'a'; 
	mapin['s'] = 'n'; 
	mapin['l'] = 'g'; 
	mapin['c'] = 'e'; 
	mapin['k'] = 'i'; 
	mapin['d'] = 's'; 
	mapin['x'] = 'm'; 
	mapin['v'] = 'p'; 
	mapin['n'] = 'b'; 
	mapin['r'] = 't'; 
	mapin['h'] = 'x'; 
	mapin['t'] = 'w'; 
	mapin['a'] = 'y'; 
	mapin['f'] = 'c'; 
	mapin['o'] = 'k'; 
	mapin['u'] = 'j'; 
	mapin['g'] = 'v'; 	
	mapin['z'] = 'q';	
	mapin['i'] = 'd';
	mapin['w'] = 'f';
	mapin['b'] = 'h';
	mapin['q'] = 'z';
	mapin[' '] = ' ';
	
	int test;
	
	
	cin >> test;
	string line;
	cin.ignore();
	
	
	
	for(int i = 1; i <= test; i++){
		getline(cin, line);
		cout << "Case #" << i << ": ";
		for(int j = 0; j < line.length(); j++){
			cout << mapin[line[j]];
		}
		cout << endl;
	}
	
return 0;
}

