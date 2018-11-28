#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
using namespace std; 

int main(){

	freopen("Q2.in", "rt", stdin);
	freopen("Q2.out", "wt", stdout);
	
//	vector<char> bases;
	int chars[] = {'Q','W','E','R','A','S','D','F'};
  	vector<char> bases (chars, chars + sizeof(char) / sizeof(char) );
  	
	int r,T;
	int C,D,N,i,j,k;
	
	char base1;
	char base2;
	char combinacion;
	string cadena;
	string aux;
	string salida;
	string aux2;
	
	vector<string> combinaciones;
	vector<char> resultados;
	vector<string> eliminacion;
	
   cin >> T;  
   for(r=0;r<T;r++){
		cout << "Case #" << r+1 << ": ";
		cerr << "Case #" << r+1 << ": ";
		
		combinaciones.clear();
		resultados.clear();
		eliminacion.clear();
		
		cin >> C;
		for(i=0;i<C;i++){
		   cin >> cadena;
		   combinaciones.push_back(cadena.substr(0,2));
		   resultados.push_back(cadena[2]);
		   aux = cadena;
		   aux[0] = cadena[1];
		   aux[1] = cadena[0];
		   combinaciones.push_back(aux.substr(0,2)); //(base2&base1);
		   resultados.push_back(cadena[2]);
		}
		
		cin >> D;
		for(i=0;i<D;i++){
		   cin >> cadena;
		   eliminacion.push_back(cadena);
			aux = cadena;
		   aux[0] = cadena[1];
		   aux[1] = cadena[0]; 
		   eliminacion.push_back(aux); //base2+base1);
		}

      cin >> N;
		cin >> cadena;
		
		salida = cadena[0];
		for(i=1;i<cadena.size();i++){
			salida = salida.append(cadena.substr(i,1));
			if(salida.size() >1){
				//Combinaciones
				aux = salida.substr(salida.size()-2,2);
				for(j=0;j<combinaciones.size();j++){
					if(aux==combinaciones[j]){
						salida[salida.size()-2]=resultados[j];
						salida.erase(salida.size()-1);
						break;
					}
				}
				//Eliminaciones
				if(salida.size()>1){
					for(k=salida.size()-2;k>=0;k--){
						aux2 = "";
						aux2.append(salida.substr(salida.size()-1,1)).append(salida.substr(k,1));
						for(j=0;j<eliminacion.size();j++){
							if(aux2==eliminacion[j]){
								//salida.erase(k,salida.size() -k);
								salida.clear();
								salida = "";
								k = -1;
								break;
							}
						} 		
					}
				}
			} 		
		}	
		
		
		cout << "[";
		cerr << "[";
		for(i=0;i<salida.size();i++){
			if(i>0){
				cout << ", ";
				cerr << ", ";				
			}
			cout << salida[i];
			cerr << salida[i];
		}
		cout << "]" << endl;
		cerr << "]" << endl;
	}
}

