#include<iostream>
#include<string>
#include<iomanip>
#include <cstdio>
using namespace std;

string board[4];
string boardInstance[4];

int checkBoard() {
	int complete =0;
	//row
	for (int i = 0; i < 4; i++) {
		if (board[i] == "XXXX" || boardInstance[i] == "XXXX")
			return 1; // x won
		if (board[i] =="OOOO" || boardInstance[i] =="OOOO")
			return 2; // O won
	}
	//column and diagonal and complete
	string temp1d ="";
	string temp2d ="";

	string temp1dd ="";
	string temp2dd ="";

	string temp1c ="";
	string temp2c ="";

	for(int i = 0 ; i < 4 ; i++)
	{
		for(int j = 0 ; j < 4 ; j++)
		{
			temp1c+= board[j][i], temp2c+= boardInstance[j][i];
			if( i == j) temp1d +=board[i][j], temp2d += boardInstance[i][j];
			if( i+j == 3) temp1dd +=board[i][j], temp2dd += boardInstance[i][j];
			if(board[i][j]!='.') complete++;
		}

		if( temp1c =="XXXX" || temp1d =="XXXX" || temp1dd =="XXXX") return 1;
		if( temp2c =="OOOO" || temp2d =="OOOO" || temp2dd =="OOOO") return 2;
	}
	if(complete ==16) return 0;

return -1; // game is not completed
}
int main() {

	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int nCases;
	cin >> nCases;
	for (int i = 1; i <= nCases; i++) {
		for (int j = 0; j < 4; j++) {
				cin >> board[j];
				boardInstance[j] = board[j];
				for(int k = 0 ; k < 4 ; k++){
				if (board[j][k] == 'T') {
					board[j][k] = 'X';
					boardInstance[j][k] = 'O';
				}
			}
		}
		//for (int j = 0; j < 4; j++) cout<<board[j]<<endl;
		int idx = checkBoard();
		if( idx == 1)
			cout << "Case #" << i << ": " <<"X won"<< endl;
		if( idx == 2)
			cout << "Case #" << i << ": " <<"O won"<< endl;
		if( idx == 0)
			cout << "Case #" << i << ": " <<"Draw"<< endl;
		if( idx == -1)
			cout << "Case #" << i << ": " <<"Game has not completed"<< endl;

	}
	return 0;
}
