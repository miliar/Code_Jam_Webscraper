#include <iostream>
#include <string>

using namespace std;

char map[300];

void pre(){
	map['a'] = 'y'; map['j'] = 'u'; map['s'] = 'n';
	map['b'] = 'h'; map['k'] = 'i'; map['t'] = 'w';
	map['c'] = 'e'; map['l'] = 'g'; map['u'] = 'j';
	map['d'] = 's'; map['m'] = 'l'; map['v'] = 'p';
	map['e'] = 'o'; map['n'] = 'b'; map['w'] = 'f';
	map['f'] = 'c'; map['o'] = 'k'; map['x'] = 'm';
	map['g'] = 'v'; map['p'] = 'r'; map['y'] = 'a';
	map['h'] = 'x'; map['q'] = 'z'; map['z'] = 'q';
	map['i'] = 'd'; map['r'] = 't'; map[' '] = ' ';
}

int main(){
	ios::sync_with_stdio(false);
	pre();
	
	int t, c = 1;
	string line;
	cin >> t; cin.ignore();
	
	while(t--){
		getline(cin, line);
		
		cout << "Case #" << c++ << ": ";
		for(int i = 0; i < line.size(); i++){
			cout << map[line[i]];
		}
		cout << "\n";
	}
}
