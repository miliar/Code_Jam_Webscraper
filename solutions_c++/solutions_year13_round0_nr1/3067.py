#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>

using namespace std;

int main (int argc, char *argv[]) {
	
	size_t T, count = 1;
	string line;
	
	int game[4][4];
	int col_sum[4], row_sum[4], di1_sum, di2_sum;
	
	// get T
	getline(cin, line);
	stringstream(line) >> T;

	// get all cases and process it
	for(size_t count = 1; count <= T; count++) {
		// init
		bool x_win = false, o_win = false;
		bool draw = false, incomplete = false;
		di1_sum = 0, di2_sum = 0;
		for(size_t i = 0; i < 4; i++) {
			col_sum[i] = 0; row_sum[i] = 0;
		}
		
		// read and fill
		for(size_t i = 0; i < 4; i++) {
			getline(cin, line);
			for(size_t j = 0; j < 4; j++) {
				if (line[j] == 'T')
					game[i][j] = 1;
				else if (line[j] == 'X')
					game[i][j] = 10;
				else if (line[j] == 'O')
					game[i][j] = 2;
				else if (line[j] == '.') {
					game[i][j] = 0;
					incomplete = true;
				}
				else {
					cout << "Error! unknown game character!" << endl;
					exit(1);
				}
				col_sum[j] += game[i][j];
				row_sum[i] += game[i][j];
			}
			di1_sum += game[i][i];
			di2_sum += game[i][3-i];
		}
		
		// process
		if (di1_sum == 31 || di2_sum == 31 || di1_sum == 40 || di2_sum == 40)
			x_win = true;
		if (di1_sum == 7 || di2_sum == 7 || di1_sum == 8 || di2_sum == 8)
			o_win = true;
		for(size_t i = 0; i < 4; i++) {
			if (col_sum[i] == 31 || row_sum[i] == 31 || col_sum[i] == 40 || row_sum[i] == 40)
				x_win = true;
			if (col_sum[i] == 7 || row_sum[i] == 7 || col_sum[i] == 8 || row_sum[i] == 8)
				o_win = true;
		}
		if (x_win == false && o_win == false && incomplete == false)
			draw = true;

		// Test stuff
		// for(size_t i = 0; i < 4; i++) {
		// 	cout << setw(3) << game[i][0];
		// 	cout << setw(3) << game[i][1];
		// 	cout << setw(3) << game[i][2];
		// 	cout << setw(3) << game[i][3];
		// 	cout << ": " << row_sum[i] << endl;
		// }
		// cout << "-------" << endl;
		// cout << setw(3) << col_sum[0];
		// cout << setw(3) << col_sum[1];
		// cout << setw(3) << col_sum[2];
		// cout << setw(3) << col_sum[3] << endl;
		// cout << setw(3) << di1_sum << setw(3) << di2_sum << endl;
		
		// print output
		cout << "Case #" << count << ": ";
		if (x_win)
			cout << "X won";
		else if (o_win)
			cout << "O won";
		else if (draw)
			cout << "Draw";
		else if (incomplete)
			cout << "Game has not completed";
		cout << endl;
	
		// spare a line
		getline(cin, line);
	}
	
	return 0;
}