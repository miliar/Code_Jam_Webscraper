#include <iostream>
#include <string>
#include <stdio.h>
#include <memory.h>
using namespace std;

int main(){
	ios::sync_with_stdio(false);
	int n, caso = 1;
	freopen( "A-small-attempt0.in", "r", stdin );
	freopen( "A-small-attempt0.out", "w", stdout );
	cin >> n;
	char vet[125];
	vet['a'] = 'y'; vet['j'] = 'u'; vet['s'] = 'n';
	vet['b'] = 'h'; vet['k'] = 'i'; vet['t'] = 'w';
	vet['c'] = 'e'; vet['l'] = 'g'; vet['u'] = 'j';
	vet['d'] = 's'; vet['m'] = 'l'; vet['v'] = 'p';
	vet['e'] = 'o'; vet['n'] = 'b'; vet['w'] = 'f';
	vet['f'] = 'c'; vet['o'] = 'k'; vet['x'] = 'm';
	vet['g'] = 'v'; vet['p'] = 'r'; vet['y'] = 'a';
	vet['h'] = 'x'; vet['q'] = 'z'; vet['z'] = 'q';
	vet['i'] = 'd'; vet['r'] = 't'; vet[' '] = ' '; 
	cin.ignore();
	while(n--){
		string str;
		getline(cin,str);
		int tam = str.size();
		cout << "Case #"<< caso++ <<": ";
		for(int  i = 0; i < tam; i++){
			cout << vet[str[i]];
		}
		cout << "\n";
	}
	return 0;
}