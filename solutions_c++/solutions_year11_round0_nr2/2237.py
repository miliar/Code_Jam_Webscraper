#include <vector>
#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

typedef vector<int> vint;
typedef vector<bool> vbool;
typedef vector<vbool> vvbool;
typedef vector<vint> vvint;
typedef vector<char> vchar;
typedef vector<vchar> vvchar;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forsn(i, s, n) for(int i=(s); i<(int)(n); ++i)
#define fL << "\n" //fin de linea
#define esp << " " <<

int hash(char base){
	int respuesta;
	switch(base){
		case 'Q':
			respuesta = 0;
			break;
		case 'W':
			respuesta = 1;
			break;
		case 'E':
			respuesta = 2;
			break;
		case 'R':
			respuesta = 3;
			break;
		case 'A':
			respuesta = 4;
			break;
		case 'S':
			respuesta = 5;
			break;
		case 'D':
			respuesta = 6;
			break;
		case 'F':
			respuesta = 7;
			break;		
		default:
			respuesta = -1;
	}
	return respuesta;
}


vchar cargarResolverProblema(ifstream &entrada){
	vchar solucion;
	vvchar compuestos(8, vchar(8, '0'));
	vvbool opuestos(8, vbool(8, false));
	vint basesPresentes(8, 0);
	
	int composiciones;
	entrada >> composiciones;
	forn(indice, composiciones){ //CARGO LAS COMPOSICIONES
		char base1, base2, compuesto;
		entrada >> base1;
		entrada >> base2;
		entrada >> compuesto;
		compuestos[hash(base1)][hash(base2)] = compuesto;
		compuestos[hash(base2)][hash(base1)] = compuesto;
	}
	
	int oposiciones;
	entrada >> oposiciones;
	forn(indice, oposiciones){ //CARGO LAS OPOSICIONES
		char base1, base2;
		entrada >> base1;
		entrada >> base2;
		opuestos[hash(base1)][hash(base2)] = true;
		opuestos[hash(base2)][hash(base1)] = true;
	}
	
	int cantidadLetras;
	entrada >> cantidadLetras;
	forn(indice, cantidadLetras){ //CARGO LAS LETRAS
		char letra;
		entrada >> letra;
		
		if(solucion.empty()){
			solucion.push_back(letra);
			basesPresentes[hash(letra)]++;
		}else{
			char ultimaLetra = solucion[solucion.size() - 1]; 
			if(hash(ultimaLetra) != -1 && compuestos[hash(ultimaLetra)][hash(letra)] != '0'){
				solucion.pop_back();
				solucion.push_back(compuestos[hash(ultimaLetra)][hash(letra)]);
				basesPresentes[hash(ultimaLetra)]--;
			}else{
				int indiceBases = 0;
				bool opuestoPresente = false;
				while(indiceBases < 8 && !opuestoPresente){
					if(basesPresentes[indiceBases] > 0 && opuestos[indiceBases][hash(letra)] == true){
						opuestoPresente = true;
						solucion.resize(0);
						forn(aux, 8){
							basesPresentes[aux] = 0;
						}
					}
					indiceBases++;
				}
				if(!opuestoPresente){
					solucion.push_back(letra);
					basesPresentes[hash(letra)]++;					
				}
			}
		}
	}	
	return solucion;
}

int main(int argc, char *argv[]){
	ifstream entrada;
	ofstream salida;
	entrada.open(argv[1]);
	if(!entrada){
		cout << "No se pudo abrir el archivo\n";
	}else{	
		salida.open("salida");
		int cantidadProblemas;
		entrada >> cantidadProblemas;
		forn(indiceProblemas, cantidadProblemas){
			vchar solucion = cargarResolverProblema(entrada);
			salida << "Case #" << indiceProblemas+1 << ": [";
			if(!solucion.empty()){
				forn(indice, solucion.size() -1){
					salida << solucion[indice] << ", ";
				}
				salida << solucion[solucion.size() - 1];
			}
			salida <<"]" fL;
		}
		salida.close();
		entrada.close();
	}
	return 0;
}
