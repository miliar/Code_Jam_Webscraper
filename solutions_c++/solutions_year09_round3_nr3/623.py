

	//	*****	*****	*****	BribePrisoners.cpp	*****	*****	*****	\\
	//	Programa de práctica para el problema Bribe the prisoners de Google Jam 2k9			\\
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
 int libera_uno(set<int> liberables, vector<bool> prisioneros);
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
	int N_casos, P_celdas, Q_liberados; // numero de casos de prueba
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
		
		fentrada >> P_celdas;
		fentrada >> Q_liberados;
		
		vector<bool> prisioneros = vector<bool> (P_celdas, bool(true)); // Prisioneros presentes
		set<int> liberables;
		
		for (int i=0; i<Q_liberados; i++) {
			int aux;
			fentrada >> aux;
			liberables.insert(aux);
		}
		
		
		// Imprimo el resultado
		fsalida  << "Case #" << casoActual << ": " << libera_uno(liberables, prisioneros) << endl;
	} // Fin del for externo
	
	fentrada.close();
	fsalida.close();
	
	return 0;
	
} // Fin del main
 // }

 // **** **** Implementaciones **** **** {
int libera_uno(set<int> liberables, vector<bool> prisioneros) {

	if (liberables.size()==0) return 0;
	
	int mejor=liberables.size()*prisioneros.size()+1;
	for (set<int>::iterator itrLibera=liberables.begin();
			itrLibera!=liberables.end(); itrLibera++)
	{
		int siguiente=(*itrLibera)-1;
		prisioneros[siguiente]=false;
		set<int> auxiliar=liberables;
		auxiliar.erase(auxiliar.find(*itrLibera));
		int acumulador=0;
		for (int i=siguiente-1; i>=0 && prisioneros[i]==true; i--)
			acumulador++;
		for (int i=siguiente+1; i<prisioneros.size() && prisioneros[i]==true; i++)
			acumulador++;
		acumulador+=libera_uno(auxiliar, prisioneros);
		if (acumulador<mejor) mejor=acumulador;
		prisioneros[siguiente]=true;
	}
	return mejor;
}
 // }


