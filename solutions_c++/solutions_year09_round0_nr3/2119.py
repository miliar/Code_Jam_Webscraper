

	//	*****	*****	*****	Welcome2CJ.cpp	*****	*****	*****	\\
	//	Programa para el problema "Welcome To Code Jam" del Google Code Jam de 2009		\\
	//	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	\\
	
// TODO: reemplazar todas las letras con tilde por vocales normales


 // **** **** Includes **** **** {
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <vector>
// #include <list>
// #include <string>
//#include <utility> // Tipo "pair<,>" standard (pair.h para compatibilidad no standard)
// #include <stdlib.h>
// #include <vector>
//#include <stdexcept>
//#include <utility>
//#include <cmath>
// #include <string.h>
 // |||||||||||||||||||||||||||||||||||||| }

 
using namespace std;
 
 
 // **** **** Defines **** **** {
//#define KNOWLEDGE "POWER"
#define nArgumentos 1 // El fichero de entrada
typedef unsigned long int tipoNumero;
 // ||||||||||||||||||||||||||||||||||||| }
 
 
 // **** **** Estructuras de datos (probablemente iran en un header a parte) **** **** {
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
	
	const string gMessage = "welcome to code jam";
	// Inicializacion de las variables necesarias para todo el main
	int N_casos; // numero de casos de prueba
	string newLinea; // linea recien leida
	
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

	for (int casoTratado=1; casoTratado<=N_casos; casoTratado++) {
// Lo primero será almacenar toda la información importante que, en este caso, son las posiciones de las letras que necesitamos
		tipoNumero numResultados=1;
		getline(fentrada, newLinea); // se asume que no hace falta "tolower"
		if (newLinea=="") {
			casoTratado--;
			continue;
		}
		
		vector<tipoNumero> vectorVacio (newLinea.size()+1, tipoNumero(0)); // Vector inicializado con ceros
		vector<tipoNumero> vectorResultados=vectorVacio; // Vector inicializado con ceros
		vector<tipoNumero> vecResultadosAnterior (newLinea.size()+1, tipoNumero(1)); // Vector inicializado con ceros
		
		int iMsg=gMessage.size();
		int jCad;
		
		while (iMsg-->0) {
			for (jCad=newLinea.size()-(gMessage.size()-iMsg); jCad>=0; jCad--) {
				vectorResultados[jCad]=vectorResultados[jCad+1];
				if (gMessage[iMsg]==newLinea[jCad])
					vectorResultados[jCad]+=vecResultadosAnterior[jCad+1];
			}
			vecResultadosAnterior=vectorResultados;
			vectorResultados=vectorVacio;
		}
		numResultados=vecResultadosAnterior[0];
	
		
		// Imprimo el resultado
		fsalida << "Case #" << casoTratado << ": ";
		numResultados=numResultados%10000; // desprecio todos los digitos que no sean los 4 primeros
		for (int i=1000; numResultados<i; i=i/10)
			fsalida << "0";
		if (numResultados>0)
			fsalida << numResultados;
		fsalida << endl;
	} // Fin del for externo
	
	fentrada.close();
	fsalida.close();
	
	return 0;
	
} // Fin del main
 // }

 // **** **** Implementaciones **** **** {
 // }
