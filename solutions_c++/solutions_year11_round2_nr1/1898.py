#include <vector>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <list>
#include <algorithm>
#include <stack>
#include <queue>
#include <math.h>
#include <string>

using namespace std;

typedef vector<int> vint;
typedef vector<double> vdouble;
typedef vector<vdouble> vvdouble;
typedef vector<bool> vbool;
typedef vector<vbool> vvbool;
typedef vector<vint> vvint;
typedef vector<char> vchar;
typedef vector<vchar> vvchar;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forsn(i, s, n) for(int i=(s); i<(int)(n); ++i)
#define fL << "\n" //fin de linea
#define esp << " " <<

vdouble cargarResolverProblema(ifstream &entrada){
	double equipos;
	entrada >> equipos;
	vvint matriz(equipos, vint(equipos, 0));
	
	vdouble solucion(equipos, 0);
	vvdouble OWPs(equipos, vdouble(equipos, 0));
	vdouble WPs(equipos, 0);
	vdouble OOWPs(equipos, 0);
	vdouble OWPArreglo(equipos, 0);
	
	vdouble equiposQueJugaronConmigo(equipos, 0);
	vvdouble equiposContraLosQueJugue(equipos, vdouble(equipos, 0));
	
	forn(i, equipos){
		forn(j, equipos){
			char aux;
			entrada >> aux;
			if(aux == '.'){
				matriz[i][j] = -1;
			}else if(aux == '1'){
				matriz[i][j] = 1;
			}else{
				matriz[i][j] = 0;
			}
		}
	}
	forn(equipo, equipos){
		double WP = 0;
		double cantidadPartidos = 0;
		forn(indiceWP, equipos){
			if(indiceWP != equipo){
				if(matriz[equipo][indiceWP] == 1){
					WP++;					
				}
				if(matriz[equipo][indiceWP] != -1){
					cantidadPartidos++;
					equiposContraLosQueJugue[equipo][indiceWP] = 1;
					equiposQueJugaronConmigo[equipo]++;
				}
			}
		}
		if(cantidadPartidos != 0){
			WPs[equipo] = WP / cantidadPartidos;
		}else{
			WPs[equipo] = 0;
		}
	}	
	forn(equipo, equipos){
		forn(rival, equipos){
			double OWP = 0;
			double cantidadPartidos = 0;
			if(rival != equipo && equiposContraLosQueJugue[equipo][rival] == 1){
				forn(otroEquipo, equipos){
					if(otroEquipo != equipo){
						if(matriz[rival][otroEquipo] == 1){
							OWP++;
						}
						if(matriz[rival][otroEquipo] != -1){
							cantidadPartidos++;
						}						
					}
				}
			}
			if(cantidadPartidos != 0){
				OWP = OWP / cantidadPartidos;
				OWPs[equipo][rival] = OWP;
			}else{
				OWPs[equipo][rival] = 0;
			}
		}
	}
	forn(equipo, equipos){
		double OWP = 0;
		forn(rival, equipos){
			if(rival != equipos){
/*				if(equipo == 3){
					//cout << OWPs[equipo][rival] fL;
				}*/
				OWP += OWPs[equipo][rival];
			}
		}
		OWP = OWP / equiposQueJugaronConmigo[equipo];
		OWPArreglo[equipo] = OWP;
	}

	forn(equipo, equipos){
		double OOWP = 0;
		forn(rival, equipos){
			if(rival != equipo && equiposContraLosQueJugue[equipo][rival] == 1){
				OOWP += OWPArreglo[rival];
			}
		}
		OOWPs[equipo] = OOWP / equiposQueJugaronConmigo[equipo];
	}	

	
	forn(equipo, equipos){
		cout <<  WPs[equipo] << " " << OWPArreglo[equipo] << " " << OOWPs[equipo] fL;
		solucion[equipo] = 0.25 * WPs[equipo] + 0.5 * OWPArreglo[equipo] + 0.25 * OOWPs[equipo];
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
			vdouble solucion = cargarResolverProblema(entrada);
			salida << "Case #" << indiceProblemas + 1 << ":" fL;
			forn(indice, solucion.size()){
				salida << solucion[indice] fL;
			}
		}
		salida.close();
		entrada.close();
	}
	return 0;
}
