#include <iostream>
#include <fstream>
using namespace std;

ofstream mycout;

void process(int testcase){
	char board[4][4];
	int Ti, Tj, empty = 0;
	string str;
	char c;
	int f;
	
	for(int i = 0; i < 4; i++){
		cin >> str;
		for(int j = 0; j < 4; j++){
			board[i][j] = str[j];
			if(board[i][j] == 'T'){
				Ti = i;
				Tj = j;
			}
			if(board[i][j] == '.')
				empty++;
		}
	}
	
	mycout << "Case #" << testcase << ": ";
	for(int i = 0; i < 4; i++){
		c = '-';
		f = 1;
		for(int j = 0; j < 4; j++){
			if(board[i][j] == '.'){
				f = 0;
				break;
			}	
			if(board[i][j] == 'T')
				continue;
			if(c == '-'){
				c = board[i][j];
				continue;
			}
			if( c != board[i][j] ){
				f = 0;
				break;
			}
		}
	
		if( f == 1){
			if(board[i][0] == 'T')
				mycout << board[i][1] << " won" << endl;
			else
				mycout << board[i][0] << " won" << endl;
			
			return;
		}
	}
	
	for(int j = 0; j < 4; j++){
		c = '-';
		f = 1;
		for(int i = 0; i < 4; i++){
			if(board[i][j] == '.'){
				f = 0;
				break;
			}	
			
			if( board[i][j] == 'T')
				continue;
			if(c == '-'){
				c = board[i][j];
				continue;
			}
			if( c != board[i][j] ){
				f = 0;
				break;
			}	
		}
		
		if( f == 1){
			if(board[0][j] == 'T')
				mycout << board[1][j] << " won" << endl;
			else
				mycout << board[0][j] << " won" << endl;
			
			return;	
		}
	}
	
	c = '-';
	f = 1;
	for(int k = 0; k < 4; k++){
	
		if(board[k][k] == '.'){
			f = 0;
			break;
		}
		if(board[k][k] == 'T')
			continue;
		if( c == '-'){
			c = board[k][k];
			continue;
		}
		if( c != board[k][k]){
			f = 0;
			break;
		}
	}
	
	if(f){
		if(board[3][3] == 'T')
			mycout << board[2][2] << " won" << endl;
		else
			mycout << board[3][3] << " won" << endl;	
		return;	
	}
	
	c = '-';
	f = 1;
	
	for(int k = 0; k < 4; k++){
		if(board[3-k][k] == '.'){
			f = 0;
			break;
		}
		if(board[3-k][k] == 'T')
			continue;
		if( c == '-')
			c = board[3-k][k];
		if( c != board[3-k][k] ){
			f = 0; 
			break;
		}
	}
	
	if(f){
		if(board[0][3] == 'T')
			mycout << board[1][2] << " won" << endl;
		else
			mycout << board[0][3] << " won" << endl;	
		return;	
	}	
	
	if(empty == 0)
		mycout << "Draw" << endl;
	else
		mycout << "Game has not completed" << endl;
}

int main(){
	int T;
	cin >> T;
	
	string s;
	
	mycout.open ("output.txt");
	for(int i = 0; i < T; i++){
		process(i+1);
	}	
	mycout.close();
}
