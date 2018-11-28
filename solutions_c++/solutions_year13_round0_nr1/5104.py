#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char **argv){
	char grid[4][4];

	ifstream fin (argv[1]);
	unsigned int T; fin >> T;
	for(unsigned int t = 0; t != T; t++){
		bool complete = true;
		for (unsigned int i = 0; i != 4; i++){
			for (unsigned int j = 0; j != 4; j++){
				char c;
				fin >> c;
				switch(c){
					case 'X': grid[i][j] = 1; break;
					case 'O': grid[i][j] = 2; break;
					case 'T': grid[i][j] = 3; break;
					case '.': 
						  grid[i][j] = 0;
						  complete = false;
						  break;
					default: cerr << "Error: " << c << endl;
				}
			}
		}
		char row0 = grid[0][0] & grid[0][1] & grid[0][2] & grid[0][3]; 
		char row1 = grid[1][0] & grid[1][1] & grid[1][2] & grid[1][3]; 
		char row2 = grid[2][0] & grid[2][1] & grid[2][2] & grid[2][3]; 
		char row3 = grid[3][0] & grid[3][1] & grid[3][2] & grid[3][3];

		char col0 = grid[0][0] & grid[1][0] & grid[2][0] & grid[3][0];
		char col1 = grid[0][1] & grid[1][1] & grid[2][1] & grid[3][1];
		char col2 = grid[0][2] & grid[1][2] & grid[2][2] & grid[3][2];
		char col3 = grid[0][3] & grid[1][3] & grid[2][3] & grid[3][3];

		char diagb = grid[0][0] & grid[1][1] & grid[2][2] & grid[3][3];
		char diagf = grid[0][3] & grid[1][2] & grid[2][1] & grid[3][0];

		char winner = row0 | row1 | row2 | row3 |
			      col0 | col1 | col2 | col3 |
			      diagb| diagf;

	

		cout << "Case #" << t+1 << ": ";
		switch(winner){
			case 0:
				if(complete)
					cout << "Draw";
				else
					cout << "Game has not completed";
				break;
			case 1: cout << "X won"; break;
			case 2: cout << "O won"; break;
		}
		cout << endl;
	
	}	
	return 0;
}
