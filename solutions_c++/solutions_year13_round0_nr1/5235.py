#include<iostream>
#include<fstream>

using namespace std;

char X[4][4];
char O[4][4];

char won(){
	for(int i = 0; i < 4; i++){
		if(X[0][i] == 'X' && X[0][i] == X[1][i] && X[2][i] == X[3][i] && X[1][i] == X[2][i]){
			return 'X';
		}
		if(X[i][0] == 'X' && X[i][0] == X[i][1] && X[i][2] == X[i][3] && X[i][1] == X[i][2]){
			return 'X';
		}
		if(O[0][i] == 'O' && O[0][i] == O[1][i] && O[2][i] == O[3][i] && O[1][i] == O[2][i]){
			return 'O';
		}
		if(O[i][0] == 'O' && O[i][0] == O[i][1] && O[i][2] == O[i][3] && O[i][1] == O[i][2]){
			return 'O';
		}
	}// vert + hor
	if((X[0][0]&X[1][1]&X[2][2]&X[3][3]) == 'X') return 'X';
	if((X[0][3]&X[1][2]&X[2][1]&X[3][0]) == 'X') return 'X';
	if((O[0][0]&O[1][1]&O[2][2]&O[3][3]) == 'O') return 'O';
	if((O[0][3]&O[1][2]&O[2][1]&O[3][0]) == 'O') return 'O';
	return '.';
}

bool tie(){
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if(X[i][j] == '.') return 0;
		}
	}
	return 1;
}

int main(){
	ifstream infile;
	ofstream ofile;
	infile.open ("test.txt");
	ofile.open("out.txt");
	int t, cases = 0;
	infile >> t;
	while(cases++ < t){
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				infile >> X[i][j];
				if(X[i][j] == 'T'){
					X[i][j] = 'X';
					O[i][j] = 'O';
				}
				else O[i][j] = X[i][j];
			}// j
		}// i
		char win = won();
		ofile << "Case #" << cases << ": ";
		if(win == '.'){
			if(tie()) ofile << "Draw\n";
			else ofile << "Game has not completed\n";
		}
		else ofile << win << " won\n";
	}// while more inputs
	
	infile.close();
	ofile.close();
	return 0;
}