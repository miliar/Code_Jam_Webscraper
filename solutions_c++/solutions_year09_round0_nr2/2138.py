

	//	*****	*****	*****	Watersheds.cpp	*****	*****	*****	\\
	//	Programa para el problema "Watersheds" del Google Code Jam de 2009				\\
	//	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++	\\
	
// TODO: reemplazar todas las letras con tilde por vocales normales


 // **** **** Includes **** **** {
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <vector>
#include <stack>
//#include <list>
 // |||||||||||||||||||||||||||||||||||||| }

 
using namespace std;
 
 
 // **** **** Defines **** **** {
//#define KNOWLEDGE "POWER"
#define nArgumentos 1 // El fichero de entrada
typedef unsigned char tipoPosicion;
typedef unsigned int tipoElevacion;
 // ||||||||||||||||||||||||||||||||||||| }
 
 
 // **** **** Estructuras de datos (probablemente iran en un header a parte) **** **** {
 // ||||||||||||||||||||||||||||||||||||| }
 
 
 // **** **** Declaraciones anticipadas **** **** {
 pair<tipoPosicion ,tipoPosicion> seleccionaMejor (pair<tipoPosicion,tipoPosicion> actual, pair<tipoPosicion,tipoPosicion> propuesta, vector<vector<tipoElevacion> > &mapaElevaciones);
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
	int N_casos, nFils, nCols; // numero de casos de prueba
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
	
	for (int casoActual=1; casoActual<=N_casos; casoActual++) {
		
		fentrada >> nFils;
		fentrada >> nCols;
		
		vector<vector<tipoElevacion> > mapaElevaciones (nFils, vector<tipoElevacion>(nCols));
		vector<vector<pair<tipoPosicion,tipoPosicion> > > mapaDrenajes (nFils, vector<pair<tipoPosicion,tipoPosicion> >(nCols));
		vector<vector<char> > mapaEtiquetas (nFils, vector<char>(nCols, char('z'+5)));
		
		for (tipoPosicion i=0; i<nFils; i++)
			for (tipoPosicion j=0; j<nCols; j++)
				fentrada >> mapaElevaciones[i][j];
				
		
		tipoPosicion filActual=0, colActual=0;
		
		for (tipoPosicion i=0; i<mapaDrenajes.size(); i++)
			for (tipoPosicion j=0; j<mapaDrenajes[i].size(); j++) {
				pair<tipoPosicion,tipoPosicion> actual(i,j);
				actual=seleccionaMejor(actual,pair<tipoPosicion,tipoPosicion>(i-1,j),mapaElevaciones);
				actual=seleccionaMejor(actual,pair<tipoPosicion,tipoPosicion>(i,j-1),mapaElevaciones);
				actual=seleccionaMejor(actual,pair<tipoPosicion,tipoPosicion>(i,j+1),mapaElevaciones);
				actual=seleccionaMejor(actual,pair<tipoPosicion,tipoPosicion>(i+1,j),mapaElevaciones);
				mapaDrenajes[i][j]=actual;
			}
	
		char etiqueta='a';
		for (tipoPosicion i=0; i<mapaEtiquetas.size(); i++)
			for (tipoPosicion j=0; j<mapaEtiquetas[i].size(); j++) {
				stack <pair<tipoPosicion,tipoPosicion> > pila;
				tipoPosicion filLocal=i, colLocal=j;
				char etiquetaLocal;
				while (mapaEtiquetas[filLocal][colLocal]=='z'+5 && mapaDrenajes[filLocal][colLocal]!=pair<tipoPosicion,tipoPosicion>(filLocal,colLocal)) {
					pila.push(pair<tipoPosicion,tipoPosicion>(filLocal,colLocal));
					filLocal=mapaDrenajes[filLocal][colLocal].first;
					colLocal=mapaDrenajes[filLocal][colLocal].second;
				}
				if (mapaEtiquetas[filLocal][colLocal]=='z'+5)
					etiquetaLocal=etiqueta++;
				else
					etiquetaLocal=mapaEtiquetas[filLocal][colLocal];
				mapaEtiquetas[filLocal][colLocal]=etiquetaLocal;
				while (pila.size()) {
					mapaEtiquetas[pila.top().first][pila.top().second]=etiquetaLocal;
					pila.pop();
				}
			}
			
		
			
		// Imprimo el resultado
		fsalida << "Case #" << casoActual << ": " << endl;
		for (tipoPosicion i=0; i<mapaEtiquetas.size(); i++) {
			for (tipoPosicion j=0; j<mapaEtiquetas[i].size(); j++)
				fsalida << "\t" << mapaEtiquetas[i][j];
			fsalida << endl;
		}
		fsalida << endl;
	} // Fin del for externo
	
	fentrada.close();
	fsalida.close();
	
	return 0;
	
} // Fin del main
 // }

 // **** **** Implementaciones **** **** {
 
 pair<tipoPosicion,tipoPosicion> seleccionaMejor (pair<tipoPosicion,tipoPosicion> actual, pair<tipoPosicion,tipoPosicion> propuesta, vector<vector<tipoElevacion> > &mapaElevaciones){
	if (propuesta.first<0 || propuesta.second<0 || propuesta.first>=mapaElevaciones.size() ||
propuesta.second>=mapaElevaciones[propuesta.first].size()) return actual;
	if (actual.first<0 || actual.second<0 || actual.first>=mapaElevaciones.size() ||
actual.second>=mapaElevaciones[actual.first].size()) return propuesta;
	if (mapaElevaciones[propuesta.first][propuesta.second]<mapaElevaciones[actual.first][actual.second])
		return propuesta;
	else
		return actual;
 }
 // }
