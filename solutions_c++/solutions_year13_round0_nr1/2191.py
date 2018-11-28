#include <string>
#include <cstdio>
#include <iostream>

using namespace std;

int processOne(int * board) {
	int dots = 0;
	for(int i = 0; i < 4; i++) {
		int s = board[i * 4] + board[i * 4 + 1] + board[i * 4 + 2] + board[i * 4 + 3];
		if(board[i * 4] == 1 || board[i * 4 + 1] == 1 || board[i * 4 + 2] == 1 || board[i * 4 + 3] == 1)
			dots++;
		if(s == 16 || s == 12)
			return 1;
		if(s == -16 || s == -12)
			return 2;
	}

	for(int i = 0; i < 4; i++) {
		int s = board[i] + board[4 + i] + board[8 + i] + board[12 + i];
		if(s == 16 || s == 12)
			return 1;
		if(s == -16 || s == -12)
			return 2;
	}

	int s = board[0] + board[5] + board[10] + board[15];
	if(s == 16 || s == 12)
		return 1;
	if(s == -16 || s == -12)
		return 2;

	s = board[3] + board[6] + board[9] + board[12];
	if(s == 16 || s == 12)
		return 1;
	if(s == -16 || s == -12)
		return 2;	
	if(dots)
		return 4;
	else
		return 3;

}

int main() {
	int board[16] = {0};
	int n;
	char c;
	cin >> n;

	for(int i = 0; i < n; i++) {
		for(int j = 0; j < 4; j++)
			for(int k = 0; k < 4; k++) {
				cin >> c;
				switch(c) {
					case 'X':
						board[k * 4 + j] = 4;
						break;
					case 'O':
						board[k * 4 + j] = -4;
						break;
					case '.':
						board[k * 4 + j] = 1;
						break;
					case 'T':
						board[k * 4 + j] = 0;
						break;
					default:
						cout << "FUCK" << endl;
				}
			}
		int res = processOne(board);
		switch(res) {
			case 1:
				printf("Case #%d: X won\n", i + 1);
				break;
			case 2:
				printf("Case #%d: O won\n", i + 1);
				break;
			case 3:
				printf("Case #%d: Draw\n", i + 1);
				break;
			case 4:
				printf("Case #%d: Game has not completed\n", i + 1);
				break;
		}

	}

	return 0;
}