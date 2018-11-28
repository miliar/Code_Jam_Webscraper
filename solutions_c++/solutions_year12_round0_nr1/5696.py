#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	
	map<char, char> mapaletras;
	
	mapaletras['a']='y';
	mapaletras['b']='h';
	mapaletras['c']='e';
	mapaletras['d']='s';
	mapaletras['e']='o';
	mapaletras['f']='c';
	mapaletras['g']='v';
	mapaletras['h']='x';
	mapaletras['i']='d';
	mapaletras['j']='u';
	mapaletras['k']='i';
	mapaletras['l']='g';
	mapaletras['m']='l';
	mapaletras['n']='b';
	mapaletras['o']='k';
	mapaletras['p']='r';
	mapaletras['q']='z';
	mapaletras['r']='t';
	mapaletras['s']='n';
	mapaletras['t']='w';
	mapaletras['u']='j';
	mapaletras['v']='p';
	mapaletras['w']='f';
	mapaletras['x']='m';
	mapaletras['y']='a';
	mapaletras['z']='q';
	mapaletras[' ']=' ';
	
	int T;
	cin >> T;
	cin.ignore();
	
	for (int i=1; i<=T; i++){

		string linea;
		getline(cin, linea);
	
		cout << "Case #" << i << ": ";
		for (int i=0; i<linea.size(); i++)
			cout << mapaletras[ linea[i] ];

		cout << endl;
		}
	return 0;
}
