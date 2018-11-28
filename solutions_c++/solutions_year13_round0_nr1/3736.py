#include <iostream>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <sstream>

using namespace std;

char checkWinner(char (*)[4], int, int);
char checkWinnerDiagonally(char (*)[4]);
int main() {
	int number = 0;
	
	string str = "";
	while (true) {
		getline(cin, str);

		stringstream stream(str);
		if (stream >> number)
			break;
	}

	for(int i = 0; i < number; i++) {
		if(i != 0)
			cout << endl;
		char matrix[4][4];
		bool inComplete = false;
		char winner = '.';
		bool valid[4][2] = {
			true, true,
			true, true,
			true, true,
			true, true
		};
		for(int j = 0; j < 4; j++) {
			for(int k = 0; k < 4; k++) {
				if(k == 0) {
					char c = '\n';
					while(c == '\n')
						c = getchar();
					matrix[j][k] = c;
				} else {
					matrix[j][k] = getchar();
				}
				if(matrix[j][k] == '.') {
					valid[j][0] = false;
					valid[k][1] = false;
					inComplete = true;
				}
			}
			//fflush(stdin);
		}
		for(int i = 0; i < 4; i++) {
			winner = '.';
			if(valid[i][0] == true){
				winner = checkWinner(matrix, i, 0);
			}
			
			if(winner != '.')
				break;

			if(valid[i][1] == true) {
				winner = checkWinner(matrix, i, 1);
			}
			
			if(winner != '.')
				break;
		}
		if(winner != '.') {
			cout << "Case #" << i + 1 << ": " << winner << " won";
			continue;
		}
		else {
			winner = checkWinnerDiagonally(matrix);
			if(winner != '.') {
				cout << "Case #" << i + 1 << ": " << winner << " won";
				continue;
			}
		}

		if(inComplete)
			cout << "Case #" << i + 1 << ": Game has not completed";
		else 
			cout << "Case #" << i + 1 << ": Draw";
	}

	return 0;
}

char checkWinnerDiagonally(char (*matrix)[4]) {
	char winner = '.';
	if(matrix[0][0] != 'T' && matrix[0][0] != 't')
		winner = matrix[0][0];
	else
		winner = matrix[1][1];
	for(int k = 0; k < 4; k++) {
		if((matrix[k][k] != 't' && matrix[k][k] != 'T')) {
			if(winner == matrix[k][k])
				continue;
			else {
				winner = '.';
				break;
			}
		}
	}
	if(winner != '.')
		return winner;

	if(matrix[0][3] != 'T' && matrix[0][3] != 't')
		winner = matrix[0][3];
	else
		winner = matrix[1][2];
	for(int k = 0; k < 4; k++) {
		if((matrix[k][3 - k] != 't' && matrix[k][3 - k] != 'T')) {
			if(winner == matrix[k][3 - k])
				continue;
			else {
				winner = '.';
				break;
			}
		}
	}

	return winner;
}

char checkWinner(char (*matrix)[4], int i, int j) {
	char winner = '.';
	if(j == 0) {
		if(matrix[i][0] != 'T' && matrix[i][0] != 't')
			winner = matrix[i][0];
		else
			winner = matrix[i][1];
		for(int k = 0; k < 4; k++) {
			if((matrix[i][k] != 't' && matrix[i][k] != 'T')) {
				if(winner == matrix[i][k]) {
					continue;
				} else {
					winner = '.';
					break;
				}
			}
		}
	} else if(j == 1) {
		if(matrix[0][i] != 'T' && matrix[0][i] != 't')
			winner = matrix[0][i];
		else
			winner = matrix[1][i];
		for(int k = 0; k < 4; k++) {
			if((matrix[k][i] != 't' && matrix[k][i] != 'T')) {
				if(winner == matrix[k][i]) {
					continue;
				} else {
					winner = '.';
					break;
				}
			}
		}
	}
	return winner;
}