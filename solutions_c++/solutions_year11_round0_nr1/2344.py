#include <vector>
#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

typedef vector<int> vint;
typedef vector<bool> vbool;
typedef vector<vint> vvint;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forsn(i, s, n) for(int i=(s); i<(int)(n); ++i)
#define fL << "\n" //fin de linea
#define esp << " " <<


long long int cargarResolverProblema(ifstream &entrada){
	int cantidadBotones;
	long long int solucion = 0;
	long long int tiempoOrange = 0;
	long long int tiempoBlue = 0;
	int tiempoMovimiento;
	int posicionOrange = 1;
	int posicionBlue = 1;
	char bot;
	char ultimo;
	int lugar;
	
	entrada >> cantidadBotones;
	entrada >> bot;
	entrada >> lugar;
	if(bot == 'O'){
		tiempoOrange = abs(posicionOrange - lugar) + 1; //más uno para apretar el boton
		posicionOrange = lugar;
		solucion = tiempoOrange;
	}else{
		tiempoBlue = abs(posicionBlue - lugar) + 1; //más uno para apretar el boton
		posicionBlue = lugar;
		solucion = tiempoBlue;
	}
	
	ultimo = bot;
			
	forsn(movimiento, 1, cantidadBotones){
		entrada >> bot;
		entrada >> lugar;
		//cout << bot esp lugar fL;
		if(bot == 'O'){
			tiempoMovimiento = abs(posicionOrange - lugar); //más uno para apretar el boton
			posicionOrange = lugar;
			if(ultimo == 'O'){
				solucion += tiempoMovimiento + 1;
				tiempoOrange += tiempoMovimiento + 1;
			}else{				
				if(tiempoBlue - tiempoMovimiento < 0){
					solucion += abs(tiempoBlue - tiempoMovimiento) + 1;
					tiempoOrange = abs(tiempoBlue - tiempoMovimiento) + 1;
				}else{
					solucion++;
					tiempoOrange = 1;
				}
			}
		}else{
			tiempoMovimiento = abs(posicionBlue - lugar); //más uno para apretar el boton
			posicionBlue = lugar;
			if(ultimo == 'B'){
				solucion += tiempoMovimiento + 1;
				tiempoBlue += tiempoMovimiento + 1;
			}else{				
				if(tiempoOrange - tiempoMovimiento < 0){
					solucion += abs(tiempoOrange - tiempoMovimiento) + 1;
					tiempoBlue = abs(tiempoOrange - tiempoMovimiento) + 1;
				}else{
					solucion++;
					tiempoBlue = 1;
				}
			}
		}
		ultimo = bot;
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
			long long int solucion = cargarResolverProblema(entrada);
			salida << "Case #" << indiceProblemas+1 << ":" esp solucion << "\n";
		}
		salida.close();
		entrada.close();
	}
	return 0;
}
