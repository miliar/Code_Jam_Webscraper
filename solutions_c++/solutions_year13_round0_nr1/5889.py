#include <iostream>

using namespace std;

char board[4][4];

int X_WIN = 'X'*4;
int X_T_WIN = 'X'*3 + 'T';
int O_WIN = 'O'*4;
int O_T_WIN = 'O'*3 + 'T';

void read(){
	for(int i=0; i<4;i++) for(int j=0; j<4; j++)
		cin >> board[i][j];
}

char determine(){
	bool fool = true;
	int sum_r, sum_c, sum_d1, sum_d2;
	
	// Rows
	sum_d1 = sum_d2 = 0;
	for(int i=0; i<4;i++){
		sum_r = 0; sum_c = 0;
		sum_d1 += board[i][i];
		sum_d2 += board[3-i][i];
		for(int j=0; j<4; j++){
			sum_r += board[i][j];
			sum_c += board[j][i];
			if(board[i][j] == '.') fool = false;
		}
		if((sum_r == O_T_WIN) || (sum_r == O_WIN)) return 'O';
		if((sum_r == X_T_WIN) || (sum_r == X_WIN)) return 'X';
		if((sum_c == O_T_WIN) || (sum_c == O_WIN)) return 'O';
		if((sum_c == X_T_WIN) || (sum_c == X_WIN)) return 'X';
	}
	if((sum_d1 == O_T_WIN) || (sum_d1 == O_WIN)) return 'O';
	if((sum_d2 == O_T_WIN) || (sum_d2 == O_WIN)) return 'O';
	if((sum_d1 == X_T_WIN) || (sum_d1 == X_WIN)) return 'X';
	if((sum_d2 == X_T_WIN) || (sum_d2 == X_WIN)) return 'X';
	
	if(fool) return 'D';
	return '-';
}

int main(int argc, char** argv){
	int n;
	cin >> n;
	for(int i=1; i<=n; i++){
		read();
		cout<<"Case #"<<i<<": ";
		switch(determine()){
		case 'X':
			cout<<"X won"<<endl; break;
		case 'O':
			cout<<"O won"<<endl; break;
		case 'D':
			cout<<"Draw"<<endl; break;
		case '-':
			cout<<"Game has not completed"<<endl; break;
		}
	}
	return 0;
}
