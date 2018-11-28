#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

char dicc(char letra){
	switch(letra){
	case ' ':
		return ' ';
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
	case '3':
		return '4';
	}
}

int main() {
    ifstream entrada("A-Small.in");
    ofstream salida("A-Small.out");
    int Casos;
    string frase;
    entrada >> Casos;
	int j=1;
	getline(entrada,frase);
//    for(int caso=1; caso<=Casos; caso++){
	while(getline(entrada,frase)){
        salida << "Case #" << j << ": ";
	for(int i=0;i<frase.length();i++){
	salida << dicc(frase[i]);}
	salida << endl;
	j++;
	}
//    }
    return 0;
}
