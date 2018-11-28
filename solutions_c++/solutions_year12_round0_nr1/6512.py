#include <iostream>
#include <map>
#include <cstdio>
#include <cstring>
using namespace std;

int main(int argc, char *argv[]) {
	
	map<char, char> googlerese;
		
	googlerese['a'] = 'y'; googlerese['b'] = 'h';
	googlerese['c'] = 'e'; googlerese['d'] = 's';
	googlerese['e'] = 'o'; googlerese['f'] = 'c';
	googlerese['g'] = 'v'; googlerese['h'] = 'x';
	googlerese['i'] = 'd'; googlerese['j'] = 'u';
	googlerese['k'] = 'i'; googlerese['l'] = 'g';
	googlerese['m'] = 'l'; googlerese['n'] = 'b';
	googlerese['o'] = 'k'; googlerese['p'] = 'r';
	googlerese['q'] = 'z'; googlerese['r'] = 't';
	googlerese['s'] = 'n'; googlerese['t'] = 'w';
	googlerese['u'] = 'j'; googlerese['v'] = 'p';
	googlerese['w'] = 'f'; googlerese['x'] = 'm';	
	googlerese['y'] = 'a'; googlerese['z'] = 'q';
	
	int numCasos;
	char cadena[101];
	
	cin >> numCasos;
	scanf("\n");
	
	for (int i = 1; i <= numCasos; i++) {
		cadena[0]='\0';
		scanf("%[^\n]", cadena);
		
		cout << "Case #" << i << ": ";
		
		int j = 0;
		while (cadena[j] != '\0') {
			if (cadena[j] == ' ')
				cout << (char)32;
			else
				cout << googlerese[cadena[j]];
			j++;
		}
		getchar();
		
		if (i != numCasos)
			cout << "\n";		
	}	

	return 0;
}
