#include <iostream>
#include <vector>
#include <fstream>
#include <stdlib.h>
#include <set>
#include <limits.h>
#include <iomanip>

using namespace std;

int R, C;
char tablero[50][50];

int main(int argc, char *argv[]){
	if (argc != 2){
		cerr << "Error: " << argv[0] << " file" << endl;
		exit(-1);
	}
	cout << setprecision(10);
	ifstream file(argv[1]);
	if (!file.is_open()){
		cerr << "Error: file " << argv[0] << " could not be opened" << endl;
	}
	int T;
	file >> T;
	for (int test = 0; test < T; test++){
		file >> R >> C;
		for (int i = 0; i < R; i++){
			for (int j = 0; j < C; j++){
				file >> tablero[i][j]; 				
			}
		}
		bool fallo = false;
		for (int i = 0; i < R; i++){
			for (int j = 0; j < C; j++){
				if (tablero[i][j] == '#'){
					if ((i <= R-2) && (j <= C -2) && (tablero[i+1][j] == '#') && (tablero[i+1][j+1] == '#') && (tablero[i][j+1] == '#')){
						tablero[i][j] = '/';
						tablero[i+1][j+1] = '/';
						tablero[i+1][j] = '\\';
						tablero[i][j+1] = '\\';
					} else {
						fallo = true;
						break;
					}
				}
			}
			if (fallo){
				break;
			}
		}
		cout << "Case #" << (test+1) << ": " << endl;
		if (fallo){
			cout << "Impossible" << endl;
		} else {
			for (int i = 0; i < R; i++){
				for (int j = 0; j < C; j++){
					cout << tablero[i][j];
				}
				cout << endl;
			}
		}
	}
}
