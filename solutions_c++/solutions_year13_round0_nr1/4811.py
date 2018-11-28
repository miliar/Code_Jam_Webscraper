/*
 * ttt.cpp
 *
 *  Created on: 12/04/2013
 *      Author: Tomás
 */

#include <string>
#include <fstream>
#include <iostream>
using namespace std;

int main(){
	string strFila;
	ifstream input("ttt.in");
	ofstream output("ttt.out");
	int fila, columna, T, casoActual, i, j;
	input >> T;
	int cols[4][2], fils[4][2], diags[2][2];
	bool hayEspacio;

	for (casoActual = 1; casoActual <= T; casoActual++){
		hayEspacio = false;

		//inicializamos filas y columnas.
		for (i = 0; i < 4; i++){
			for (j = 0; j < 2; j++){
				cols[i][j] = 0;
				fils[i][j] = 0;
			}
		}
		//inicializamos diagonales.
		for (i = 0; i < 2; i++){
			for (j = 0; j < 2; j++){
				diags[i][j] = 0;
			}
		}
		//contamos cada uno.
		for (fila = 0; fila < 4; fila ++){
			input >> strFila;
			for (columna = 0; columna < 4; columna ++){
				//chequeo si está en alguna diagonal.
				int diag;
				if (columna == fila){
					diag = 0;
				} else {
					if (columna == 3 - fila){
						diag = 1;
					} else {
						diag = 3;
					}
				}
				// conteo.
				switch (strFila[columna]){
				case 'X':
					cols[columna][0] ++;
					fils[fila][0] ++;
					if (diag != 3){
						diags[diag][0]++;
					}
					break;
				case 'O':
					cols[columna][1] ++;
					fils[fila][1]++;
					if (diag != 3){
						diags[diag][1]++;
					}
					break;
				case 'T':
					cols[columna][0] ++;
					fils[fila][0] ++;
					cols[columna][1] ++;
					fils[fila][1]++;
					if (diag != 3){
						diags[diag][1]++;
						diags[diag][0]++;
					}
					break;
				case '.':
					hayEspacio = true;
					break;
				}
			}
		}
		bool hayGanador = false;
		//terminado de procesar el caso. A ver el resultado. Primero Filas y columnas.
		for (i = 0; (i < 4) && (!hayGanador); i ++){
			if ( ((cols[i][0]) == 4) || ((fils[i][0]) == 4) ){
				output << "Case #" << casoActual << ": X won" << endl;
				hayGanador = true;
			} else {
				if ( ((cols[i][1]) == 4) || ((fils[i][1]) == 4) ){
					output << "Case #" << casoActual << ": O won" << endl;
					hayGanador = true;
				}
			}
		}
		//sino las diagonales.
		if (!hayGanador){
			for (i = 0; i < 2; i++){
				if (diags[i][0] == 4){
					output << "Case #" << casoActual << ": X won" << endl;
					hayGanador = true;
				} else {
					if (diags[i][1] == 4){
						output << "Case #" << casoActual << ": O won" << endl;
						hayGanador = true;
					}
				}
			}
		}
		//casos sin ganador.
		if (!hayGanador){
			if (!hayEspacio){
				output << "Case #" << casoActual << ": Draw" << endl;
			} else {
				output << "Case #" << casoActual << ": Game has not completed" << endl;
			}
		}
	}
	return 0;
}



