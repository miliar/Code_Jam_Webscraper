#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <iterator>
#include <cstdio>
using namespace std;

int main(int argc, char *argv[]) {
	
	int repeticiones;
	char linea[100];
	char letra;
	map<char, char> transformador;
	pair<char, char> par;
	vector<string> frases;
	string datos = "";
		
	par.first = 'a';
	par.second = 'y';
	transformador.insert(par);
	
	par.first = 'b';
	par.second = 'h';
	transformador.insert(par);
	
	par.first = 'c';
	par.second = 'e';
	transformador.insert(par);
	
	par.first = 'd';
	par.second = 's';
	transformador.insert(par);
	
	par.first = 'e';
	par.second = 'o';
	transformador.insert(par);
	
	par.first = 'f';
	par.second = 'c';
	transformador.insert(par);
	
	par.first = 'g';
	par.second = 'v';
	transformador.insert(par);
	
	par.first = 'h';
	par.second = 'x';
	transformador.insert(par);
	
	par.first = 'i';
	par.second = 'd';
	transformador.insert(par);
	
	par.first = 'j';
	par.second = 'u';
	transformador.insert(par);
	
	par.first = 'k';
	par.second = 'i';
	transformador.insert(par);
	
	par.first = 'l';
	par.second = 'g';
	transformador.insert(par);
	
	par.first = 'm';
	par.second = 'l';
	transformador.insert(par);
	
	par.first = 'n';
	par.second = 'b';
	transformador.insert(par);
	
	par.first = 'o';
	par.second = 'k';
	transformador.insert(par);
	
	par.first = 'p';
	par.second = 'r';
	transformador.insert(par);
	
	par.first = 'q';
	par.second = 'z';
	transformador.insert(par);
	
	par.first = 'r';
	par.second = 't';
	transformador.insert(par);
	
	par.first = 's';
	par.second = 'n';
	transformador.insert(par);
	
	par.first = 't';
	par.second = 'w';
	transformador.insert(par);
	
	par.first = 'u';
	par.second = 'j';
	transformador.insert(par);
	
	par.first = 'v';
	par.second = 'p';
	transformador.insert(par);
	
	par.first = 'w';
	par.second = 'f';
	transformador.insert(par);
	
	par.first = 'x';
	par.second = 'm';
	transformador.insert(par);
	
	par.first = 'y';
	par.second = 'a';
	transformador.insert(par);
	
	par.first = 'z';
	par.second = 'q';
	transformador.insert(par);
	
	par.first = ' ';
	par.second = ' ';
	transformador.insert(par);
		
	cin >> repeticiones;
	cin.ignore(1000, '\n');
	cin.clear();
	for(;repeticiones!=0;repeticiones--){
		gets(linea);
		for(int j = 0; linea[j] != '\0'; j++){
			letra=linea[j];
			map<char,char>:: iterator iter;
			for(iter = transformador.begin();iter!=transformador.end();iter++){
				if((*iter).first == letra) datos+=(*iter).second;
			}
		}
		frases.push_back(datos);
		datos.clear();
	}
	for (int i=0; i<frases.size();i++){
		cout << "Case #" << i+1 << ": " << frases.at(i) << endl;
	}
	return 0;
}

