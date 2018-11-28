#include <iostream>
#include <stdio.h>
#include<stdlib.h>
#include <map>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char *argv[]) {
	
	map<char,char> transf;
	
	transf.insert(make_pair('a','y'));
	transf.insert(make_pair('b','h'));
	transf.insert(make_pair('c','e'));
	transf.insert(make_pair('d','s'));
	transf.insert(make_pair('e','o'));
	transf.insert(make_pair('f','c'));
	transf.insert(make_pair('g','v'));
	transf.insert(make_pair('h','x'));
	transf.insert(make_pair('i','d'));
	transf.insert(make_pair('j','u'));
	transf.insert(make_pair('k','i'));
	transf.insert(make_pair('l','g'));
	transf.insert(make_pair('m','l'));
	transf.insert(make_pair('n','b'));
	transf.insert(make_pair('o','k'));
	transf.insert(make_pair('p','r'));
	transf.insert(make_pair('q','z'));
	transf.insert(make_pair('r','t'));
	transf.insert(make_pair('s','n'));
	transf.insert(make_pair('t','w'));
	transf.insert(make_pair('u','j'));
	transf.insert(make_pair('v','p'));
	transf.insert(make_pair('w','f'));
	transf.insert(make_pair('x','m'));
	transf.insert(make_pair('y','a'));
	transf.insert(make_pair('z','q'));
	
	int casos;
	string cadena;
	string linea;
	ifstream entrada("entrada.txt");
	ofstream salida("salida.txt");
	

	getline(entrada, cadena);
	
	casos = atoi(cadena.c_str()); ;
	
	for(int i = 0; i < casos; i++){
	
		getline(entrada, cadena);
		unsigned int tam = cadena.size();
		for(unsigned int j = 0; j < tam; j++){
			if('a' <= cadena[j] && cadena[j] <= 'z')
				cadena[j] = transf[cadena[j]];
			
		}
		
		salida << "Case #" << i + 1 << ": " << cadena << endl;
		
	}
	
	return 0;
}

