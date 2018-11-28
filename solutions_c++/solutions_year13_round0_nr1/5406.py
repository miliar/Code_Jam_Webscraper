#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

int bStatus(char board[][4]) {
	//if X won?
	int over = 1;
	int code[4][4];
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (board[i][j] == '.') {
				board[i][j] = '7';
				over = 0; //not complete
			} else if (board[i][j] == 'X') code[i][j] = 3;
			else if (board[i][j] == 'O') code[i][j] = 0;
			else if (board[i][j] == 'T') code[i][j] = 5;
		}
	}
	//check X
	for (int i = 0; i < 4; i++) {
		int mul = code[i][0] * code[i][1] * code[i][2] * code[i][3];
		if (mul == 81 || mul == 135)
			return 1; //X won
		mul = code[0][i] * code[1][i] * code[2][i] * code[3][i];
		if (mul == 81 || mul == 135)
			return 1;

		int sum = code[i][0] + code[i][1] + code[i][2] + code[i][3];
		if (sum == 5 || sum == 0) return 2;
		sum = code[0][i] + code[1][i] + code[2][i] + code[3][i];
		if (sum == 5 || sum == 0) return 2;
	}

	int mul = code[0][0] * code[1][1] * code[2][2] * code[3][3];
	if (mul == 81 || mul == 135)
		return 1;
	mul = code[0][3] * code[1][2] * code[2][1] * code[3][0];
	if (mul == 81 || mul == 135)
		return 1;

	int sum = code[0][0] + code[1][1] + code[2][2] + code[3][3];
	if (sum == 5 || sum == 0) return 2;
	sum = code[0][3] + code[1][2] + code[2][1] + code[3][0];
	if (sum == 5 || sum == 0) return 2;

	if (over == 0) return 0;
	return 3; //draw
}

int main () {
	ifstream input;
	ofstream output;
	input.open("./A-small-attempt0.in");
	//input.open("./test.in");
	//output.open("./B-small-practice.out");
	output.open("./test.out");

	int t = 0;

	input >> t;
	char board[4][4];
	char a,b,c,d;
	int res[t];
	for (int i = 0; i < t; i++) {
		for (int j = 0; j < 4; j++) {
			//input >> a >> b >> c >> d;
			//cout << c;
			input >> board[j][0] >> board[j][1] >> board[j][2] >> board[j][3];
		}

		res[i] = bStatus(board);
		//input >> endl;
		switch (res[i]) {
			case 0: output << "Case #" << i + 1 << ": Game has not completed\n";
			break;
			case 1: output << "Case #" << i + 1 << ": X won\n"; break;
			case 2: output << "Case #" << i + 1 << ": O won\n"; break;
			case 3: output << "Case #" << i + 1 << ": Draw\n"; break;
			default: break;
		}
	}
	input.close();
	output.close();
	return 0;
}