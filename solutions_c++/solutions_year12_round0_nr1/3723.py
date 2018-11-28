#include<iostream>
#include<string>
#include<map>
using namespace std;

int main(){
	int n,i=0,j;
	cin>>n;
	string str[n];
	getline (cin, str[i]);
	for(i=0;i<n;i++){
		getline (cin, str[i]);
	}

	
	map<char,char> charmap;
	
	charmap[' '] = ' ';
	charmap['a'] = 'y';
	charmap['b'] = 'h';
	charmap['c'] = 'e';
	charmap['d'] = 's';
	charmap['e'] = 'o';
	charmap['f'] = 'c';
	charmap['g'] = 'v';
	charmap['h'] = 'x';
	charmap['i'] = 'd';
	charmap['j'] = 'u';
	charmap['k'] = 'i';
	charmap['l'] = 'g';
	charmap['m'] = 'l';
	charmap['n'] = 'b';
	charmap['o'] = 'k';
	charmap['p'] = 'r';
	charmap['q'] = 'z';
	charmap['r'] = 't';
	charmap['s'] = 'n';
	charmap['t'] = 'w';
	charmap['u'] = 'j';
	charmap['v'] = 'p';
	charmap['w'] = 'f';
	charmap['x'] = 'm';
	charmap['y'] = 'a';
	charmap['z'] = 'q';

	for(i=0;i<n;i++){
		for(j=0;j<str[i].length();j++){
			str[i][j] = charmap[ str[i][j] ];
		}
	}
	
	for(i=0;i<n;i++){
		cout<<"Case #"<<i+1<<": "<<str[i]<<endl;
	}
	
	return 0;
}
