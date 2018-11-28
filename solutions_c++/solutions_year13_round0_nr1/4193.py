#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

int checkStatus(char status[4][4]) {
	int matrix[4][4];
	int nempty = 0;
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if(status[i][j]=='X') matrix[i][j] = 1;
			if(status[i][j]=='O') matrix[i][j] = -1;
			if(status[i][j]=='T') matrix[i][j] = 1;
			if(status[i][j]=='.') {
				matrix[i][j] = 0;
				++nempty;
			}
		}
	}

	int diagx = 0;
	int diagy = 0;
	int xsum = 0;
	int ysum = 0;
	for(int i=0; i<4; i++) {
		diagx += matrix[i][i];
		diagy += matrix[i][3-i];
		xsum = 0;
		ysum = 0;
		for(int j=0; j<4; j++) {
			xsum += matrix[i][j];
			ysum += matrix[j][i];
		}
		if(xsum == 4 || ysum == 4 || diagx == 4 || diagy == 4) return 1;  // X won
		if(xsum == -4 || ysum == -4 || diagx == -4 || diagy == -4) return 2;  // O won
	}

	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if(status[i][j]=='T') matrix[i][j] = -1;
			xsum = 0;
			ysum = 0;
			diagx = 0;
			diagy = 0;
			for(int k=0; k<4; k++) {
				xsum += matrix[i][k];
				ysum += matrix[k][j];
				if(i == j) diagx += matrix[k][k];
				if(i+j == 3) diagy += matrix[k][3-k];
			}
			if(xsum == 4 || ysum == 4 || diagx == 4 || diagy == 4) return 1;  // X won
			if(xsum == -4 || ysum == -4 || diagx == -4 || diagy == -4) return 2;  // O won
		}
	}

	if(nempty == 0) return 3; // Draw
	return 4; // game not over yet
}

int main() {
	string line;
	ifstream infile;
	ofstream outfile;
	char status[4][4];
	int result;
	infile.open("input.txt");
	outfile.open("output.txt");
	getline(infile, line);  // read test case number#
	int nCase = atoi(line.c_str());
	for(int i=0; i<nCase; i++) {
		for(int j=0; j<4; j++) {
			getline(infile, line);
			for(int k=0; k<4; k++) {
				status[j][k] = line[k];
			}
		}
		result = checkStatus(status);
		outfile << "Case #" << i+1 << ": ";
		if(result == 1) outfile << "X won";
		if(result == 2) outfile << "O won";
		if(result == 3) outfile << "Draw";
		if(result == 4) outfile << "Game has not completed";
		outfile << endl;
		getline(infile,line);
	}
	infile.close();
	outfile.close();
	return 0;
}
