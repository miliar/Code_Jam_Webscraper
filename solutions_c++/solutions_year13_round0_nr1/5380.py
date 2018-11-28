#include <iostream>
#include <string>

using namespace std;

int main(){
	long K;
	cin >> K;
	for(int k = 0; k< K; ++k){
		cout << "Case #" << k+1 <<  ": ";
		string board[4];
		for (int i = 0; i < 4; ++i)
		{
			cin >> board[i];
		}

		//i has board
		bool done = false;
		long X,O,T,emp;
		emp= 0;
		//rows
		for(int y = 0; y < 4; y++){
			X = 0;
			O = 0;
			T = 0;

			for(int x =0; x<4; x++){
				if(board[y][x] == 'X')
					X++;
				if(board[y][x] == 'O')
					O++;
				if(board[y][x] == 'T')
					T++;
				if(board[y][x] == '.')
					emp++;
			}

			if(X+T > 3){
				cout << "X won" << endl;
				done = true;
				break;
			} else if(O+T > 3){
				cout << "O won" << endl;
				done = true;
				break;
			}

		}
		//cols
		for(int x = 0; x < 4; x++){
			if(done) break;
			X = 0;
			O = 0;
			T = 0;

			for(int y =0; y<4; y++){
				if(board[y][x] == 'X')
					X++;
				if(board[y][x] == 'O')
					O++;
				if(board[y][x] == 'T')
					T++;
			}

			if(X+T > 3){
				cout << "X won" << endl;
				done = true;
				break;
			} else if(O+T > 3){
				cout << "O won" << endl;
				done = true;
				break;
			}

		}
		//diags
		if(done) continue;

		X = 0;
		O = 0;
		T = 0;
		//down
		for(int i = 0; i < 4; i++){
			if(board[i][i] == 'X')
				X++;
			if(board[i][i] == 'O')
				O++;
			if(board[i][i] == 'T')
				T++;

			if(X+T > 3){
				cout << "X won" << endl;
				done = true;
				break;
			} else if(O+T > 3){
				cout << "O won" << endl;
				done = true;
				break;
			}
		}
		X = 0;
		O = 0;
		T = 0;
		//up
		for(int i = 0; i < 4; i++){
			if(board[i][3-i] == 'X')
				X++;
			if(board[i][3-i] == 'O')
				O++;
			if(board[i][3-i] == 'T')
				T++;

			if(X+T > 3){
				cout << "X won" << endl;
				done = true;
				break;
			} else if(O+T > 3){
				cout << "O won" << endl;
				done = true;
				break;
			}
		}

		if(done) continue;

		if(emp > 0)
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;
	}
}