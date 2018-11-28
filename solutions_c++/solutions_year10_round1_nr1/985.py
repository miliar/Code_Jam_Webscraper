#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>

using namespace std;

int main(int argc, char *argv[]){
	if (argc != 2){
		cerr << "Error: " << argv[0] << " file" << endl;
		exit(-1);
	}
	ifstream file(argv[1]);
	if (!file.is_open()){
		cerr << "Error: file " << argv[0] << " could not be opened" << endl;
	}
	int T;
	file >> T;
	for (int i = 0; i < T; i++){
		cout << "Case #" << (i+1) << ": ";
		int N, K;
		file >> N >> K;
		//N tam. tablero
		//K cuantas tiene que unir
		vector < vector < char > > tablero (N, vector <char>(N, 'a'));
		for (int i = 0; i < N; i++){
			string line;
			file >> line;
			for (int j = 0; j < N; j++){
					tablero[j][i] = line[j];
			}
		}

		//Rotar
		vector < vector < char > > tableroRotado (N, vector <char>());
		for (int i = 0; i < N; i++){//y
			for (int j = 0; j < N; j++){//x
				if (tablero[i][j] == '.'){
					tableroRotado[j].push_back('.');
				} 
			}
		}
		for (int i = 0; i < N; i++){//y
			for (int j = 0; j < N; j++){//x
				if (tablero[i][j] != '.'){
					tableroRotado[j].push_back(tablero[i][j]);
				} 
			}
		}

		/*cout << "Tablero" << endl;
		for (int i = 0; i < N; i++){//y
			for (int j = 0; j < N; j++){//x
				cout << tablero[j][i];
			}
			cout << endl;
		}

		cout << "Tablero Rotado" << endl;
		for (int i = 0; i < N; i++){//y
			for (int j = 0; j < N; j++){//x
				cout << tableroRotado[j][i];
			}
			cout << endl;
		}*/
		//Contar en filas
		bool R, B;
		R = false;
		B = false;
		for (int i = 0; i < N; i++){
			char current = '.';
			int currentValue = 0;
			for (int j = 0; j < N; j++){
				if (tableroRotado[i][j] == '.'){
					currentValue = 0;
					current = '.';
				} else if (tableroRotado[i][j] == current){
					currentValue++;
					if (currentValue == K){
						if (current == 'R'){
							R = true;
						} else {
							B = true;
						}
					}
				} else {
					current = tableroRotado[i][j];
					currentValue = 1;
				}
			}
		}
		//Contar en columnas
		for (int i = 0; i < N; i++){
			char current = '.';
			int currentValue = 0;
			for (int j = 0; j < N; j++){
				if (tableroRotado[j][i] == '.'){
					currentValue = 0;
					current = '.';
				} else if (tableroRotado[j][i] == current){
					currentValue++;
					if (currentValue == K){
						if (current == 'R'){
							R = true;
						} else {
							B = true;
						}
					}
				} else {
					current = tableroRotado[j][i];
					currentValue = 1;
				}
			}
		}
		//Contar en diagonal
		for (int i = 0; i < N; i++){
			int currentY = 0;
			int currentX = i;
			char current = '.';
			int currentValue = 0;

			for (int j = 0; j < N - i; j++){
				if (tableroRotado[currentX + j][currentY + j] == '.'){
					currentValue = 0;
					current = '.';
				} else if (tableroRotado[currentX + j][currentY + j] == current){
					currentValue++;
					if (currentValue == K){
						if (current == 'R'){
							R = true;
						} else {
							B = true;
						}
					}
				} else {
					current = tableroRotado[currentX + j][currentY + j];
					currentValue = 1;
				}
			}
		}

		for (int i = 0; i < N; i++){
			int currentX = 0;
			int currentY = i;
			char current = '.';
			int currentValue = 0;

			for (int j = 0; j < N - i; j++){
				if (tableroRotado[currentX + j][currentY + j] == '.'){
					currentValue = 0;
					current = '.';
				} else if (tableroRotado[currentX + j][currentY + j] == current){
					currentValue++;
					if (currentValue == K){
						if (current == 'R'){
							R = true;
						} else {
							B = true;
						}
					}
				} else {
					current = tableroRotado[currentX + j][currentY + j];
					currentValue = 1;
				}
			}
		}

		for (int i = 0; i < N; i++){
			int currentY = 0;
			int currentX = i;
			char current = '.';
			int currentValue = 0;

			for (int j = 0; j < i+1; j++){
				if (tableroRotado[currentX - j][currentY + j] == '.'){
					currentValue = 0;
					current = '.';
				} else if (tableroRotado[currentX - j][currentY + j] == current){
					currentValue++;
					if (currentValue == K){
						if (current == 'R'){
							R = true;
						} else {
							B = true;
						}
					}
				} else {
					current = tableroRotado[currentX - j][currentY + j];
					currentValue = 1;
				}

			}
		}

		for (int i = 0; i < N; i++){
			int currentY = i;
			int currentX = N-1;
			char current = '.';
			int currentValue = 0;

			for (int j = 0; j < N - i; j++){
				if (tableroRotado[currentX - j][currentY + j] == '.'){
					currentValue = 0;
					current = '.';
				} else if (tableroRotado[currentX - j][currentY + j] == current){
					currentValue++;
					if (currentValue == K){
						if (current == 'R'){
							R = true;
						} else {
							B = true;
						}
					}
				} else {
					current = tableroRotado[currentX - j][currentY + j];
					currentValue = 1;
				}
			}
		}

		if (R && B){
			cout << "Both" << endl;
		} else if (R){
			cout << "Red" << endl;
		} else if (B){
			cout << "Blue" << endl;
		} else {
			cout << "Neither" << endl;	
		}

	}

	file.close();
}
