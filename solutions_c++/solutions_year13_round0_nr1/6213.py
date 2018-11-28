#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main(){

	int numCases=0;
	unsigned int cases = 0;
	string str;

	char board[6][6]; // board

	cin >> numCases;
	//getline(cin, str); // get rid of the newline char.

	int x, o, t, cnt;

	while(numCases--){
		x = 0;
		o = 0;

		cases++;

		gets(board[0]);

		for(int i = 0; i<4; i++){
			gets(board[i]);
		}

		for (int i = 0; i<4; i++){
			if((board[i][0] == 'X' || board[i][0] == 'T') &&
			 (board[i][1] == 'X' || board[i][1] == 'T') && 
			 (board[i][2] == 'X' || board[i][2] == 'T') &&
			 (board[i][3] == 'X' || board[i][3] == 'T')){
				x = 1;
				break;
			}
			if((board[i][0] == 'O' || board[i][0] == 'T') &&
			 (board[i][1] == 'O' || board[i][1] == 'T') && 
			 (board[i][2] == 'O' || board[i][2] == 'T') &&
			 (board[i][3] == 'O' || board[i][3] == 'T')){
				o = 1;
				break;
			}
		}


		for(int i = 0; i < 4; i++){
			if((board[0][i] == 'X' || board[0][i] == 'T') &&
			 (board[1][i] == 'X' || board[1][i] == 'T') &&
			 (board[2][i] == 'X' || board[2][i] == 'T') &&
			 (board[3][i] == 'X' || board[3][i] == 'T')){
				x = 1;
				break;
			}
			if((board[0][i] == 'O' || board[0][i] == 'T') &&
			 (board[1][i] == 'O' || board[1][i] == 'T') &&
			 (board[2][i] == 'O' || board[2][i] == 'T') &&
			 (board[3][i] == 'O' || board[3][i] == 'T')){
				o = 1;
				break;
			}
		}

		if((board[0][0] == 'X' || board[0][0] == 'T') &&
			 (board[1][1] == 'X' || board[1][1] == 'T') &&
			 (board[2][2] == 'X' || board[2][2] == 'T') &&
			 (board[3][3] == 'X' || board[3][3] == 'T')){
				x = 1;
		}

		if((board[0][0] == 'O' || board[0][0] == 'T') &&
			 (board[1][1] == 'O' || board[1][1] == 'T') &&
			 (board[2][2] == 'O' || board[2][2] == 'T') &&
			 (board[3][3] == 'O' || board[3][3] == 'T')){
				o = 1;
		}

		if((board[0][3] == 'X' || board[0][3] == 'T') &&
			 (board[1][2] == 'X' || board[1][2] == 'T') &&
			 (board[2][1] == 'X' || board[2][1] == 'T') &&
			 (board[3][0] == 'X' || board[3][0] == 'T')){
				x = 1;
		}

		if((board[0][3] == 'O' || board[0][3] == 'T') &&
			 (board[1][2] == 'O' || board[1][2] == 'T') &&
			 (board[2][1] == 'O' || board[2][1] == 'T') &&
			 (board[3][0] == 'O' || board[3][0] == 'T')){
				o = 1;
		}

		cout<<"Case #"<<cases<<": ";
		//cout<<"x: "<<x<<endl;
		//cout<<"o: "<<o<<endl;
		if (x==1){
			cout<<"X won"<<endl;
			continue;
		}
		if(o==1){
			cout<<"O won"<<endl;
			continue;
		}


		cnt=0;

		for (int i=0; i < 4; i++){
			for (int j = 0; j <4 ; j++){
				if (board[i][j] == '.')
					cnt++;
			}
		}

		if(cnt){
			cout<<"Game has not completed"<<endl;
		}else{
			cout<<"Draw"<<endl;
		}

	
	}//getline(cin, str);
	/*
	for (int i = 1; i <= numCases; ++i){
		getline(cin, str);
	}
	*/

	return 0;
}