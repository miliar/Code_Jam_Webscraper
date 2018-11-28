#include <iostream>
#include<stdlib.h>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	
	int casos, cant, atencion, p, empleado[101], modulo, div, resultado, cont;
	string cadena;
	
	ifstream entrada("entrada.txt");
	ofstream salida("salida.txt");
	
	getline(entrada, cadena);
	
	casos = atoi(cadena.c_str());
	
	for(int t = 0; t < casos; t++){
		
		getline(entrada, cadena);
		cant = atoi(cadena.substr(0, cadena.find_first_of(" ", 0)).c_str());
		cadena = cadena.substr(cadena.find_first_of(" ", 0) + 1,cadena.size() - 1);
		atencion = atoi(cadena.substr(0, cadena.find_first_of(" ", 0)).c_str());
		cadena = cadena.substr(cadena.find_first_of(" ", 0) + 1,cadena.size() - 1);
		p = atoi(cadena.substr(0, cadena.find_first_of(" ", 0)).c_str());
		cadena = cadena.substr(cadena.find_first_of(" ", 0) + 1,cadena.size() - 1);
		resultado = 0;
		cont = atencion;
		
	for(int i = 0; i < cant; i++){
		empleado[i] = atoi(cadena.substr(0, cadena.find_first_of(" ", 0)).c_str());
		cadena = cadena.substr(cadena.find_first_of(" ", 0) + 1,cadena.size() - 1);
	}
	
	for(int j = 0; j < cant; j++){
		modulo = empleado[j] % 3;
		div = empleado[j] / 3;
		if(div >= p)
			resultado++;
		else
			if(modulo == 0 && div > 0 && cont > 0 && ((div + 1) == p)){
				resultado++;
				cont--;
			}
			else
				if(modulo == 1 && ((div + 1) == p))
					resultado++;
				else
					if(modulo == 2 && ((div + 1) == p))
						resultado++;
					else
						if(modulo == 2 && cont > 0 && ((div + 2) == p)){
							resultado++;
							cont--;
						}
			
	}
	salida << "Case #" << t + 1 << ": " << resultado << endl;
	}
	
	
	
	
	return 0;
}

