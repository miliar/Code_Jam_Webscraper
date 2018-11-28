

	//	*****	*****	*****	AllYourBase.cpp	*****	*****	*****	\\
	//	Programa de práctica para el problema All Your Base(Belong....) de Google Jam 2k9		\\
	//	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	\\
	

 // **** **** Includes **** **** {
 
 // **** Standard Libraries ****
#include <iostream>
#include <fstream>
//#include <time.h> // constante CLOCKS_PER_SEC, funcion clock()
#include <utility> // Tipo "pair<,>" standard (pair.h para compatibilidad no standard)
//#include <stack>
#include <set>
#include <vector>
#include <map>
#include <math.h>
//#include <stdlib.h>
//#include <string.h>
//#include <stdexcept>

 // **** Custom Headers ****
//#include "header0_text.h"
//#include "header1_func.h"

 // |||||||||||||||||||||||||||||||||||||| }

 
using namespace std;
 
 
 // **** **** Defines **** **** {
//#define KNOWLEDGE "POWER"
#define nArgumentos 1 // El fichero de entrada
int numeroObjetivo=0;
 // ||||||||||||||||||||||||||||||||||||| }
 
 
 // **** **** Estructuras de datos (probablemente irán en un header a parte) **** **** {
 // ||||||||||||||||||||||||||||||||||||| }
 
 
 // **** **** Declaraciones anticipadas **** **** {
 // |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| }
 
  // **** **** Funcion principal de la aplicacion **** **** {
int main(unsigned int argc, char* argv[]) {

	if (argc!=nArgumentos+1) { // El numero de argumentos es una precondicion para la ejecucion del programa
		cout << "Error:\n\tDebe introducir " << nArgumentos << " argumento. La llamada debe ser:\n\t\t" << argv[0] << " <nombreInput>" << endl << endl;
		return -1;
	}
	string ficheroEntrada=argv[1];
	string ficheroSalida="salida_" + ficheroEntrada;
	
	// Inicializacion de las variables necesarias para todo el main
	int N_casos; // numero de casos de prueba
	string strNumero;
	
	// Tratamiento de ficheros sobre el disco
	ifstream fentrada(ficheroEntrada.c_str());
	if (!fentrada.good()) {
		cout << "\nError: no se puede acceder al fichero " << ficheroEntrada << " de entrada." << endl;
		return -1;
	}
	ofstream fsalida(ficheroSalida.c_str());
	if (!fsalida.good()) {
		fentrada.close();
		cout << "\nError: no se puede acceder al fichero " << ficheroSalida << " de salida." << endl;
		return -1;
	}
	
	fentrada >> N_casos;
	
	cout << "Se trataran " << N_casos << " casos de prueba" << endl;
	
	for (int casoActual=1; casoActual<=N_casos; casoActual++) {
	
		map<char,int> digitosConocidos;
		
		fentrada >> strNumero;
		int contador=1, posicion=0;
		digitosConocidos[strNumero[posicion]]=contador++;
		posicion++;
		while (posicion < strNumero.size() && strNumero[posicion]==strNumero[0])
			posicion++;
		if (posicion < strNumero.size())
			digitosConocidos[strNumero[posicion]]=0;
		while (++posicion < strNumero.size())
			if (digitosConocidos.count(strNumero[posicion])==0)
				digitosConocidos[strNumero[posicion]]=contador++;
				
		
		// for (int i=0; i<strNumero.size(); i++)
			// cout << digitosConocidos[strNumero[i]] << "\t";
		// cout << endl;
		
		unsigned long long int acumulador=0;
		
		for (int i=0; i<strNumero.size(); i++) {
			int potencia=strNumero.size()-i-1;
			int base=digitosConocidos.size();
			if (base<2) base=2;
			acumulador+=(unsigned long long int)pow(base, potencia)*digitosConocidos[strNumero[i]];
		}
		
		
		// Imprimo el resultado
		fsalida << "Case #" << casoActual << ": " << acumulador << endl;
	} // Fin del for externo
	
	fentrada.close();
	fsalida.close();
	
	return 0;
	
} // Fin del main
 // }

 // **** **** Implementaciones **** **** {
 // }


