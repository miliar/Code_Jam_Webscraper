#include <iostream>
#include <string>

using namespace std;

int main(int argc, char** argv){
	unsigned int T;
	cin >> T;

	char board[4][4];
	for(int t=1; t<=T; ++t) {
		bool filled = true;
		bool done = false;

		for(int i=0; i<4; ++i){
			for(int j=0; j<4; ++j){
				cin >> board[i][j]; 
				if(board[i][j] == '.') filled = false;
			}
		}

		for(int i=0; i<4; ++i){
			char symbol = board[i][0];
			if(symbol == 'T') symbol = board[i][1];
			if(symbol == '.') continue;

			if(symbol != board[i][1] && board[i][1] != 'T') continue;
			if(symbol != board[i][2] && board[i][2] != 'T') continue;
			if(symbol != board[i][3] && board[i][3] != 'T') continue;
			
			cout << "Case #" << t << ": " << symbol << " won" << endl;
			done = true;
			break;
		}
		if(done) continue;

		for(int i=0; i<4; ++i){
			char symbol = board[0][i];
			if(symbol == 'T') symbol = board[1][i];
			if(symbol == '.') continue;

			if(symbol != board[1][i] && board[1][i] != 'T') continue;
			if(symbol != board[2][i] && board[2][i] != 'T') continue;
			if(symbol != board[3][i] && board[3][i] != 'T') continue;
			
			cout << "Case #" << t << ": " << symbol << " won" << endl;
			done = true;
			break;
		}
		if(done) continue;

		{
			char symbol = board[0][0];
			if(symbol == 'T') symbol = board[1][1];
			if(symbol != '.'
				&& (symbol == board[1][1] || board[1][1] == 'T') 
				&& (symbol == board[2][2] || board[2][2] == 'T')
				&& (symbol == board[3][3] || board[3][3] == 'T'))
			{
				cout << "Case #" << t << ": " << symbol << " won" << endl;
				continue;
			}
		}

		{
			char symbol = board[0][3];
			if(symbol == 'T') symbol = board[1][2];
			if(symbol != '.'
				&& (symbol == board[1][2] || board[1][2] == 'T') 
				&& (symbol == board[2][1] || board[2][1] == 'T')
				&& (symbol == board[3][0] || board[3][0] == 'T'))
			{
				cout << "Case #" << t << ": " << symbol << " won" << endl;
				continue;
			}
		}

		if(filled) cout << "Case #" << t << ": " << "Draw" << endl;
		else cout << "Case #" << t << ": " << "Game has not completed" << endl;
	}

	return 0;
}
