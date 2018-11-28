

	//	*****	*****	*****	AlienLanguage.cpp	*****	*****	*****	\\
	//	Programa para el problema "Alien Language del Google Code Jam de 2009					\\
	//	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	\\
	
// TODO: reemplazar todas las letras con tilde por vocales normales


 // **** **** Includes **** **** {
#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <string>
#include <set>
 // |||||||||||||||||||||||||||||||||||||| }

 
using namespace std;
 
 
 // **** **** Defines **** **** {
//#define KNOWLEDGE "POWER"
#define nArgumentos 1 // El fichero de entrada
 // ||||||||||||||||||||||||||||||||||||| }
 
 
 // **** **** Estructuras de datos (probablemente iran en un header a parte) **** **** {
 // ||||||||||||||||||||||||||||||||||||| }
 
 
 // **** **** Declaraciones anticipadas **** **** {
 void generaPalabras(unsigned int &contador, set<string> &diccionario, vector<set<char> > &cjtosLetras, int posicion=0, string cadenaPrefijo="");
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
	int L_minusculas, D_palabras, N_pruebas; // minusculas por palabra, palabras, numero de tests
	set<string> diccionario;
	string newPalabra; // palabra recien leida
	
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
	
	fentrada >> L_minusculas;
	fentrada >> D_palabras;
	fentrada >> N_pruebas;
	
// Lo primero es insertar todas las palabras en el diccionario
	for (int i=0; i<D_palabras; i++) {
		getline(fentrada, newPalabra); // se asume que no hace falta "tolower"
		if (newPalabra!="")
			diccionario.insert(newPalabra);
		else
			i--;
	}
	
	cout << "Se trata de un input con " << L_minusculas << " letras, " << D_palabras << " palabras y " << N_pruebas << " casos de prueba" << endl;

	for (int casoTratado=1; casoTratado<=N_pruebas; casoTratado++) {
// Lo siguiente será acumular todos los conjuntos de posibles letras para cada palabra en cada posicion
		getline(fentrada, newPalabra); // se asume que no hace falta "tolower"
		vector<set<char> > cjtosLetras(L_minusculas); // los cjtos de letras
		int posLetra=0,  numCoincidencias=0;
		for (int i=0; i<newPalabra.size(); i++) {
			switch (newPalabra[i]) {
				case '(':
							while (newPalabra[++i]!= ')')
								cjtosLetras[posLetra].insert(newPalabra[i]);
							break;
				default: // letra suelta
							cjtosLetras[posLetra].insert(newPalabra[i]);
							break;
			}
			posLetra++;
		}
		
// Ahora hay que hacer algo con los datos recopilados
		set<string>::iterator itrDiccionario=diccionario.begin();
		
		// Para cada palabra del diccionario intenta relacionarla con los conjuntos del caso actual
		for (set<string>::iterator itrDiccionario=diccionario.begin(); itrDiccionario!=diccionario.end(); itrDiccionario++) {
			int i=0;
			while (i<(*itrDiccionario).size() && cjtosLetras[i].find((*itrDiccionario)[i])!=cjtosLetras[i].end())
				i++;
			if (i==(*itrDiccionario).size()) {
				cout << (*itrDiccionario) << endl;
				numCoincidencias++;
			}
		}
		
		// Imprimo el resultado
		fsalida << "Case #" << casoTratado << ": " << numCoincidencias << endl;
	}
	
	fentrada.close();
	fsalida.close();
	
	return 0;
	
} // Fin del main
 // }

 // **** **** Implementaciones **** **** {
 void generaPalabras(int &contador, set<string> &diccionario, vector<set<char> > &cjtosLetras, int posicion, string cadenaPrefijo) {
	// Caso base
	if (cjtosLetras.size()==posicion) {
		if (diccionario.find(cadenaPrefijo)==diccionario.end())
			contador++;
		return;
	}
	// Caso Recursivo
	for (set<char>::iterator itrLetra=cjtosLetras[posicion].begin();
							itrLetra!=cjtosLetras[posicion].end(); itrLetra++) {
		generaPalabras(contador, diccionario, cjtosLetras, posicion+1, cadenaPrefijo + *itrLetra);
	}
	return;
}

 // }


