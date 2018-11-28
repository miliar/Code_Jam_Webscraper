#include <iostream>

using namespace std;

int main() {

	int N;
	cin >> N;

	for(int n = 0; n < N; n++) {
		bool flag = false;


		char board[4][4];
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				char c;
				cin >> c;
				board[i][j] = c;
				// cout << board[i][j];
			}
			// cout << endl;
		}
		
		// cout << "i = 0, j = 3: " << board[0][3] << endl;

		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				// cout << "checking " << i << ", " << j << ": " << board[i][j] << endl;
				char current = board[i][j];
				if(current == '.' || current == 'T') {
					continue;
				} 
				if((board[i][0] == current || board[i][0] == 'T') && (board[i][1] == current || board[i][1] == 'T') && (board[i][2] == current || board[i][2] == 'T') && (board[i][3] == current || board[i][3] == 'T')) {
					cout << "Case #" << (n+1) << ": " << current << " won" << endl;
					i = 4;
					flag = true;
					break;
				}
				if((board[0][j] == current || board[0][j] == 'T') && (board[1][j] == current || board[1][j] == 'T') && (board[2][j] == current || board[2][j] == 'T') && (board[3][j] == current || board[3][j] == 'T')) {
					cout << "Case #" << (n+1) << ": " << current << " won" << endl;
					i = 4;
					flag = true;
					break;
				}
				if(i == j) {
					if((board[0][0] == current || board[0][0] == 'T') && (board[1][1] == current || board[1][1] == 'T') && (board[2][2] == current || board[2][2] == 'T') && (board[3][3] == current || board[3][3] == 'T')) {
						cout << "Case #" << (n+1) << ": " << current << " won" << endl;
						i = 4;
						flag = true;
						break;
					}
				}
				if((i==0 && j == 3) || (i==1 && j == 2) || (i==2 && j == 1) || (i==3 && j == 0)) {
					if((board[0][3] == current || board[0][3] == 'T') && (board[1][2] == current || board[1][2] == 'T') && (board[2][1] == current || board[2][1] == 'T') && (board[3][0] == current || board[3][0] == 'T')) {
						cout << "Case #" << (n+1) << ": " << current << " won" << endl;
						i = 4;
						flag = true;
						break;
					}
				}
				
			}
		}
		//draw or incomplete
		if(flag == false) {
			for(int i = 0; i < 4; i++) {
				for(int j = 0; j < 4; j++) {
					if(board[i][j] == '.') {
						cout << "Case #" << (n+1) << ": " << "Game has not completed" << endl;
							i = 4;
							flag = true;
							break;
					}
				}
			}
		}
		if(flag == false) {
			cout << "Case #" << (n+1) << ": " << "Draw" << endl;
		}
	}

}