#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	char tablero[5][5];
	string linea;
		
	int T;
	cin >> T;
	cin.ignore();
	
	// T cases
	for (int i=1; i<=T; i++){

		//4 filas de cada tablero
		for (int fila=1; fila<=4; fila++) {
			getline(cin, linea);
			for (int col=1; col<=4; col++) 
				 tablero[fila][col]= linea[col-1];
		}	
		
		//fila en blanco
		getline(cin, linea);
		
		//proceso tablero
		string resultado;
		bool haypunto=false;
		int ctaX, ctaO, ctaT;
			
		//verifico filas
		int fila=1;
		while (fila<=4 && resultado.empty()){
			ctaX=0; ctaO=0; ctaT=0;
			int col=1;
			while (col<=4){
				if (tablero[fila][col] == '.') { col=5; haypunto=true; }
				if (tablero[fila][col] == 'X') ctaX++;
				if (tablero[fila][col] == 'O') ctaO++;
				if (tablero[fila][col] == 'T') ctaT++;
				col++;
			}
			if ( (ctaX==4) || (ctaX==3 && ctaT==1) ) resultado="X won";
			else if ( (ctaO==4) || (ctaO==3 && ctaT==1) ) resultado="O won";			
			fila++;
		}
		
		//verifico columnas
		int col=1;	
		while (col<=4 && resultado.empty()){
			ctaX=0; ctaO=0; ctaT=0;
			int fila=1;
			while (fila<=4){
				if (tablero[fila][col] == '.') fila=5; 
				if (tablero[fila][col] == 'X') ctaX++;
				if (tablero[fila][col] == 'O') ctaO++;
				if (tablero[fila][col] == 'T') ctaT++;
				fila++;
			}
			if ( (ctaX==4) || (ctaX==3 && ctaT==1) ) resultado="X won";
			else if ( (ctaO==4) || (ctaO==3 && ctaT==1) ) resultado="O won";			
			col++;
		}		
			
		//verifico diagonal 1
		int d=1;	
		ctaX=0; ctaO=0; ctaT=0;
		while (d<=4 && resultado.empty()){
			if (tablero[d][d] == '.') d=5; 
			if (tablero[d][d] == 'X') ctaX++;
			if (tablero[d][d] == 'O') ctaO++;
			if (tablero[d][d] == 'T') ctaT++;
			d++;
		}
		if ( (ctaX==4) || (ctaX==3 && ctaT==1) ) resultado="X won";
		else if ( (ctaO==4) || (ctaO==3 && ctaT==1) ) resultado="O won";					
		
		//verifico diagonal 2
		d=1; int dd=4;	
		ctaX=0; ctaO=0; ctaT=0;
		while (d<=4 && resultado.empty()){
			if (tablero[d][dd] == '.') d=5;
			if (tablero[d][dd] == 'X') ctaX++;
			if (tablero[d][dd] == 'O') ctaO++;
			if (tablero[d][dd] == 'T') ctaT++;
			d++;dd--;
		}
		if ( (ctaX==4) || (ctaX==3 && ctaT==1) ) resultado="X won";
		else if ( (ctaO==4) || (ctaO==3 && ctaT==1) ) resultado="O won";	
		
		if (resultado.empty()){
			if (!haypunto) resultado="Draw";
			else resultado="Game has not completed";
		}
		
		cout << "Case #" << i << ": " << resultado << endl;
		}
	
	return 0;
}
