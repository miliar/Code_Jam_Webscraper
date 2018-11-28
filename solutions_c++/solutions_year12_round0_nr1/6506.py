#include <iostream>
#include <cstdio>
#include <iterator>
using namespace std;

char getLetra(char letra) {
	switch(letra) {
	case 'a':
		return 'y';
	case 'b':
		return 'h';
	case 'c':
		return 'e';
	case 'd':
		return 's';
	case 'e':
		return 'o';
	case 'f':
		return 'c';
	case 'g':
		return 'v';
	case 'h':
		return 'x';
	case 'i':
		return 'd';
	case 'j':
		return 'u';
	case 'k':
		return 'i';
	case 'l':
		return 'g';
	case 'm':
		return 'l';
	case 'n':
		return 'b';
	case 'o':
		return 'k';
	case 'p':
		return 'r';
	case 'q':
		return 'z';
	case 'r':
		return 't';
	case 's':
		return 'n';
	case 't':
		return 'w';
	case 'u':
		return 'j';
	case 'v':
		return 'p';
	case 'w':
		return 'f';
	case 'x':
		return 'm';
	case 'y':
		return 'a';
	case 'z':
		return 'q';
	case ' ':
		return (char) 32;
	}
}

int main(int argc, char *argv[]) {
	
	char entrada[101];
	int repeticiones;
	
	cin >> repeticiones;
	cin.clear();
	cin.ignore();
	
	for(int i=0; i<repeticiones; i++) {
		gets(entrada);
		
		for (int p=0; entrada[p] != '\0'; p++) {        
			//cout << getLetra(entrada[p]) << endl;
			entrada[p] = getLetra(entrada[p]);
		}
		cout << "Case #" << i+1 << ": " << entrada;
		if(i+1 != repeticiones)
			cout << endl; 
	}
	
	return 0;
}

