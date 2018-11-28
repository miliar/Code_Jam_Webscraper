#include <iostream>
#include <map>
#include <cstring>

using namespace std;

int main(){
	char alp[300];
	
	alp[' '] = ' ';
	alp['a'] = 'y';
	alp['b'] = 'h';
	alp['c'] = 'e';
	alp['d'] = 's';
	alp['e'] = 'o';
	alp['f'] = 'c';
	alp['g'] = 'v';
	alp['h'] = 'x';
	alp['i'] = 'd';
	alp['j'] = 'u';
	alp['k'] = 'i';
	alp['l'] = 'g';
	alp['m'] = 'l';
	alp['n'] = 'b';
	alp['o'] = 'k';
	alp['p'] = 'r';
	alp['q'] = 'z';
	alp['r'] = 't';
	alp['s'] = 'n';
	alp['t'] = 'w';
	alp['u'] = 'j';
	alp['v'] = 'p';
	alp['w'] = 'f';
	alp['x'] = 'm';
	alp['y'] = 'a';
	alp['z'] = 'q';

	int n;
	char nc[100];
	cin >> n;
	cin.getline(nc, 100);
	
	for(int i = 0; i < n; i++){
		if(i>0)cout << endl;
		cout<< "Case #"<<i+1<<": ";
		char a[101];
		cin.getline(a, 200);
		for(int j = 0; j < strlen(a); j++)
			cout << alp[a[j]];
	}
	
	
	/*
	int n;
	char nc[100];
	cin >> n;
	cin.getline(nc, 100);

	map<char, char> alphabet;
	
	for(int i = 0; i < n; i++){
		char a[101], b[101];
		cin.getline(a, 100);
		cin.getline(b, 100);
		
		cout << a << endl <<  b << endl;
		for(int j = 0; j < strlen(a); j++)
			alphabet[a[j]] = b[j];
	}
	
	for(map<char,char>::iterator it = alphabet.begin(); it != alphabet.end(); ++it) {
		cout << "alp['" << it->first << "'] = '" << it->second << "';" << endl;
	}
	cout << "alp['z'] = 'q';" << endl;
	*/
}
