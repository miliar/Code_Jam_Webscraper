#include <fstream>
using namespace std;

int main(){
	ifstream cin;
	ofstream cout;
	cin.open("A-large.in");
	cout.open("QR1_Loutput.txt");
	int N;
	cin >> N;
	for(int n=0 ; n<N ; n++){
		char winner = 'D';
		char **board = new char*[4];
		for(int i=0 ; i<4 ; i++){
			board[i] = new char[4];
			for(int j=0 ; j<4 ; j++){
				cin >> board[i][j];
				if(board[i][j] == '.'){
					winner = 'N';
				}
			}
		}

		char temp;
		// chaeck horizontally
		for(int i=0 ; i<4 ; i++){
			if(board[i][0] != '.' && board[i][1] != '.'){
				temp = (board[i][0] != 'T')? board[i][0]: board[i][1];
				for(int j=1 ; j<4 ; j++){
					if(!(temp == board[i][j] || board[i][j]=='T')){
						temp = 'N';
						break;
					}
				}
				if(temp!='N'){winner = temp ;break;}
			}
		}

		//check vertically
		if(winner=='N' || winner == 'D'){
			for(int i=0 ; i<4 ; i++){
				if(board[0][i] != '.' && board[1][i] != '.'){
					temp = (board[0][i] != 'T')? board[0][i]: board[1][i];
					for(int j=1 ; j<4 ; j++){
						if(!(temp == board[j][i] || board[j][i]=='T')){
							temp = 'N';
							break;
						}
					}
					if(temp!='N'){winner = temp;  break;}
				}
			}
		}

		//check cross
		if(winner == 'N' || winner == 'D'){
			if(board[0][0] != '.' && board[1][1] !='.'){
				temp = (board[0][0] !='T')? board[0][0] : board[1][1];
				for(int j=0 ; j<4 ; j++){
					if(!(temp==board[j][j] || board[j][j] == 'T')){
						temp = 'N';
						break;
					}
				}
				if(temp!= 'N'){winner = temp;}
			}
		}

		if(winner == 'N' || winner == 'D'){
			if(board[0][3] != '.' && board[1][2] !='.'){
				temp = (board[0][3] !='T')? board[0][3] : board[1][2];
				for(int j=0 ; j<4 ; j++){
					if(!(temp==board[j][3-j] || board[j][3-j] == 'T')){
						temp = 'N';
						break;
					}
				}
				if(temp != 'N'){winner = temp;}
			}
		}

		cout << "Case #" << n+1 << ": ";
		switch(winner){
		case 'N' : cout << "Game has not completed" << endl; break;
		case 'O' : cout << "O won" << endl; break;
		case 'X' : cout << "X won" << endl; break;
		case 'D' : cout << "Draw" << endl; break;
		}
	}
	cin.close();
	cout.close();
}