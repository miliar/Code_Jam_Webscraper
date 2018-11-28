#include <iostream>
using namespace std;

int main(){
	char field[4][4];
	int T;
	cin >> T;
	for(int i = 0; i < T; i++){
		bool isEmpty = false;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				cin >> field[j][k];
				if(field[j][k] == '.') isEmpty = true;
			}
		}
		//search
		//raw
		bool x_row[4], y_row[4], x_col[4], y_col[4];
		for(int j = 0; j < 4; j++){
			x_row[j] = true;
			x_col[j] = true;
			y_row[j] = true;
			y_col[j] = true;
		}
		bool x_diag1 = true, x_diag2 = true, y_diag1 = true, y_diag2 = true;
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
				x_row[j] &= (field[j][k] == 'X' || field[j][k] == 'T');
				y_row[j] &= (field[j][k] == 'O' || field[j][k] == 'T');
				x_col[j] &= (field[k][j] == 'X' || field[k][j] == 'T');
				y_col[j] &= (field[k][j] == 'O' || field[k][j] == 'T');
			}
		}
		for(int j = 0; j < 4; j++){
			x_diag1 &= (field[j][j] == 'X' || field[j][j] == 'T');
			y_diag1 &= (field[j][j] == 'O' || field[j][j] == 'T');
			x_diag2 &= (field[3-j][j] == 'X' || field[3-j][j] == 'T');
			y_diag2 &= (field[3-j][j] == 'O' || field[3-j][j] == 'T');

		}
		bool res_x = x_diag1 | x_diag2, res_y = y_diag1 | y_diag2;
		//X won
		for(int j = 0; j < 4; j++){
			res_x |= (x_row[j] | x_col[j]);
		}
		//Y won
		for(int j = 0; j < 4; j++){
			res_y |= (y_row[j] | y_col[j]);
		}

		if(res_x) cout << "Case #" << i+1 << ": " << "X won" << endl;
		else if(res_y) cout << "Case #" << i+1 << ": " << "O won" << endl;
		else if(!res_x && !res_y && !isEmpty) cout << "Case #" << i+1 << ": " << "Draw" << endl;
		else cout << "Case #" << i+1 << ": " << "Game has not completed" << endl;
	}
	return 0;
}
