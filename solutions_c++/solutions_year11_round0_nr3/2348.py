#include <vector>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>

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

vint representacionBinaria(long long int x){
	vint representacion;
	while(x > 0){
		representacion.push_back(x % 2);
		x = x / 2;
	}
	return representacion;
}

long long int sumaEspecial(long long int x, long long int y){
	vint binX = representacionBinaria(x);
	vint binY = representacionBinaria(y);
	long long int solucion = 0;
	long long int z = min(x,y);
	forn(i, representacionBinaria(z).size()){
		if(binX[i] != binY[i]){
			solucion += pow(2, i);
		}
	}
	forsn(i, representacionBinaria(min(x,y)).size(), representacionBinaria(max(x,y)).size()){
		if(x > y){
			solucion += pow(2, i) * binX[i];
		}else{
			solucion += pow(2, i) * binY[i];
		}
	}
	return solucion;
}

bool cargarResolverProblema(ifstream &entrada, long long int& cantidad){
	int caramelos;
	entrada >> caramelos;	
	entrada >> cantidad; //N >= 2 para todos los casos
	long long int minimo = cantidad;
	long long int cantidadEspecial = cantidad;
	forsn(i, 1, caramelos){
		long long int caramelo;
		entrada >> caramelo;
		cantidadEspecial = sumaEspecial(cantidadEspecial, caramelo);

		minimo = min(minimo, caramelo);
		cantidad += caramelo;		
	}
	cantidad -= minimo;
	return cantidadEspecial == 0;
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
			long long int cantidadSolucion;
			salida << "Case #" << indiceProblemas + 1 << ": ";
			if(cargarResolverProblema(entrada,cantidadSolucion)){
				salida << cantidadSolucion;
			}else{
				salida << "NO";
			}
			salida fL;
		}
		salida.close();
		entrada.close();
	}
	return 0;
}
