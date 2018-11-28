// Tic-Tac-Toe-Tomek
#include <iostream>
#include <string>

using namespace std;
#define forn(i,n) for(int i=0;i<int(n);++i)

int tX, tY;
char tab[4][4];

bool gano(char j) {
	// filas
	forn (y,4) {
		if (tab[y][0]==j && tab[y][1]==j && tab[y][2]==j && tab[y][3]==j)
			return true;
	}
	// columnas
	forn (x,4) {
		if (tab[0][x]==j && tab[1][x]==j && tab[2][x]==j && tab[3][x]==j)
			return true;
	}
	// diagonales
	if (tab[0][0]==j && tab[1][1]==j && tab[2][2]==j && tab[3][3]==j)
		return true;
	if (tab[3][0]==j && tab[2][1]==j && tab[1][2]==j && tab[0][3]==j)
		return true;
	return false;
}

string veredicto(bool hayMovidasPosibles) {
	// verificar si gano O
	// sino, verificar si gano X
	// sino, verificar si hay lugares en blanco..
	if (tX != -1)
		tab[tY][tX] = 'O';
	// filas
	if (gano('O'))
		return "O won";

	if (tX != -1)
		tab[tY][tX] = 'X';

	if (gano('X'))
		return "X won";

	if (hayMovidasPosibles)
		return "Game has not completed";

	return "Draw";
}

int main() {
	int casos;
	cin >> casos;


	forn (i,casos) {
		cout << "Case #" << i+1 << ": ";
		bool hayLibres = false;
		tX = tY = -1;
		forn (y,4) {
			string linea;
			cin >> linea;
			forn (x,4) {
				tab[y][x] = linea[x];
				if (tab[y][x]=='T') {
					tX = x;
					tY = y;
				}
				hayLibres |= tab[y][x] == '.';
			}
		}

		cout << veredicto(hayLibres) << endl;
	}

	return 0;
}
