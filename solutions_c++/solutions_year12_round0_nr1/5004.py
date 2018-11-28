#include<stdio.h>
#include<string>
#include<iostream>
#include<sstream>

using namespace std;

char mapa[400];

int main(){	

	mapa['a'] = 'y';
	mapa['b'] = 'h';
	mapa['c'] = 'e';
	mapa['d'] = 's';
	mapa['e'] = 'o';
	mapa['f'] = 'c';
	mapa['g'] = 'v';
	mapa['h'] = 'x';
	mapa['i'] = 'd';
	mapa['j'] = 'u';
	mapa['k'] = 'i';
	mapa['l'] = 'g';
	mapa['m'] = 'l';
	mapa['n'] = 'b';
	mapa['o'] = 'k';
	mapa['p'] = 'r';
	mapa['q'] = 'z';
	mapa['r'] = 't';
	mapa['s'] = 'n';
	mapa['t'] = 'w';
	mapa['u'] = 'j';
	mapa['v'] = 'p';
	mapa['w'] = 'f';
	mapa['x'] = 'm';
	mapa['y'] = 'a';
	mapa['z'] = 'q';
	mapa[' '] = ' ';
	int T, i;
	scanf("%d ", &T);
	string s;
	for(i=0; i<T; i++){
		getline(cin, s);
		for(int k=0; k<s.size(); k++){
			s[k]=mapa[s[k]];
		}
		cout << "Case #" << i+1 << ": " << s << endl;
	}
	return 0;
}
